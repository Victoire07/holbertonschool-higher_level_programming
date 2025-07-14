#!/usr/bin/node
// #!/usr/bin/env node : pour execution

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
