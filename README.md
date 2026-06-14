# Hogwarts RPG — kindgerechtes Novel-RPG-Skill

*A child-safe, story-driven Hogwarts adventure as a skill for OpenClaw / Claude Code.
German content. Built on the [`novel-rpg`](https://github.com/kiki123124/novel-rpg) engine.*

Eine **kindgerechte, story-getriebene Hogwarts-Variante** der Novel-RPG-Engine. Die
Spielerin/der Spieler spielt eine **eigene Figur** (Vorgabe „Robin", frei umbenennbar)
im selben Jahrgang wie die berühmten Schülerinnen und Schüler, begegnet ihnen und kann
über viele Begegnungen Teil ihrer Clique werden. Der kanonische Plot ist der rote Faden;
**Freiheit lebt in den Lücken** zwischen den Kanon-Beats.

> **Hinweis / Disclaimer:** Nicht-kommerzielles **Fan-Projekt** zu privaten und
> Bildungszwecken. „Harry Potter" und die Hogwarts-Welt sind © J. K. Rowling / Warner
> Bros.; dieses Projekt steht in keiner Verbindung zu den Rechteinhabern. Es wird **kein
> Buchtext** verwendet — nur handkuratierte Metadaten + Modellwissen (genau wie die
> Built-in-Bücher der Vorlage). Charaktere/Setting dienen nur als Spielrahmen.

Basiert auf **[kiki123124/novel-rpg](https://github.com/kiki123124/novel-rpg)** (MIT) und
fügt eine durchgängige **Kindersicherheits-Architektur** hinzu — die eigentliche
wiederverwendbare Zutat dieses Forks.

---

## Was dieser Fork beiträgt (wiederverwendbar)

| Baustein | Datei | Zweck |
|---|---|---|
| **Output-Moderation** | `skill/scripts/moderation.py` | Jede Szene/jeder Fakt wird geprüft, **bevor** er angezeigt/gespeichert wird. Fail-Closed, Incident-Log. Modi: OpenClaw-Inferenz (same-auth), OpenAI-`/moderations`, oder Offline-Wortliste. |
| **Divergenz-Cap** | `skill/scripts/game_engine.py` | Harte Obergrenze, ab der keine Nicht-Kanon-Pfade mehr möglich sind — die Geschichte bleibt auf Schienen. |
| **Sandkasten + Orts-Whitelist** | `game_engine.py` / `locations.json` | Freie Bewegung zwischen Beats, aber **nur** auf erlaubte Schauplätze (Leitplanke ist die Welt, nicht nur der Prompt). Divergenz-neutral. |
| **Kreuzungspunkte + autonome Kanon-Spur** | `plot_graph.json` | Andocken an Kanon-Beats oder nacherzählt erleben — beide Pfade führen zum selben nächsten Beat. „Teil der Clique" = mehrere Kreuzungen **und** Kern-Freundschaften. |
| **Persistentes Welt-Memory** | `skill/scripts/world_memory.py` | Merkt selbst erschaffene Sandkasten-Inhalte über Sessions — **mit Moderation beim Schreiben**, Relevanz-Injektion, Summarization (Token-Budget) und **Eltern-Fenster** (`list`/`remove`/`clear`). |
| **Kindgerechte GM-Härtung** | `skill/SKILL.md` | Ton fest verdrahtet (Kinderbuch-Niveau, keine Romantik/Gewalt/Isolation), **nicht durch Spielereingaben überschreibbar**. |

**Umfang des Beispiel-Buches:** ein ausführliches Schuljahr-Setting über **2 Jahre**,
**265 Szenen** und **118 Kreuzungen** (Unterricht, Mahlzeiten, Gemeinschaftsraum,
Bibliothek, Ländereien, Eulerei, Nebenfiguren-Stränge). Inhalt ist handkuratiert/
generiert (`build_year.py`, `build_year2.py`) — reproduzierbar und erweiterbar.

## Architektur (Layer)

```
 Spieler:in
   |  ^  jede Ausgabe durch die Moderation
   v  |
 Interface (z. B. OpenClaw-Channel / Terminal)
   |
 GM / Agent  — laedt das Skill, erzaehlt
   | ruft Skripte
   v
 Moderation . Engine (State/Divergenz/Kreuzungen) . Welt-Memory . Content (JSON)
```

## Setup

```bash
pip install -r requirements.txt

# Als OpenClaw-Skill installieren:
openclaw skills install ./skill --as hogwarts-rpg
python3 skill/scripts/book_manager.py init-builtins   # Buchdaten initialisieren

# Moderation konfigurieren (Pflicht fuer den Kinder-Einsatz), z. B.:
#   MODERATION_MODE=openclaw   (Klassifizierung ueber dasselbe Modell-Auth, kein Extra-Key)
#   MODERATION_MODE=openai + OPENAI_MOD_KEY=...   (OpenAI /moderations)
#   MODERATION_MODE=local      (nur Offline-Wortliste, fuer Tests)
```

Spielstaende/Welt-Memory/Incident-Log liegen **ausserhalb** des Skills unter
`~/.openclaw/hogwarts-state/` (ueberschreibbar via `HOGWARTS_STATE_DIR`) und ueberleben
Skill-Reinstalls.

## Werkzeuge fuer Eltern / Betreiber

```bash
# Was hat sich das Spiel "gemerkt"? — ansehen/beschneiden:
python3 skill/scripts/world_memory.py list   <save-id>
python3 skill/scripts/world_memory.py remove <save-id> <fact-id>
python3 skill/scripts/world_memory.py clear  <save-id>

# Moderations-Vorfaelle:
cat ~/.openclaw/hogwarts-state/moderation_log/*.jsonl
```

## Tests

```bash
python3 -m pytest tests/ -q
```
Abgedeckt: Divergenz-Cap, Kreuzungen/Clique-Regel, autonome Spur, Sandkasten-Whitelist,
Moderation (inkl. Fail-Closed), Welt-Memory (Capture/Moderation-Reject/Relevanz/
Summarization/Eltern-CLI).

## Lizenz

MIT — siehe [LICENSE](LICENSE). Basiert auf [kiki123124/novel-rpg](https://github.com/kiki123124/novel-rpg)
(ebenfalls MIT). Eigenstaendige Hogwarts-Inhalte und die Sicherheits-Architektur stehen
ebenfalls unter MIT. Markenrechte/IP von „Harry Potter" verbleiben bei den Rechteinhabern
(siehe Disclaimer oben).
