# ----------------------------------------------------------
# PRUEBA DE INTEGRACIÓN: lectura de archivo + cálculo
# ----------------------------------------------------------
import tempfile
from src.calculadora import sumar

# Prueba de suma leyendo datos desde un archivo CSV
def test_suma_desde_csv(tmp_path):
    # Creamos un archivo temporal
    archivo = tmp_path / "datos.csv"
    archivo.write_text("2,3\n4,5\n")

    total = 0
    # Leemos el archivo y sumamos los valores
    for linea in archivo.read_text().splitlines():
        a, b = map(int, linea.split(","))
        total += sumar(a, b)

    # Verificamos el resultado
    assert total == 14  # 2+3 + 4+5
