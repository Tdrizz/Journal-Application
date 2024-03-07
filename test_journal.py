from journal import get_material, get_feeling, get_programs
import pytest 

def test_get_material_nil(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "")
    with pytest.raises(ValueError):
        get_material()

def test_get_material_fine(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "testing")
    assert get_material() == "testing"

def test_get_feeling_nil(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "")
    with pytest.raises(ValueError):
        get_feeling()

def test_get_feeling_fine(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "testing")
    assert get_feeling() == "testing"

def test_get_programs_nil(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "")
    with pytest.raises(ValueError):
        get_programs()

def test_get_programs_negative(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "-1")
    with pytest.raises(ValueError):
        get_programs()
    
def test_get_programs_word(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "testing")
    with pytest.raises(ValueError):
        get_programs()

def test_get_programs_fine(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "5")
    assert get_programs() == 5