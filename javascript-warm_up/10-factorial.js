#!/usr/bin/node
const arg = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 0) {
    return (1);
  } else if (n === 1) {
    return (1);
  }
  return n * factorial(n - 1);
}
if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
