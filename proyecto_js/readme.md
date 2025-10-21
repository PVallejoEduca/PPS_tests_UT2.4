# Instalar dependencias
npm install

# Ejecutar los tests
make test

# ============================================================
# Makefile para ejecutar las pruebas automáticas con Jest
# ============================================================
# Uso:
#   make test       → ejecuta los tests con salida detallada y cobertura
# ------------------------------------------------------------

# Objetivo principal: ejecutar tests definidos en *.test.js
test:
	# Ejecuta Jest a través de npx (sin instalación global)
	npx jest \
		--verbose \       # Muestra cada test con su nombre y resultado
		--coverage        # Genera informe de cobertura de código

# ------------------------------------------------------------
# Notas:
# - npx ejecuta Jest desde node_modules/.bin automáticamente.
# - La cobertura muestra qué porcentaje del código fue probado.
# - Es útil comparar este Makefile con el de Python:
#     ambos usan "make test" aunque debajo corren herramientas distintas.
# - Para ejecutar manualmente sin Makefile: npx jest --verbose --coverage
# ------------------------------------------------------------


# Salida esperada
 PASS  tests/calculadora.test.js
  ✓ suma correcta (3 ms)
  ✓ suma con negativos
  ✓ división correcta
  ✓ división por cero lanza error

----------------------|---------|----------|---------|---------|-------------------
File                  | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s 
----------------------|---------|----------|---------|---------|-------------------
All files             |     100 |      100 |     100 |     100 |                   
----------------------|---------|----------|---------|---------|-------------------

