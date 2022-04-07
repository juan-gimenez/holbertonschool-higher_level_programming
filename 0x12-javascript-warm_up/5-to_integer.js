#!/usr/bin/node
// check if can be an int
const a = process.argv;
const number = parseInt(a[2]);
if (!number) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
