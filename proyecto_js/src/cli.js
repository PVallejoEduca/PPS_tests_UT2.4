// ----------------------------------------------------------
// Interfaz de línea de comandos (nivel sistema/E2E)
// ----------------------------------------------------------
const { sumar, dividir } = require('./calculadora');

const args = process.argv.slice(2);
if (args.length !== 3) {
  console.log("Uso: node src/cli.js <operacion> <a> <b>");
  process.exit(1);
}

const [op, a, b] = args;
const x = Number(a);
const y = Number(b);

if (op === 'sumar') console.log(sumar(x, y));
else if (op === 'dividir') console.log(dividir(x, y));
else {
  console.log("Operación no válida");
  process.exit(2);
}
