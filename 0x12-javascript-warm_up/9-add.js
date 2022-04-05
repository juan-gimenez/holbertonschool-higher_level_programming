#!/usr/bin/node
// add two numbers
const args = process.argv;
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
// call the function
console.log(add(args[2], args[3]));
