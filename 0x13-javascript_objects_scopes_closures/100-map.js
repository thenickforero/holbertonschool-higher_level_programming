#!/usr/bin/node
//  Script that imports an array and computes a new array using map.

const data = require('./100-data').list;
const parsedData = data.map((num, index) => num * index);
console.log(data);
console.log(parsedData);
