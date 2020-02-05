#!/usr/bin/node
/* Script that prints the addition of 2 integers:
    The first argument is the first integer
    The second argument is the second integer
    Prototype: function add(a, b)
*/

const firstNum = parseInt(process.argv[2], 10);
const secondNum = parseInt(process.argv[3], 10);

function add (a, b) {
  return a + b;
}

const sum = add(firstNum, secondNum);

console.log(sum);
