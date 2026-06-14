"""Sandkasten-Bewegung: Whitelist greift (Leitplanke ist die Welt) und
sandbox-context liefert den inerten Ebene-3-Seam."""
import os
import sys
import json
import subprocess
import pathlib

import game_engine
from conftest import new_save, DATA

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skill" / "scripts"
ENV = {**os.environ, "HOGWARTS_DATA_DIR": str(DATA), "MODERATION_MODE": "local"}


def _run(script, *args):
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args],
        capture_output=True, text=True, env=ENV,
    )


def test_move_auf_whitelist_ort_ok():
    sid = new_save()
    r = _run("game_engine.py", "move", sid, "bibliothek")
    assert r.returncode == 0, r.stdout + r.stderr
    save = game_engine.load_save(sid)
    assert save["current_location"] == "Bibliothek"


def test_move_ausserhalb_whitelist_abgelehnt():
    sid = new_save()
    r = _run("game_engine.py", "move", sid, "mordor")
    assert r.returncode == 2          # hart abgelehnt
    assert "abgelehnt" in r.stdout.lower()
    save = game_engine.load_save(sid)
    assert save["current_location"] is None  # unverändert


def test_sandbox_context_leitplanke_und_seam():
    sid = new_save()
    r = _run("scene_retriever.py", "sandbox-context", "hogwarts", "see", sid)
    # 'see' ist kein gültiger id/name → location_invalid, aber Struktur muss stehen
    data = json.loads(r.stdout)
    assert data["mode"] == "sandbox"
    assert "guardrails" in data and any("THEMA" in g for g in data["guardrails"])
    # Ebene-3-Seam ist AKTIV: Struktur vorhanden, bei leerem Memory ohne Fakten
    assert data["welt_memory"]["summary"] is None
    assert data["welt_memory"]["aktive_fakten"] == []


def test_sandbox_context_gueltiger_ort():
    sid = new_save()
    r = _run("scene_retriever.py", "sandbox-context", "hogwarts", "bibliothek", sid)
    data = json.loads(r.stdout)
    assert data["location_invalid"] is False
    assert data["location"]["name"] == "Bibliothek"
