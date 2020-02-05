#!/usr/bin/node
/* Script that prints the first argument passed to it:
    If no arguments are passed to the script, print “No argument”
*/
console.log(process.argv[2] === undefined ? 'No argument' : process.argv[2]);
