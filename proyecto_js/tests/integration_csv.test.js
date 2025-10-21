// ----------------------------------------------------------
// PRUEBA DE INTEGRACIÓN: lectura de archivo + cálculo
// ----------------------------------------------------------
const fs = require('fs');
const { sumar } = require('../src/calculadora');

test('suma desde archivo CSV', () => {
  const tmp = './datos.csv';
  fs.writeFileSync(tmp, '2,3\n4,5\n');
  const lines = fs.readFileSync(tmp, 'utf8').trim().split('\n');

  const total = lines.reduce((acc, line) => {
    const [a, b] = line.split(',').map(Number);
    return acc + sumar(a, b);
  }, 0);

  expect(total).toBe(14);
  fs.unlinkSync(tmp);
});
