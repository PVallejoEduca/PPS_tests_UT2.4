# ----------------------------------------------------------
# PRUEBA E2E: ejecuta la aplicación completa (CLI)
# ----------------------------------------------------------
import subprocess

# Prueba de suma a través de la CLI
def test_cli_suma():
    # Ejecutamos el comando de suma
    result = subprocess.run(
        ["python", "-m", "src.cli", "sumar", "2", "3"],
        capture_output=True,
        text=True
    )

    # Verificamos la salida
    assert result.stdout.strip() == "5.0"
    assert result.returncode == 0
