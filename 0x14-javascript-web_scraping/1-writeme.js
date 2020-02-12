#!/usr/bin/node
/*  Script that writes a string to a file.
    - The 1st argument is the file path
    - The 2nd argument is the string to write
    - The content of the file must be written in utf-8
*/

const { writeFile } = require('fs');
const [filePath, writeData] = process.argv.slice(2);
const handler = error => { if (error) console.log(error); };

writeFile(filePath, writeData, 'utf8', handler);
