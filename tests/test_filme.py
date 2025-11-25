import pytest
from src.filme import Filme

'''
    SEMANA 2
'''

def test_filme_criacao():
    f = Filme("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "ASSISTINDO", 10)
    assert f.titulo == "Jogos Vorazes"
    assert f.nota == 10

def test_nota_invalida_filme():
    with pytest.raises(ValueError):
        Filme("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "ASSISTINDO", -10)