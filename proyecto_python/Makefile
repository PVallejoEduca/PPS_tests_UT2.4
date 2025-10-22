# ============================================================
# Makefile - Proyecto Python (UT2)
# Compatible con Windows, Linux y Docker
# ============================================================

# Variable de intérprete (puede cambiarse si el entorno usa 'python3')
PYTHON := python

# ------------------------------------------------------------
# Comando principal: ejecuta todos los tests con pytest
# ------------------------------------------------------------
test:
	$(PYTHON) -m pytest -v --disable-warnings --cov=src --cov-report=term-missing

# ------------------------------------------------------------
# Notas:
# - Usa 'python -m pytest' para que funcione incluso si el PATH del entorno virtual
#   no está activo (Windows suele dar ese problema con 'pytest' a secas).
# - Si aparece el error "make no se reconoce", ejecuta directamente el comando:
#     python -m pytest -v --disable-warnings --cov=src --cov-report=term-missing
# - Cobertura mínima recomendada: 60 %
# ------------------------------------------------------------

