# Hogwarts RPG — altersgerechtes Novel-RPG-Skill (~12)

*A story-driven, age-appropriate (~12) Hogwarts adventure as a skill for OpenClaw /
Claude Code. German content. Built on the
[`novel-rpg`](https://github.com/kiki123124/novel-rpg) engine.*

Eine **story-getriebene Hogwarts-Variante** der Novel-RPG-Engine, ausgelegt fuer etwa
**12 Jahre** (Niveau der Harry-Potter-Buecher/Filme). Man spielt eine **eigene Figur**
(Vorgabe „Robin", frei umbenennbar) und erlebt — beginnend mit einem eigenen Prolog —
**sieben komplette Schuljahre** als durchgehende Geschichte: Freundschaften wachsen,
der Kanon ist der rote Faden, und **Freiheit lebt in den Luecken** zwischen den Beats.

> **Disclaimer:** Nicht-kommerzielles **Fan-Projekt** zu privaten/Bildungszwecken.
> „Harry Potter" und die Hogwarts-Welt sind © J. K. Rowling / Warner Bros.; dieses
> Projekt steht in keiner Verbindung zu den Rechteinhabern. Es wird **kein Buchtext**
> verwendet — nur handkuratierte/generierte Metadaten + Modellwissen (eigene
> Paraphrasen der Handlungs-Beats), genau im Geiste der Built-in-Buecher der Vorlage.

Basiert auf **[kiki123124/novel-rpg](https://github.com/kiki123124/novel-rpg)** (MIT) und
fuegt eine durchgaengige **Sicherheits-/Alters-Architektur** hinzu — die eigentliche
wiederverwendbare Zutat dieses Forks.

---

## Umfang

| | |
|---|---|
| Schuljahre | **7** (komplette Saga, nahtlos im selben Spielstand) |
| Szenen | **857** |
| Kreuzungspunkte (Bindungsmomente) | **397** |
| Figuren | 38 (mit fest verdrahteter Stimme/Motiv, inkl. aller Lehrer) |

Inhalt ist handkuratiert/generiert (`build_year.py` … `build_year7.py`) — reproduzierbar
und erweiterbar. Die Beats sind **Szenen-Seeds** (Ort, Situation, Auswahlmoeglichkeiten);
die eigentliche Erzaehlung schreibt das Modell daraus zur Laufzeit.

## Ton & Sicherheit (~12, Niveau der Vorlage)

- **Altersgerecht fuer ~12:** Spannung, Geheimnis und auch mal echter Grusel sind
  erwuenscht; **altersgerechte Romantik** (Verknalltsein, Tanzen, ein erster Kuss) ist
  okay. **Tabu bleibt nur explizit Sexuelles, Gore/Folter mit Details, Drogen,
  Selbstgefaehrdung, echte Grausamkeit.**
- **Die duestersten Kanon-Momente** (z. B. der Verlust geliebter Figuren) werden mit
  **Ernst und Wuerde, aber ohne grausige Bilder** erzaehlt; Erwachsene fuehren, schuetzen
  und troesten.

## Was dieser Fork beitraegt (wiederverwendbar)

| Baustein | Datei | Zweck |
|---|---|---|
| **Output-Moderation** | `skill/scripts/moderation.py` | Jede Szene/jeder Fakt wird geprueft, **bevor** er angezeigt/gespeichert wird. Fail-Closed, Incident-Log. Backends: LLM-Klassifizierer (gleiche Modell-Auth), OpenAI-`/moderations`, oder Offline-Wortliste. |
| **Divergenz-Cap** | `skill/scripts/game_engine.py` | Harte Obergrenze, ab der keine Nicht-Kanon-Pfade mehr moeglich sind. |
| **Sandkasten + Orts-Whitelist** | `game_engine.py` / `locations.json` | Freie Bewegung *zwischen* Beats, aber nur zu erlaubten Orten. Divergenz-neutral. |
| **Kreuzungspunkte + autonome Kanon-Spur** | `plot_graph.json` | Andocken oder nacherzaehlt erleben — beide Pfade fuehren zum selben naechsten Beat. |
| **Persistentes Welt-Memory** | `skill/scripts/world_memory.py` | Merkt selbst erschaffene Sandkasten-Inhalte — mit **Moderation beim Schreiben**, Relevanz-Injektion, Summarization und **Eltern-Fenster** (`list`/`remove`/`clear`). |
| **Alters-/Ton-Haertung** | `skill/SKILL.md` (Abschnitt 0) | Ton + Grenzen fest verdrahtet, **nicht durch Spielereingaben ueberschreibbar**. |

## Setup

```bash
pip install -r requirements.txt
openclaw skills install ./skill --as hogwarts-rpg
python3 skill/scripts/book_manager.py init-builtins

# Moderation (Pflicht), z. B.:
#   MODERATION_MODE=openclaw   (Klassifizierung ueber dieselbe Modell-Auth, kein Extra-Key)
#   MODERATION_MODE=openai + OPENAI_MOD_KEY=...
#   MODERATION_MODE=local      (nur Offline-Wortliste, fuer Tests)
```

Spielstaende/Welt-Memory/Incident-Log liegen **ausserhalb** des Skills unter
`~/.openclaw/hogwarts-state/` (via `HOGWARTS_STATE_DIR`) und ueberleben Reinstalls.

## Werkzeuge fuer Eltern / Betreiber

```bash
python3 skill/scripts/world_memory.py list   <save-id>   # was sich das Spiel gemerkt hat
python3 skill/scripts/world_memory.py remove <save-id> <fact-id>
python3 skill/scripts/world_memory.py clear  <save-id>
cat ~/.openclaw/hogwarts-state/moderation_log/*.jsonl     # Moderations-Vorfaelle
```

## Tests

```bash
python3 -m pytest tests/ -q
```
Abgedeckt: Divergenz-Cap, Kreuzungen/Clique-Regel, autonome Spur, Sandkasten-Whitelist,
Moderation (inkl. Fail-Closed), Welt-Memory (Capture/Moderation-Reject/Relevanz/
Summarization/Eltern-CLI).

## Lizenz

MIT — siehe [LICENSE](LICENSE). Basiert auf
[kiki123124/novel-rpg](https://github.com/kiki123124/novel-rpg) (ebenfalls MIT). Marken-/
IP-Rechte an „Harry Potter" verbleiben bei den Rechteinhabern (siehe Disclaimer).
