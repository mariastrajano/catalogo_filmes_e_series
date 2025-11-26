import pytest
from src.filme import Filme

'''
    SEMANA 2
'''

def test_filme_criacao():
    f = Filme("Jogos Vorazes", "Filme", "Ação", 2012, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "ASSISTINDO", 142, 10)
    assert f.titulo == "Jogos Vorazes"
    assert f.nota == 10

def test_filme_nota_invalida():
    with pytest.raises(ValueError):
        Filme("Jogos Vorazes", "Filme", "Ação", 2012, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "ASSISTINDO", 142, -10)

def test_filme_duracao_invalida():
    with pytest.raises(ValueError):
        Filme("Jogos Vorazes", "Filme", "Ação", 2012, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth","NÃO ASSISTIDO", -19, 10)