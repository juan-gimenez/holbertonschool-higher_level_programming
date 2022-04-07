#!/usr/bin/node
// print square
const a = process.argv;
const number = parseInt(a[2]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < number; x++) {
  // repeat str method
    console.log('X'.repeat(number));
  }
}
