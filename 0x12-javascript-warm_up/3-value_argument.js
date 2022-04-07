#!/usr/bin/node
// prints a message depending on the number of args
const a = process.argv;
if (a[2] === undefined) {
  console.log('No argument');
} else {
  console.log(a[2]);
// if argument
}
