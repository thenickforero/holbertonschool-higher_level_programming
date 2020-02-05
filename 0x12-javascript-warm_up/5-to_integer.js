#!/usr/bin/node
/* Script that prints My number: <first argument converted in integer>
    If the argument can’t be converted to an integer, print “Not a number”
*/
const num = parseInt(process.argv[2], 10);
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
