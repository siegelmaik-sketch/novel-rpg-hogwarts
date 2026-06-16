<div align="center">

# 🏰 Hogwarts RPG

### Ein altersgerechtes, story-getriebenes Zauberschul-Abenteuer (~12 Jahre) als Skill für Claude Code / OpenClaw

*A story-driven, age-appropriate (~12) Hogwarts adventure as a skill for Claude Code / OpenClaw.
German content, seven full school years, built-in child-safety layer. Built on the
[`novel-rpg`](https://github.com/kiki123124/novel-rpg) engine.*

[![License: MIT](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab.svg?logo=python&logoColor=white)
![Sprache](https://img.shields.io/badge/Inhalt-Deutsch-informational.svg)
![Altersfreigabe](https://img.shields.io/badge/Alter-~12%20%C2%B7%20kindersicher-ff69b4.svg)
![Skill](https://img.shields.io/badge/Claude%20Code%20%2F%20OpenClaw-Skill-7c3aed.svg)
![Fan-Projekt](https://img.shields.io/badge/Fan--Projekt-nicht%20kommerziell-lightgrey.svg)

**7 Schuljahre · 857 Szenen · 397 Bindungsmomente · 38 Figuren — eine durchgehende Saga, ein Spielstand.**

</div>

---

Du spielst nicht Harry. Du spielst **Robin** — ein elfjähriges, muggelstämmiges Mädchen,
die Erste ihrer Familie auf einer Zauberschule. Es beginnt zu Hause, mit einem Brief, einem
Abschied und einer ersten Reise durch die **Winkelgasse** an der Seite deiner Freundin **Lily**
und deines Malteser-Hündchens **Flocke**. An Gleis 9¾ übernimmt der Kanon — und von da an
erlebst du **sieben komplette Schuljahre** als eine zusammenhängende Geschichte, in der Harry,
Ron, Hermine & Co. die Nebenfiguren in *deiner* Geschichte sind.

> 🎩 **Dein Haus ist frei wählbar** (alle vier, an der Hut-Zeremonie). Freundschaften und der
> „Freundeskreis“/Clique-Mechanismus funktionieren **hausübergreifend** — ein Gryffindor und
> ein Slytherin dürfen beste Freunde sein.

---

## ✨ Ein Blick ins Spiel

> *Ausschnitt aus dem Prolog — wie sich eine Runde anfühlt:*

```text
WINKELGASSE · OLLIVANDERS ZAUBERSTABLADEN

Staub tanzt in den schmalen Lichtbahnen zwischen tausenden schmaler Schachteln,
die sich bis unter die Decke stapeln. Flocke drückt sich eng an dein Bein und
winselt leise. Lily hält dir den Arm fest.
„Probier den da", flüstert sie. „Der hat geleuchtet, als du reingekommen bist.
Ehrlich. Ich hab's gesehen."
Herr Ollivander tritt lautlos aus dem Schatten zwischen den Regalen.
„Eschenholz, Einhornhaar, neunundzwanzig Zentimeter", sagt er und legt dir die
Schachtel in die Hände. „Nun. Mal sehen, wer hier wen gewählt hat."

  Was tust du?
  › 1  Den Zauberstab vorsichtig heben und ihn schwingen
    2  Erst Flocke beruhigen, bevor du irgendetwas anfasst
    3  Lily fragen, was sie genau gesehen hat
    4  (frei) etwas anderes sagen oder tun
```

Du schreibst frei — die Engine erzählt daraus eine Szene, merkt sich, was du erschaffst,
und führt dich (sanft) zurück auf den roten Faden, wenn du zu weit abdriftest.

---

## 🧭 Was es besonders macht

- 🛡️ **Kindersicher von Grund auf** — eine durchgehende Moderations- und Ton-Architektur,
  die **nicht durch Spielereingaben überschreibbar** ist. Das ist die eigentliche
  wiederverwendbare Zutat dieses Projekts.
- 📖 **Eine echte Saga, kein Episoden-Flickwerk** — sieben Jahre nahtlos im selben Spielstand,
  Freundschaften wachsen über Jahre.
- 🪄 **Freiheit lebt in den Lücken** — frei zwischen den Story-Beats bewegen (Sandkasten +
  Orts-Whitelist), während der Kanon der verlässliche rote Faden bleibt.
- 🧠 **Persistentes Welt-Gedächtnis** — das Spiel merkt sich, was *du* erfindest, und webt es
  später wieder ein.
- 🎭 **Du bist die Heldin** — Harry & Co. sind Nebenfiguren in deiner Geschichte, nicht umgekehrt.
- 🤖 **Läuft als Skill** in Claude Code / OpenClaw — plus optionale **Telegram-Anbindung**
  (`frontend/telegram_bridge.py`).

---

## 📜 Umfang

| | |
|---|---|
| Schuljahre | **7** (komplette Saga, nahtlos im selben Spielstand) |
| Szenen | **857** |
| Kreuzungspunkte (Bindungsmomente) | **397** |
| Figuren | **38** (mit fest verdrahteter Stimme/Motiv, inkl. aller Lehrer) |

Inhalt ist handkuratiert/generiert (`build_year.py` … `build_year7.py`) — reproduzierbar
und erweiterbar. Die Beats sind **Szenen-Seeds** (Ort, Situation, Auswahlmöglichkeiten);
die eigentliche Erzählung schreibt das Modell daraus zur Laufzeit.

## 🧸 Ton & Sicherheit (~12, Niveau der Vorlage)

- **Altersgerecht für ~12:** Spannung, Geheimnis und auch mal echter Grusel sind
  erwünscht; **altersgerechte Romantik** (Verknalltsein, Tanzen, ein erster Kuss) ist
  okay. **Tabu bleibt nur explizit Sexuelles, Gore/Folter mit Details, Drogen,
  Selbstgefährdung, echte Grausamkeit.**
- **Die düstersten Kanon-Momente** (z. B. der Verlust geliebter Figuren) werden mit
  **Ernst und Würde, aber ohne grausige Bilder** erzählt; Erwachsene führen, schützen
  und trösten.

## 🔧 Was dieser Fork beiträgt (wiederverwendbar)

| Baustein | Datei | Zweck |
|---|---|---|
| **Output-Moderation** | `skill/scripts/moderation.py` | Jede Szene/jeder Fakt wird geprüft, **bevor** er angezeigt/gespeichert wird. Fail-Closed, Incident-Log. Backends: LLM-Klassifizierer (gleiche Modell-Auth), OpenAI-`/moderations`, oder Offline-Wortliste. |
| **Divergenz-Cap** | `skill/scripts/game_engine.py` | Harte Obergrenze, ab der keine Nicht-Kanon-Pfade mehr möglich sind. |
| **Sandkasten + Orts-Whitelist** | `game_engine.py` / `locations.json` | Freie Bewegung *zwischen* Beats, aber nur zu erlaubten Orten. Divergenz-neutral. |
| **Kreuzungspunkte + autonome Kanon-Spur** | `plot_graph.json` | Andocken oder nacherzählt erleben — beide Pfade führen zum selben nächsten Beat. |
| **Persistentes Welt-Memory** | `skill/scripts/world_memory.py` | Merkt selbst erschaffene Sandkasten-Inhalte — mit **Moderation beim Schreiben**, Relevanz-Injektion, Summarization und **Eltern-Fenster** (`list`/`remove`/`clear`). |
| **Alters-/Ton-Härtung** | `skill/SKILL.md` (Abschnitt 0) | Ton + Grenzen fest verdrahtet, **nicht durch Spielereingaben überschreibbar**. |

## 🚀 Setup

```bash
pip install -r requirements.txt
openclaw skills install ./skill --as hogwarts-rpg
python3 skill/scripts/book_manager.py init-builtins

# Moderation (Pflicht), z. B.:
#   MODERATION_MODE=openclaw   (Klassifizierung über dieselbe Modell-Auth, kein Extra-Key)
#   MODERATION_MODE=openai + OPENAI_MOD_KEY=...
#   MODERATION_MODE=local      (nur Offline-Wortliste, für Tests)
```

Spielstände/Welt-Memory/Incident-Log liegen **außerhalb** des Skills unter
`~/.openclaw/hogwarts-state/` (via `HOGWARTS_STATE_DIR`) und überleben Reinstalls.

## 👨‍👩‍👧 Werkzeuge für Eltern / Betreiber

```bash
python3 skill/scripts/world_memory.py list   <save-id>   # was sich das Spiel gemerkt hat
python3 skill/scripts/world_memory.py remove <save-id> <fact-id>
python3 skill/scripts/world_memory.py clear  <save-id>
cat ~/.openclaw/hogwarts-state/moderation_log/*.jsonl     # Moderations-Vorfälle
```

## ✅ Tests

```bash
python3 -m pytest tests/ -q
```
Abgedeckt: Divergenz-Cap, Kreuzungen/Clique-Regel, autonome Spur, Sandkasten-Whitelist,
Moderation (inkl. Fail-Closed), Welt-Memory (Capture/Moderation-Reject/Relevanz/
Summarization/Eltern-CLI).

## ⚖️ Lizenz & Disclaimer

MIT — siehe [LICENSE](LICENSE). Basiert auf
[kiki123124/novel-rpg](https://github.com/kiki123124/novel-rpg) (ebenfalls MIT).

> **Nicht-kommerzielles Fan-Projekt** zu privaten/Bildungszwecken. „Harry Potter“ und die
> Hogwarts-Welt sind © J. K. Rowling / Warner Bros.; dieses Projekt steht in **keiner
> Verbindung** zu den Rechteinhabern. Es wird **kein Buchtext** verwendet — nur
> handkuratierte/generierte Metadaten + Modellwissen (eigene Paraphrasen der Handlungs-Beats),
> genau im Geiste der Built-in-Bücher der Vorlage.
