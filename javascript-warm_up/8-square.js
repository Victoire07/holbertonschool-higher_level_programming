#!/usr/bin/node
// #!/usr/bin/env node : pour execution
const argument = process.argv[2];
const number = parseInt(argument);
if (isNaN(number)) {
  console.log('Missing size');
} else if (number > 0) {
  const line = 'X'.repeat(number);
  for (let index = 0; index < number; index++) {
    console.log(line);
  }
}
