import pytest
from models.filme import Filme

def test_filme_criacao():
    f = Filme("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "ASSISTINDO", 10, "2025-09-21")
    assert f.titulo == "Jogos Vorazes"
    assert f.nota == 10