#!/usr/bin/node
/* Script that searches the second biggest integer in the list of arguments.
    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
*/

const numArgs = process.argv.length - 2;

if (!numArgs || numArgs === 1) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).sort().reverse();
  console.log(numbers[1]);
}
