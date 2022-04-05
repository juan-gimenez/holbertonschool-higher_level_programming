#!/usr/bin/node
// class square
const newSquare = require('./5-square');
module.exports = class Square extends newSquare {
  charPrint (c) {
    if (c === 'undefined') {
      this.print();
      // use last method
    } else {
      for (let x = 0; x < this.width; x++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
