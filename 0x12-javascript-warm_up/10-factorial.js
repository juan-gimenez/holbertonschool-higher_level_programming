#!/usr/bin/node
// computes and prints a factorial
const a = process.argv;
const n = parseInt(a[2]);

function factorial (n) {
// base case
  if (n === 0 || Number.isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(n));
