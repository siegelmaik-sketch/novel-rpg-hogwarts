"""Ebene-3-Schnittstelle (Welt-Memory): in V1 vorhanden, aber inert."""
import game_engine
import world_memory
from conftest import new_save


def test_neuer_save_hat_inerten_world_state():
    sid = new_save()
    save = game_engine.load_save(sid)
    ws = save.get("world_state")
    assert ws == {"version": 1, "facts": [], "summary": None}


def test_beat_scheduler_v1_linear():
    import beat_scheduler
    _, plot = game_engine.load_book_data("hogwarts")
    s07 = next(s for s in plot["scenes"] if s["id"] == "y1_s07")
    # V1: linearer Scheduler liefert immer die erste Folge-Szene (was auch immer
    # nach Story-Erweiterungen darauf folgt).
    assert beat_scheduler.next_beat(s07) == s07["next_scenes"][0]
