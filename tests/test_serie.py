import pytest
from models.serie import Serie

def test_serie_criacao():
    s = Serie("Dark", "Série", "Mistério", 2017, 160, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", "Assistido", 9.6, "2025-12-09")
    assert s.titulo == "Dark"
    assert s.nota == 9.6