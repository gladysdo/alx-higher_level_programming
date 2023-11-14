#!/usr/bin/node
// prints the first argument passed

const arg = process.argv[2];

if (arg) {
  console.log(arg);
} else {
  console.log('NO argument');
}
