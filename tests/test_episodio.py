import pytest
from models.episodio import Episodio

def test_episodio_criacao():
    e = Episodio(1, "Piloto", 50, "Assistido", 10)
    assert e.titulo == "Piloto"
    assert e.duracao == 50
    assert e.nota == 10

def test_episodio_numero_negativo():
    with pytest.raises(ValueError):
        Episodio(-1, "Piloto", 50, "Assistido", 10)

def test_episodio_nota_invalida():
    with pytest.raises(ValueError):
        Episodio(1, "Piloto", 50, "Assistido", 100)

def test_episodio_duracao_invalida():
    with pytest.raises(ValueError):
        Episodio(1, "Piloto", -50, "Assistido", 10)