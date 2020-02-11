#!/usr/bin/node
/*  Base class to make a Square with:
- Specific size.
- Validated dimensions.
- Method to print representation in console.
- Method to swap the height and the width.
- Method to double the dimensions of the Rectangle (multiplies by 2).
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
