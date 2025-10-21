// ----------------------------------------------------------
// PRUEBA E2E: ejecuta CLI completo
// ----------------------------------------------------------
const { execSync } = require('child_process');

test('CLI suma correctamente', () => {
  const output = execSync('node src/cli.js sumar 2 3').toString().trim();
  expect(output).toBe('5');
});
