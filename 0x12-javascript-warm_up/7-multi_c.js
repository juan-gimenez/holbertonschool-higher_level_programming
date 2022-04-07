#!/usr/bin/node
// print “C is fun” x times
const a = process.argv;
const number = parseInt(a[2]);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < number; x++) {
    console.log('C is fun');
  }
}
