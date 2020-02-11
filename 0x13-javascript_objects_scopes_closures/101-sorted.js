#!/usr/bin/node
/*  Script that imports a dictionary of occurrences by user id and
    computes a dictionary of user ids by occurrence.

    In the new dictionary:
    - A key is a number of occurrences
    - A value is the list of user ids

*/

const data = require('./101-data.js').dict;
const ocurrences = {};
for (const key in data) {
  const idx = data[key];
  if (ocurrences[idx] === undefined) {
    ocurrences[idx] = [];
  }
  ocurrences[idx].push(key);
}

console.log(ocurrences);
