#!/usr/bin/node
//  prints a message depending on the number of args
const a = process.argv;
const myVar = ' is ';
console.log(a[2] + myVar + a[3]);
