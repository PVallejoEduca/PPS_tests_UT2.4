# ----------------------------------------------------------
# Funciones básicas de cálculo (nivel unitario)
# ----------------------------------------------------------
def sumar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
