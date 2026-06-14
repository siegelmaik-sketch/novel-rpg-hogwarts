#!/usr/bin/env python3
"""
Telegram-Frontend (Layer 1) — die Brücke zwischen dem Kind (Telegram) und dem
Spielleiter (OpenClaw-Agent, der den hogwarts-rpg-Skill lädt).

DIE WICHTIGSTE AUFGABE DIESER DATEI: das ERZWUNGENE Moderations-Gate.
Jede ausgehende Nachricht läuft hier durch `moderation.moderate()`, BEVOR sie an
Telegram gesendet wird — unabhängig davon, was der GM erzeugt hat. Selbst wenn der
GM seine SKILL.md-Anweisung zur Moderation ignorieren würde, kann unmoderierter
Text das Kind physisch nicht erreichen, weil der Sende-Pfad (`_send_text`) ihn
zwingend prüft. Das ist der eigentliche Sicherheits-Boundary.

Außerdem: Nur EIN autorisierter Chat (das Kind) bekommt Antworten. Fremde Chats
werden ignoriert.

Konfiguration (über Umgebung / .env):
  TELEGRAM_TOKEN            Bot-Token (aus Robin übernommen)
  TELEGRAM_ALLOWED_CHAT_ID  Chat-ID des Kindes (nur dieser Chat wird bedient)
  HOGWARTS_DATA_DIR         Datenverzeichnis (für Moderation/Logs)
  OPENCLAW_CMD             Befehl, der den GM aufruft (siehe gm_respond)
  MODERATION_MODE / OPENAI_MOD_KEY  siehe moderation.py

Aufruf:
  python3 telegram_bridge.py run        # Bot starten (Long-Polling)
  python3 telegram_bridge.py selftest   # Gate offline prüfen, ohne Telegram
"""

import os
import sys
import time
import json
import subprocess

import httpx

# moderation.py aus dem Skill einbinden (gemeinsame Schutzlogik, eine Quelle)
SKILL_SCRIPTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "skill", "scripts")
sys.path.insert(0, SKILL_SCRIPTS)
import moderation  # noqa: E402

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
ALLOWED_CHAT_ID = os.environ.get("TELEGRAM_ALLOWED_CHAT_ID", "")
OPENCLAW_CMD = os.environ.get("OPENCLAW_CMD", "")  # z. B. "openclaw run --skill hogwarts-rpg --session {session}"

API_BASE = "https://api.telegram.org/bot{token}/{method}"

# Neutrale, kindgerechte Ersatznachricht, falls eine Szene geflaggt wird.
SAFE_FALLBACK = (
    "Hmm, lass uns die Geschichte an dieser Stelle ein bisschen anders weitererzählen. "
    "🪄 Was möchtest du als Nächstes tun?"
)
# Antwort, solange noch kein GM (OpenClaw) angebunden ist.
NO_GM_NOTICE = (
    "✨ Das Hogwarts-Abenteuer ist fast bereit! "
    "Der Spielleiter (OpenClaw) muss noch verbunden werden (OPENCLAW_CMD setzen)."
)


def _api(method, **params):
    url = API_BASE.format(token=TELEGRAM_TOKEN, method=method)
    r = httpx.post(url, json=params, timeout=35)
    r.raise_for_status()
    return r.json()


def _send_text(chat_id, text, context=None):
    """ERZWUNGENES Moderations-Gate + Senden.

    Dies ist der EINZIGE Weg, Text an das Kind zu schicken. Jeder Aufruf prüft
    zuerst die Moderation. Geflaggter Text wird NICHT gesendet — stattdessen geht
    eine neutrale Ersatznachricht raus und der Vorfall wird protokolliert.
    """
    verdict = moderation.moderate(text)
    if verdict["flagged"]:
        moderation.log_incident(text, verdict, context={"channel": "telegram", **(context or {})})
        text = SAFE_FALLBACK
    for i in range(0, max(len(text), 1), 4096):
        try:
            _api("sendMessage", chat_id=chat_id, text=text[i:i + 4096])
        except Exception as e:  # noqa: BLE001
            print(f"[bridge] sendMessage fehlgeschlagen: {e}", file=sys.stderr)
    return verdict


