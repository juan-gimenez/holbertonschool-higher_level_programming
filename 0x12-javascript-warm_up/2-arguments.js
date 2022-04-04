#!/usr/bin/node
// prints a message depending on the number of args
const a = process.argv.length;

if (a === 3) {
    console.log('Argument found');
} else if (a <= 2)
    console.log('No argument');
else {
    console.log('Arguments found');
}
