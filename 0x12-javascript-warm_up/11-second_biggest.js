#!/usr/bin/node
// find second largest numb
let intArray = process.argv.slice(2);
// let intArray = intArray.filter(x => x !== undefined);
if (intArray.length <= 1) {
  console.log(0);
}
intArray = [...new Set(intArray)]; // Remove duplicate numbers
const secondLargestNumber = intArray.sort((a, b) => {
  return b - a;
  const filtered = secondLargestNumber.filter(x => x !== undefined);
  console.log(filtered);
})[1];
