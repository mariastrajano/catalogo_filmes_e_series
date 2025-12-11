import pytest
from models.midia import Midia

def test_criacao_midia():
    m = Midia("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "ASSISTIDO", 10, None)
    assert m.titulo == "Jogos Vorazes"
    assert m.duracao == 142

def test_titulo_vazio():
    with pytest.raises(ValueError):
        Midia("", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "ASSISTINDO", 10, None)

def test_duracao_invalida():
    with pytest.raises(ValueError):
        Midia("Dark", "Série", "Mistério", 2017, -19, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", "ASSISTIDO", 9.6, "2025-12-09")

def test_status_invalido():
    with pytest.raises(ValueError):
        Midia("Dark", "Série", "Mistério", 2017, 160, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", "JÁ ASSISTI", 9.6, "2025-12-09")

def test_nota_invalida():
    with pytest.raises(ValueError):
        Midia("Jogos Vorazes", "Filme", "Ação", 2012, 142, 14, "Jennifer Lawrence, Josh Hutcherson e Liam Hemsworth", "ASSISTINDO", -10, None)

def test_midia_eq():
    m1 = Midia("Dark", "Série", "Mistério", 2017, 160, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", "ASSISTIDO", 9.6, "2025-12-09")
    m2 = Midia("Dark", "Série", "Mistério", 2017, 160, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", "ASSISTIDO", 9.6, "2025-12-09")
    assert m1 == m2