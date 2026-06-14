"""Kreuzungspunkte & Clique: 'Teil der Clique' nur über mehrere Kreuzungen."""
import game_engine
from conftest import new_save


def _load(save_id):
    return game_engine.load_save(save_id)


def test_einzelne_kreuzung_macht_noch_keine_clique():
    sid = new_save()
    game_engine.advance(sid, "y1_s02", 0, "andocken")  # bond +1
    save = _load(sid)
    assert save["clique_bond"] == 1
    assert save["in_clique"] is False


def test_clique_braucht_kreuzungen_UND_kernfreundschaften():
    # Kern-Freunde starten auf "Fremde" (trust 35) → Clique entsteht erst über einen
    # volleren Freundschafts-Pfad: alle 4 Kreuzungen andocken + beziehungsstarke Beats.
    sid = new_save()
    game_engine.advance(sid, "y1_s02", 0, "andocken")   # Harry/Ron 45
    game_engine.advance(sid, "y1_s06", 0, "andocken")   # Harry 55
    game_engine.advance(sid, "y1_s07", 0, "andocken")   # Harry 65, Ron 55, Hermine 55
    game_engine.advance(sid, "y1_s08", 0, "zusammen herausfinden")  # Harry+10, Hermine+5, Ron+5
    game_engine.advance(sid, "y1_s11", 0, "andocken")   # alle +10 → je >= 70
    save = _load(sid)
    assert all(save["relationships"][n]["status"] == "Freund" for n in game_engine.CORE_FRIENDS)
    assert len(save["crossings_used"]) >= game_engine.CLIQUE_CROSSINGS_MIN
    assert save["in_clique"] is True
    assert "Teil der Clique" in save["achievements"]


def test_kreuzungen_aber_nicht_alle_freunde_keine_clique():
    # Nur eine Kreuzung andocken: Kreuzungen evtl. ok, aber nicht alle Kern-Freunde
    sid = new_save()
    game_engine.advance(sid, "y1_s02", 0, "andocken")  # nur Harry/Ron auf 60 (Bekannt)
    save = _load(sid)
    assert save["in_clique"] is False


def test_kreuzung_zaehlt_nur_einmal():
    sid = new_save()
    game_engine.advance(sid, "y1_s02", 0, "andocken")
    game_engine.advance(sid, "y1_s02", 0, "andocken")  # gleiche Kreuzung erneut
    save = _load(sid)
    assert save["clique_bond"] == 1
    assert save["crossings_used"].count("y1_s02") == 1


def test_beziehungs_tiers_steigen():
    sid = new_save()
    game_engine.advance(sid, "y1_s02", 0, "andocken")  # Harry +10, Ron +10
    save = _load(sid)
    # Start trust 50; +10 → 60 = 'Bekannt'
    assert save["relationships"]["Harry"]["status"] == "Bekannt"
    # nicht angedockte Option ohne docks darf Bindung nicht erhöhen
    sid2 = new_save()
    game_engine.advance(sid2, "y1_s07", 1, "Lehrer holen")  # canon, docks False
    s2 = _load(sid2)
    assert s2["clique_bond"] == 0
