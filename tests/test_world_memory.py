# -*- coding: utf-8 -*-
"""Ebene-3 Welt-Memory (AKTIV): Capture+Moderation, Persistenz, Relevanz,
Summarization, Eltern-CLI."""
import game_engine
import world_memory
from conftest import new_save


def _load(sid):
    return game_engine.load_save(sid)


def test_add_fact_clean_wird_gespeichert():
    sid = new_save()
    f = world_memory.add_fact(sid, "npc", "Tom, ein freundlicher Hufflepuff aus dem Jahrgang")
    assert f is not None
    save = _load(sid)
    texts = [x["text"] for x in save["world_state"]["facts"]]
    assert any("Tom" in t for t in texts)
    assert f["typ"] == "npc" and f["created_segment"] == save.get("segment", 0)


def test_add_fact_geflaggt_wird_NICHT_gespeichert(tmp_path, monkeypatch):
    # Incident-Log in temp umleiten, damit der Test sauber bleibt
    monkeypatch.setattr(world_memory.moderation, "LOG_DIR", str(tmp_path))
    sid = new_save()
    res = world_memory.add_fact(sid, "ereignis", "jemand wird gefoltert und Blut spritzt")
    assert res is None                      # Fail-Closed: nicht gespeichert
    save = _load(sid)
    assert save["world_state"]["facts"] == []


def test_persistenz_ueber_reload():
    sid = new_save()
    world_memory.add_fact(sid, "ort", "Mein Geheimplatz hinter dem Wandteppich")
    # frisch von der Platte laden
    save = game_engine.load_save(sid)
    assert any("Geheimplatz" in x["text"] for x in save["world_state"]["facts"])


def test_get_context_nur_relevante_fakten():
    save = {"segment": 10, "world_state": {"version": 1, "summary": None, "facts": [
        {"id": "f001", "typ": "ort", "text": "Mein Lieblingsplatz in der Bibliothek",
         "created_segment": 1, "last_seen_segment": 1},
        {"id": "f002", "typ": "npc", "text": "Tom, mein Hufflepuff-Freund",
         "created_segment": 1, "last_seen_segment": 1},
        {"id": "f003", "typ": "ereignis", "text": "Ein Picknick am See im Sommer",
         "created_segment": 1, "last_seen_segment": 1},
    ]}}
    ctx = world_memory.get_context(save, ort="Bibliothek", segment=10, anwesende=["Tom"])
    ids = {f["id"] for f in ctx["aktive_fakten"]}
    assert "f001" in ids        # Ort-Treffer
    assert "f002" in ids        # anwesende Figur im Text
    assert "f003" not in ids    # weder Ort noch anwesend noch jüngstes Segment


def test_recency_macht_fakt_aktiv():
    save = {"segment": 1, "world_state": {"version": 1, "summary": None, "facts": [
        {"id": "f001", "typ": "ereignis", "text": "Irgendwas Belangloses",
         "created_segment": 1, "last_seen_segment": 1},
    ]}}
    ctx = world_memory.get_context(save, ort="Ganz woanders", segment=1, anwesende=[])
    assert {f["id"] for f in ctx["aktive_fakten"]} == {"f001"}   # jüngstes Segment


def test_summarize_komprimiert_und_haelt_aktive():
    sid = new_save()
    for i in range(15):
        world_memory.add_fact(sid, "ereignis", f"Sandkasten-Erlebnis Nummer {i}")
    save = _load(sid)
    ws = save["world_state"]
    assert len(ws["facts"]) <= world_memory.SUMMARIZE_THRESHOLD   # Älteres gefaltet
    assert ws["summary"]                                          # summary gefüllt
    # die jüngsten Erlebnisse sind noch verbatim da
    texts = " ".join(x["text"] for x in ws["facts"])
    assert "Nummer 14" in texts


def test_eltern_cli_remove_und_clear():
    sid = new_save()
    f1 = world_memory.add_fact(sid, "npc", "Figur A")
    world_memory.add_fact(sid, "ort", "Ort B")
    world_memory.remove_fact(sid, f1["id"])
    save = _load(sid)
    assert all(x["id"] != f1["id"] for x in save["world_state"]["facts"])
    world_memory.clear_facts(sid)
    assert _load(sid)["world_state"]["facts"] == []
