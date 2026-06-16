# -*- coding: utf-8 -*-
"""Onboarding: eigene Figur (Name/Geschlecht/Heimatort/Haustier) + set-profile."""
import os
import game_engine


def _load(s):
    return game_engine.load_save(s)


def _new_save_with(profile=None):
    """Legt ein Spiel mit (optionalem) Onboarding-Profil an und liefert die save_id."""
    before = set(os.listdir(game_engine.SAVES_DIR))
    game_engine.new_game("hogwarts", "player_heroine", profile)
    after = set(os.listdir(game_engine.SAVES_DIR))
    return (after - before).pop()[:-5]


# ── Default (ohne Flags) ──────────────────────────────────────────────────────
def test_default_profil_robin_weiblich_flocke():
    prot = _load(_new_save_with())["protagonist"]
    assert prot["name"] == "Robin"
    assert prot["gender"] == "weiblich"
    assert prot["pronouns"]["subjekt"] == "sie"
    assert prot["pronouns"]["possessiv"] == "ihre"
    assert prot["hometown"] == "ein kleines Dorf"
    assert prot["pet"] == {"name": "Flocke", "kind": "Malteser-Hündchen"}


def test_default_name_und_companion_synchron():
    save = _load(_new_save_with())
    assert save["character_name"] == "Robin"
    assert save["companion"] == "Flocke"


# ── Voll personalisiert ───────────────────────────────────────────────────────
def test_voll_personalisiert():
    sid = _new_save_with({
        "name": "Mika", "gender": "männlich", "hometown": "Bremen",
        "pet_name": "Schnuffel", "pet_kind": "Kaninchen",
    })
    save = _load(sid)
    prot = save["protagonist"]
    assert prot["name"] == "Mika"
    assert prot["gender"] == "männlich"
    assert prot["pronouns"]["subjekt"] == "er"
    assert prot["pronouns"]["possessiv"] == "sein"
    assert prot["hometown"] == "Bremen"
    assert prot["pet"] == {"name": "Schnuffel", "kind": "Kaninchen"}
    # Name + Begleiter werden mitgeführt
    assert save["character_name"] == "Mika"
    assert save["companion"] == "Schnuffel"


def test_haustier_umbenannt_verschiebt_beziehung():
    sid = _new_save_with({"pet_name": "Schnuffel", "pet_kind": "Kaninchen"})
    rels = _load(sid)["relationships"]
    assert "Schnuffel" in rels          # neue Begleiter-Beziehung da
    assert "Flocke" not in rels         # alte Vorgabe verschwunden
    assert "Kaninchen" in rels["Schnuffel"]["note"]   # Notiz spiegelt die Art


def test_default_haustier_behaelt_originalbeziehung():
    # Ohne Umbenennung bleibt die Flocke-Beziehung samt Start-Vertrauen erhalten
    rels = _load(_new_save_with())["relationships"]
    assert "Flocke" in rels
    assert rels["Flocke"]["trust"] == 95


# ── Neutrales Geschlecht ──────────────────────────────────────────────────────
def test_divers_hat_keine_gegenderten_pronomen():
    prot = _load(_new_save_with({"gender": "neutral"}))["protagonist"]
    assert prot["gender"] == "divers"
    assert prot["pronouns"]["subjekt"] == ""
    assert prot["pronouns"]["possessiv"] == ""
    assert prot["pronouns"]["anrede"] == "Kind"


# ── Geschlechts-Normalisierung ────────────────────────────────────────────────
def test_normalize_gender_varianten():
    n = game_engine._normalize_gender
    for v in ("m", "männlich", "Junge", "male", "j"):
        assert n(v) == "männlich"
    for v in ("w", "weiblich", "Mädchen", "female", "f"):
        assert n(v) == "weiblich"
    for v in ("d", "divers", "neutral", "keine", "nonbinary"):
        assert n(v) == "divers"
    # Unbekanntes / leeres fällt auf die Vorgabe (weiblich)
    assert n("xyz") == "weiblich"
    assert n("") == "weiblich"
    assert n(None) == "weiblich"


# ── Flag-Parsing ──────────────────────────────────────────────────────────────
def test_parse_profile_flags():
    p = game_engine._parse_profile_flags(
        ["--name", "Lena", "--gender", "w", "--home", "Köln",
         "--pet-name", "Minka", "--pet-kind", "Katze"]
    )
    assert p == {
        "name": "Lena", "gender": "w", "hometown": "Köln",
        "pet_name": "Minka", "pet_kind": "Katze",
    }


def test_parse_profile_flags_leer_und_unbekannt():
    assert game_engine._parse_profile_flags([]) == {}
    # unbekannte Flags / Flag ohne Wert werden ignoriert (kein Crash)
    assert game_engine._parse_profile_flags(["--foo", "bar", "--name"]) == {}


# ── set-profile (nachträglich ändern) ─────────────────────────────────────────
def test_set_profile_aendert_nur_gesetzte_felder():
    sid = _new_save_with({"name": "Mika", "gender": "männlich", "hometown": "Bremen"})
    game_engine.set_profile(sid, {"name": "Robin"})
    prot = _load(sid)["protagonist"]
    assert prot["name"] == "Robin"
    assert prot["gender"] == "männlich"   # unverändert
    assert prot["hometown"] == "Bremen"   # unverändert
    assert _load(sid)["character_name"] == "Robin"


def test_set_profile_pet_umbenennen_verschiebt_beziehung():
    sid = _new_save_with()                 # startet mit Flocke
    game_engine.set_profile(sid, {"pet_name": "Flummi", "pet_kind": "Eule"})
    save = _load(sid)
    assert save["companion"] == "Flummi"
    assert save["protagonist"]["pet"] == {"name": "Flummi", "kind": "Eule"}
    assert "Flummi" in save["relationships"]
    assert "Flocke" not in save["relationships"]
    assert "Eule" in save["relationships"]["Flummi"]["note"]


def test_set_profile_gender_aktualisiert_pronomen():
    sid = _new_save_with()                 # weiblich → sie/ihre
    game_engine.set_profile(sid, {"gender": "männlich"})
    prot = _load(sid)["protagonist"]
    assert prot["gender"] == "männlich"
    assert prot["pronouns"]["subjekt"] == "er"
