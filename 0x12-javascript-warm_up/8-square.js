#!/usr/bin/node
/* Script that prints a square
    The first argument is the size of the square
    If the first argument can’t be converted to an integer, print “Missing size”
    You must use the character X to print the square
*/

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let iterator = 0; iterator < size; iterator++) {
    console.log('X'.repeat(size));
  }
}
