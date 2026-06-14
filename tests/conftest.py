"""Test-Setup: isoliertes Datenverzeichnis, Skill-Skripte importierbar machen."""
import os
import sys
import shutil
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = pathlib.Path("/tmp/hog_pytest_data")

# Umgebung VOR dem Import der Skill-Module setzen (DATA_DIR wird beim Import gelesen)
os.environ["HOGWARTS_DATA_DIR"] = str(DATA)
os.environ.setdefault("MODERATION_MODE", "local")

sys.path.insert(0, str(ROOT / "skill" / "scripts"))

# Frisches Datenverzeichnis mit den handkuratierten Buchdaten aufbauen
if DATA.exists():
    shutil.rmtree(DATA)
(DATA / "books" / "hogwarts").mkdir(parents=True)
(DATA / "saves").mkdir()
_src = ROOT / "skill" / "data" / "books" / "hogwarts"
for _f in ["meta.json", "characters.json", "plot_graph.json", "locations.json"]:
    shutil.copy(_src / _f, DATA / "books" / "hogwarts" / _f)


def new_save():
    """Legt ein neues Spiel an und liefert dessen save_id zurück."""
    import game_engine
    before = set(os.listdir(game_engine.SAVES_DIR))
    game_engine.new_game("hogwarts", "player_heroine")
    after = set(os.listdir(game_engine.SAVES_DIR))
    new = (after - before).pop()
    return new[:-5]  # ".json" abschneiden
