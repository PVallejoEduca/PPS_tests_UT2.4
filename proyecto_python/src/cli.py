# ----------------------------------------------------------
# Interfaz de línea de comandos (nivel sistema/E2E)
# ----------------------------------------------------------
import sys
from src.calculadora import sumar, dividir

# Función principal de la CLI
def main():

    if len(sys.argv) != 4:
        print("Uso: python -m src.cli <operacion> <a> <b>")
        sys.exit(1)

    op, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])

    # Realizamos la operación solicitada
    if op == "sumar":
        print(sumar(a, b))
    elif op == "dividir":
        print(dividir(a, b))
    else:
        print("Operación no válida")
        sys.exit(2)

# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()
