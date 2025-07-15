#!/usr/bin/node
const arguments = process.argv.slice(2).map(Number);
if (arguments.length === 0) {
    console.log('0')
} else if (arguments.length === 1) {
    console.log('0')
} else {
  arguments.sort((a, b) => b - a);
  console.log(arguments[1]);
}

