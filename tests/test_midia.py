import pytest
from src.midia import Midia

'''
    SEMANA 2
'''

def test_criacao_midia():
    m = Midia("Jogos Vorazes", "Filme", "Ação", 2012, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "NÃO ASSISTIDO")
    assert m.titulo == "Jogos Vorazes"
    assert m.genero == "Ação"
    assert m.ano == 2012

def test_titulo_vazio():
    with pytest.raises(ValueError):
        Midia("", "Filme", "Ação", 2012, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth","NÃO ASSISTIDO")

def test_midia_eq():
    m1 = Midia("Jogos Vorazes", "Filme", "Ação", 2012, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "NÃO ASSISTIDO")
    m2 = Midia("Jogos Vorazes", "Filme", "Ação", 2012, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "NÃO ASSISTIDO")
    assert m1 == m2