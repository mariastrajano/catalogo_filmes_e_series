import pytest
from src.midia import Midia
from src.filme import Filme
from src.serie import Serie
from src.episodio import Episodio

'''
    MIDIA
'''

def test_criacao_midia():
    m = Midia("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth")
    assert m.titulo == "Jogos Vorazes"
    assert m.genero == "Ação"
    assert m.ano == 2012

def test_titulo_vazio():
    with pytest.raises(ValueError):
        Midia("", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth")

def test_midia_eq():
    m1 = Midia("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth")
    m2 = Midia("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth")
    assert m1 == m2

'''
    FILME
'''

def test_filme_criacao():
    f = Filme("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", 10)
    assert f.titulo == "Jogos Vorazes"
    assert f.nota == 10

def test_nota_invalida_filme():
    with pytest.raises(ValueError):
        Filme("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", -10)

'''
    SERIE
'''

def test_serie_criacao():
    s = Serie("Dark", "Série", "Mistério", 2017, 142, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", 3)
    assert s.temporadas == 3

def test_serie_temporadas_invalidas():
    with pytest.raises(ValueError):
        Serie("Dark", "Série", "Mistério", 2017, 142, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", 0)

'''
    EPISODIO
'''

def test_episodio_criacao():
    e = Episodio(1, "Piloto", 50, "ASSISTIDO", 10)
    assert e.titulo == "Piloto"
    assert e.duracao == 50
    assert e.nota == 10

def test_episodio_nota_invalida():
    with pytest.raises(ValueError):
        Episodio(1, "Piloto", 50, "ASSISTIDO", 0)
