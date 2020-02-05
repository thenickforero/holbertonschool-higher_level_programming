#!/usr/bin/node
/* Script that computes and prints a factorial
    The first argument is an integer (argument can be cast as integer),
    used for computing the factorial.
    Factorial of NaN is 1.
    It must use a recursive function.
*/

const num = parseInt(process.argv[2], 10);

const factorial = a => a === 0 || isNaN(a) ? 1 : a * factorial(a - 1);

const result = factorial(num);

console.log(result);
