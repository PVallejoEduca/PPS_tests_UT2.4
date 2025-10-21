# Cada proyecto tiene su propio readme.md para ejecutarlo.
##  Tipos de Pruebas en el Proyecto

| Nivel | Archivo Python | Archivo JavaScript | Qué comprueba | Cuándo se ejecuta | Objetivo educativo |
|:------|:----------------|:-------------------|:---------------|:------------------|:-------------------|
| **1 Unitarias** | `tests/test_unit_calculadora.py` | `tests/unit_calculadora.test.js` | Cada función o módulo de forma **aislada**, sin dependencias externas. | Durante el desarrollo (cada cambio de código). | Entender cómo probar **lógica pura** y detectar errores locales. |
| **2 Integración** | `tests/test_integration_csv.py` | `tests/integration_csv.test.js` | Varias partes del sistema juntas (por ejemplo, **lectura de archivo + cálculo**). | Antes del despliegue o integración con otros módulos. | Aprender a validar la **colaboración entre componentes**. |
| **3 E2E / Sistema** | `tests/test_e2e_cli.py` | `tests/e2e_cli.test.js` | La aplicación completa ejecutada como un **usuario real** (CLI o API). | En entorno de pruebas o staging. | Comprobar que todo el flujo del programa **funciona de principio a fin**. |
| **4 Humo (Smoke Test)** | `tests/test_smoke_import.py` | `tests/smoke_import.test.js` | Que la app o módulo **arranca sin romperse** y se puede importar/ejecutar. | Después de un despliegue o instalación. | Asegurar que el sistema **enciende correctamente** antes de más pruebas. |
| **5 Regresión** | *(implícita, al volver a ejecutar toda la suite)* | *(implícita, igual)* | Que los cambios nuevos **no rompan funcionalidades previas**. | En cada commit o pipeline de CI/CD. | Comprender la importancia de **repetir las pruebas tras cambios**. |

---

### Resumen visual – Pirámide de Testing

    ┌───────────────────────────────┐
    │   3 - E2E / Sistema / UI      │  ← lentas, pocas
    ├───────────────────────────────┤
    │   2 - Integración             │
    ├───────────────────────────────┤
    │   1 - Unitarias               │  ← rápidas, muchas
    └───────────────────────────────┘


> Cuanto más abajo, más rápidas y numerosas son las pruebas.  
> Cuanto más arriba, más realistas pero lentas y costosas.  
> En un despliegue seguro, todas son necesarias en su nivel.

---

###  Notas

- Cada proyecto incluye los **cuatro niveles reales de pruebas** explicados en la UT 2.  
- Todos se ejecutan con el mismo comando:  
  - En Python → `make test` (usa `pytest`).  
  - En JavaScript → `make test` (usa `Jest`).  
- La cobertura mínima recomendada en PPS es del **60 %**.  
- Repite las pruebas después de cada cambio: eso es una **prueba de regresión**.
