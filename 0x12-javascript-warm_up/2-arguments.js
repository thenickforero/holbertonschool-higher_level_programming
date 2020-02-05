#!/usr/bin/node
/* Script that prints a message depending of the number of arguments passed:
    If no arguments are passed to the script, print “No argument”
    If only one argument is passed to the script, print “Argument found”
    Otherwise, print “Arguments found”
*/
const numArgs = process.argv.length;

if (numArgs > 2) {
  console.log(numArgs === 3 ? 'Argument found' : 'Arguments found');
} else {
  console.log('No argument');
}
