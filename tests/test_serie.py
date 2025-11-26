import pytest
from src.serie import Serie

'''
    SEMANA 2
'''

def test_serie_criacao():
    s = Serie("Dark", "Série", "Mistério", 2017, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", "ASSISTIDO", 3)
    assert s.temporadas == 3

def test_serie_temporadas_invalidas():
    with pytest.raises(ValueError):
        Serie("Dark", "Série", "Mistério", 2017, 18, "Louis Hofmann, Oliver Masucci e Jördis Triebel", "ASSISTIDO", 0)