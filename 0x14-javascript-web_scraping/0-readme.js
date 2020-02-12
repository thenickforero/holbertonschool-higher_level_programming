#!/usr/bin/node
/*  Script that reads and prints the content of a file.
    - The first argument is the file path
    - The content of the file must be read in utf-8
*/

const { readFile } = require('fs');
const filePath = process.argv[2];
const handler = (err, data) => console.log(err !== null ? err : data);

readFile(filePath, 'utf8', handler);
