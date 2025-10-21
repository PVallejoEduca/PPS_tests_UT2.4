// ----------------------------------------------------------
// PRUEBAS UNITARIAS
// ----------------------------------------------------------
const { sumar, dividir } = require('../src/calculadora');

test('suma básica', () => {
  expect(sumar(2, 3)).toBe(5);
});

test('división correcta', () => {
  expect(dividir(10, 2)).toBe(5);
});

test('división por cero lanza error', () => {
  expect(() => dividir(5, 0)).toThrow("No se puede dividir entre cero");
});
