#!/usr/bin/node
/*  Base class to make a Square with:
- Specific size.
- Validated dimensions.
- Method to print representation in console
(optionally using a specific character).
- Method to swap the height and the width.
- Method to double the dimensions of the Rectangle (multiplies by 2).
*/

const Base = require('./5-square');

class Square extends Base {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let iterator = 0; iterator < this.height; iterator++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
