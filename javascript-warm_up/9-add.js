#!/usr/bin/node
// #!/usr/bin/env node : pour execution
const premier_argument = process.argv[2];
const deuxieme_argument = process.argv[3];
const a = parseInt(premier_argument);
const b = parseInt(deuxieme_argument);
function add(premier_nombre, deuxieme_nombre) {
    return premier_nombre + deuxieme_nombre;
}
console.log(add(premier_nombre, deuxieme_nombre))