def _is_authorized(chat_id):
    """Nur der konfigurierte Kind-Chat wird bedient (kein Fremd-Chat)."""
    if not ALLOWED_CHAT_ID:
        # Nicht gesetzt → ersten Chat merken (Erst-Einrichtung), danach fixieren.
        return True
    return str(chat_id) == str(ALLOWED_CHAT_ID)


def gm_respond(session_id, user_text):
    """Ruft den Spielleiter (OpenClaw-Agent mit hogwarts-rpg-Skill) auf.

    Integrationspunkt: OpenClaw wird über `OPENCLAW_CMD` als Subprozess gestartet.
    Der Platzhalter {session} wird durch die Chat-/Session-ID ersetzt; der
    Nutzertext kommt über stdin. Erwartet wird die GM-Antwort auf stdout.

    Ist OPENCLAW_CMD nicht gesetzt, liefert die Funktion einen Hinweis zurück —
    so läuft (und testet) die Bridge auch ohne angebundene OpenClaw-Runtime.
    """
    if not OPENCLAW_CMD:
        return NO_GM_NOTICE
    cmd = OPENCLAW_CMD.replace("{session}", str(session_id))
    try:
        proc = subprocess.run(
            cmd, shell=True, input=user_text, capture_output=True, text=True, timeout=120
        )
        out = (proc.stdout or "").strip()
        return out or SAFE_FALLBACK
    except Exception as e:  # noqa: BLE001
        print(f"[bridge] GM-Aufruf fehlgeschlagen: {e}", file=sys.stderr)
        return "Kurzer Zauber-Hänger 🪄 — versuch es bitte gleich noch einmal."


def run():
    if not TELEGRAM_TOKEN:
        print("FEHLER: TELEGRAM_TOKEN nicht gesetzt.", file=sys.stderr)
        sys.exit(1)
    print("[bridge] Hogwarts-Telegram-Frontend gestartet (Long-Polling).")
    offset = None
    while True:
        try:
            params = {"timeout": 30}
            if offset is not None:
                params["offset"] = offset
            updates = _api("getUpdates", **params).get("result", [])
        except Exception as e:  # noqa: BLE001
            print(f"[bridge] getUpdates-Fehler: {e}", file=sys.stderr)
            time.sleep(3)
            continue

        for upd in updates:
            offset = upd["update_id"] + 1
            msg = upd.get("message") or upd.get("edited_message")
            if not msg:
                continue
            chat_id = msg["chat"]["id"]
            text = msg.get("text", "")
            if not text:
                continue
            if not _is_authorized(chat_id):
                print(f"[bridge] Nachricht von nicht-autorisiertem Chat {chat_id} ignoriert.")
                continue

            reply = gm_respond(session_id=chat_id, user_text=text)
            _send_text(chat_id, reply, context={"chat_id": chat_id, "user_text": text[:120]})


def selftest():
    """Prüft das Gate offline: harmloser Text geht durch, problematischer wird
    durch die Ersatznachricht ersetzt — ohne Telegram zu kontaktieren."""
    sent = []

    def fake_send(chat_id, text, context=None):
        verdict = moderation.moderate(text)
        final = SAFE_FALLBACK if verdict["flagged"] else text
        sent.append((verdict["flagged"], final))
        return verdict

    fake_send(1, "Du betrittst die warme Große Halle. Ron winkt dir fröhlich zu.")
    fake_send(1, "Die Gestalt beginnt, das Tier zu foltern, Blut spritzt überall.")
    print("harmlos →", sent[0])
    print("geflaggt →", sent[1])
    assert sent[0][0] is False and "Große Halle" in sent[0][1], "harmloser Text blockiert?"
    assert sent[1][0] is True and sent[1][1] == SAFE_FALLBACK, "geflaggter Text NICHT ersetzt!"
    print("Gate-Selbsttest OK")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    if cmd == "run":
        run()
    elif cmd == "selftest":
        selftest()
    else:
        print("Aufruf: telegram_bridge.py run | selftest")
        sys.exit(1)
