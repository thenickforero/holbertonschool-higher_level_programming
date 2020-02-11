#!/usr/bin/node
/*  Script that concats 2 files.
    - The 1st argument is the file path of the first source file.
    - The 2nd argument is the file path of the second source file.
    - The 3rd argument is the file path of the destination.
*/

const { readFile, appendFileSync } = require('fs');
const [fileA, fileB, outputFile] = process.argv.slice(2);

readFile(fileA, (err, data) => {
  if (err) throw err;
  appendFileSync(outputFile, data);
});

readFile(fileB, (err, data) => {
  if (err) throw err;
  appendFileSync(outputFile, data);
});
