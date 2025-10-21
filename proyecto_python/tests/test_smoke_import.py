# ----------------------------------------------------------
# PRUEBA DE HUMO: comprobar que el módulo se importa
# ----------------------------------------------------------
def test_importacion():
    # Intentamos importar el módulo principal
    import src.calculadora
    # Verificamos que la importación fue exitosa
    assert hasattr(src.calculadora, "sumar")
