"""Pflicht-Umbau 2: Der Divergenz-Cap muss hart bei 30 deckeln und sperren."""
import game_engine
from conftest import new_save


def _load(save_id):
    return game_engine.load_save(save_id)


def test_cap_deckelt_bei_30():
    sid = new_save()
    # 6 Nicht-Kanon-Wahlen (Index 1 in y1_s01 ist nicht-kanon) → 6 * 5 = 30
    for _ in range(6):
        game_engine.advance(sid, "y1_s01", 1, "nicht-kanon")
    save = _load(sid)
    assert save["divergence_score"] == game_engine.DIVERGENCE_CAP == 30
    assert save["divergence_locked"] is True


def test_ueber_cap_keine_weitere_abweichung():
    sid = new_save()
    for _ in range(8):  # mehr als nötig
        game_engine.advance(sid, "y1_s01", 1, "nicht-kanon")
    save = _load(sid)
    # nie über 30, und die letzte Wahl wurde als gesperrt markiert
    assert save["divergence_score"] == 30
    assert save["choices_made"][-1]["divergence_rejected"] is True


def test_kanon_erhoeht_divergenz_nicht():
    sid = new_save()
    game_engine.advance(sid, "y1_s01", 0, "kanon")  # Index 0 ist canon
    save = _load(sid)
    assert save["divergence_score"] == 0
    assert save["divergence_locked"] is False
