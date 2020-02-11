#!/usr/bin/node
/*  Function that prints the number of arguments already printed
    and the new argument value.
*/

exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  } else {
    this.count++;
  }
  console.log(`${this.count}: ${item}`);
};
