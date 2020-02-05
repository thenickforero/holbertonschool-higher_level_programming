#!/usr/bin/node
/* Script that searches the second biggest integer in the list of arguments.
    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
*/

const numbers = process.argv.slice(2).map(a => parseInt(a, 10)).sort().reverse();

if (!numbers.length || numbers.length === 1) {
  console.log(0);
} else {
  console.log(numbers[1]);
}
