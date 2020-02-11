#!/usr/bin/node
/*  Base class to make a Rectangle with:
    - Validated dimensions.
    - Print to console method.
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
}

module.exports = Rectangle;
