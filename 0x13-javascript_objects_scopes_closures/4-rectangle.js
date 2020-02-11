#!/usr/bin/node
/*  Base class to make a Rectangle with:
- Validated dimensions.
- Method to print representation in console.
- Method to swap the height and the width.
- Method to double the dimensions of the Rectangle (multiplies by 2).
*/

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let iterator = 0; iterator < this.height; iterator++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}

module.exports = Rectangle;
