"""Pflicht-Umbau 1: Moderationsschicht — harmlos durch, problematisch geflaggt."""
import moderation


def test_harmloser_text_geht_durch():
    v = moderation.moderate("Du läufst über den sonnigen Hof. Hagrid winkt dir freundlich zu.")
    assert v["flagged"] is False


def test_problematischer_text_wird_geflaggt():
    v = moderation.moderate("Plötzlich foltern sie das Tier und Blut spritzt überall.")
    assert v["flagged"] is True
    assert v["hits"]  # lokale Wortliste hat angeschlagen


def test_fail_closed_bei_api_fehler(monkeypatch):
    # OpenAI-Modus erzwingen, aber Key entfernen und API-Aufruf scheitern lassen.
    monkeypatch.setattr(moderation, "MODE", "openai")
    monkeypatch.setattr(moderation, "FAIL_CLOSED", True)
    monkeypatch.setattr(moderation, "openai_check",
                        lambda text: (None, {}, "simulierter Netzfehler"))
    v = moderation.moderate("Ein völlig harmloser Satz über Zaubertränke.")
    assert v["flagged"] is True
    assert "fail-closed" in v["reason"]


def test_incident_log_wird_geschrieben(tmp_path, monkeypatch):
    monkeypatch.setattr(moderation, "LOG_DIR", str(tmp_path))
    v = moderation.moderate("foltern und Blut spritzt")
    assert v["flagged"]
    path = moderation.log_incident("foltern und Blut spritzt", v, context={"source": "test"})
    assert path
    import os
    assert os.path.exists(path)
