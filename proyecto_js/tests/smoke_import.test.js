// ----------------------------------------------------------
// PRUEBA DE HUMO: comprobar que el módulo se carga
// ----------------------------------------------------------
test('el módulo calculadora se importa', () => {
  const calc = require('../src/calculadora');
  expect(calc.sumar).toBeDefined();
});
