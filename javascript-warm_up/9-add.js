#!/usr/bin/node
// #!/usr/bin/env node : pour execution
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add(premier_nombre, deuxieme_nombre) {
    return premier_nombre + deuxieme_nombre;
}
console.log(add(a, b))
