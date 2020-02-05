#!/usr/bin/node
/* Script that prints x times “C is fun” using a loop:
    Where x is the first argument of the script
    If the first argument can’t be converted to an integer, print “Missing number of occurrences”
*/

const num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let iterator = 0; iterator < num; iterator++) {
    console.log('C is fun');
  }
}
