"""Autonome Kanon-Spur: Nicht-Andocken verpasst die Kreuzung, der Beat passiert
trotzdem, und BEIDE Pfade führen zum selben nächsten Beat."""
import game_engine
from conftest import new_save


def _load(s):
    return game_engine.load_save(s)


def test_nicht_andocken_vermerkt_verpasste_kreuzung_und_beat_passiert():
    sid = new_save()
    # y1_s07 (Troll) ist Kreuzung; Index 1 = canon "Lehrer holen", docks NICHT
    game_engine.advance(sid, "y1_s07", 1, "Lehrer holen")
    save = _load(sid)
    assert "y1_s07" in save["crossings_missed"]
    assert "y1_s07" not in save["crossings_used"]
    assert "y1_s07" in save["beats_completed"]   # Beat gilt als passiert
    assert save["in_clique"] is False


def test_beide_pfade_fuehren_zum_selben_naechsten_beat():
    # Invariante: Andocken UND autonome Spur führen zum SELBEN nächsten Beat —
    # egal, welcher das nach späteren Story-Erweiterungen konkret ist.
    a = new_save()
    b = new_save()
    game_engine.advance(a, "y1_s07", 0, "andocken")     # Kreuzung genutzt
    game_engine.advance(b, "y1_s07", 1, "Lehrer holen")  # autonome Spur
    sa, sb = _load(a), _load(b)
    assert sa["current_scene"] == sb["current_scene"]
    assert sa["current_scene"] not in ("y1_s07", "END")


def test_recap_text_existiert_fuer_jede_kreuzung():
    # Jede Kreuzung muss einen autonomous_recap haben (für die Nicht-Andock-Erzählung)
    _, plot = game_engine.load_book_data("hogwarts")
    crossings = [s for s in plot["scenes"] if s.get("crossing_point")]
    assert crossings, "keine Kreuzungspunkte gefunden"
    for s in crossings:
        assert s.get("autonomous_recap"), f"{s['id']} ohne autonomous_recap"
