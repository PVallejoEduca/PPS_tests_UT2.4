# ----------------------------------------------------------
# PRUEBAS UNITARIAS: funciones individuales
# ----------------------------------------------------------
from src.calculadora import sumar, dividir
import pytest

# Prueba de suma básica
def test_sumar_basico():
    assert sumar(2, 3) == 5

# Prueba de división básica
def test_dividir_correcto():
    assert dividir(10, 2) == 5

# Prueba de división por cero
def test_dividir_por_cero():
    # Verificamos que se lanza una excepción al dividir por cero
    with pytest.raises(ValueError):
        dividir(5, 0)
