# Instalar dependencias
python -m venv venv
source venv/bin/activate      # (en Windows: venv\Scripts\activate)
pip install -r requirements.txt

# Ejecutar los tests
make test

# ============================================================
# Makefile para ejecutar las pruebas automáticas con pytest
# ============================================================
# Uso:
#   make test       → ejecuta los tests con salida detallada y cobertura
# ------------------------------------------------------------

# Objetivo principal: ejecutar pruebas unitarias e integración
test:
	# Ejecuta pytest (busca automáticamente archivos test_*.py)
	pytest \
		-v \                           # Modo verbose: muestra cada test con detalle
		--maxfail=1 \                  # Detiene la ejecución tras el primer fallo
		--disable-warnings \           # Oculta advertencias que no sean errores
		--cov=src \                    # Mide la cobertura del código en carpeta src/
		--cov-report=term-missing      # Muestra qué líneas no fueron ejecutadas

# ------------------------------------------------------------
# Notas:
# - Este comando permite ver qué parte del código está probada.
# - La opción --maxfail=1 ayuda a centrarse en el primer error.
# - La cobertura ideal mínima en PPS será del 60%.
# - Para ejecutar manualmente sin Makefile: pytest -v --cov=src
# ------------------------------------------------------------


# Salida esperada
tests/test_calculadora.py::test_sumar_basico PASSED
tests/test_calculadora.py::test_sumar_negativos PASSED
tests/test_calculadora.py::test_dividir_basico PASSED
tests/test_calculadora.py::test_dividir_por_cero PASSED

# Cobretura
Name                     Stmts   Miss  Cover
--------------------------------------------
src/calculadora.py           7      0   100%
