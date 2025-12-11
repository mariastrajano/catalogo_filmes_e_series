import pytest
from models.temporada import Temporada

def test_temporada_numero_negativo():
    with pytest.raises(ValueError):
        Temporada(-1)