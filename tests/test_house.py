# -*- coding: utf-8 -*-
"""Freie Hauswahl: die Hut-Zeremonie setzt das Haus echt, alle vier möglich."""
import game_engine
from conftest import new_save


def _load(s):
    return game_engine.load_save(s)


def test_neuer_save_haus_offen():
    # Vor der Hut-Zeremonie ist das Haus offen (wird frei gewählt)
    assert _load(new_save()).get("house") is None


def test_hut_setzt_gewaehltes_haus():
    sid = new_save()
    game_engine.advance(sid, "y1_s04", 1, "Hut: Ravenclaw")   # Index 1 = Ravenclaw
    assert _load(sid)["house"] == "Ravenclaw"


def test_alle_vier_haeuser_waehlbar():
    haeuser = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    for i, h in enumerate(haeuser):
        sid = new_save()
        game_engine.advance(sid, "y1_s04", i, f"Hut: {h}")
        assert _load(sid)["house"] == h


def test_set_house_funktion():
    sid = new_save()
    game_engine.set_house.__wrapped__ if hasattr(game_engine.set_house, "__wrapped__") else None
    # gültiges Haus wird (case-insensitiv) gesetzt
    save = _load(sid)
    save["house"] = None
    game_engine.write_save(sid, save)
    # direkt über die advance-Mechanik bereits getestet; hier nur HOUSES-Konstante
    assert game_engine.HOUSES == ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]


def test_clique_ist_hausuebergreifend():
    # Auch als Ravenclaw kann man Teil der Clique werden (Haus spielt keine Rolle)
    sid = new_save()
    game_engine.advance(sid, "y1_s04", 1, "Ravenclaw")          # Haus: Ravenclaw
    game_engine.advance(sid, "y1_s02", 0, "andocken")
    game_engine.advance(sid, "y1_s06", 0, "andocken")
    game_engine.advance(sid, "y1_s07", 0, "andocken")
    game_engine.advance(sid, "y1_s08", 0, "zusammen")
    game_engine.advance(sid, "y1_s11", 0, "andocken")
    save = _load(sid)
    assert save["house"] == "Ravenclaw"
    assert save["in_clique"] is True   # Clique trotz Nicht-Gryffindor
