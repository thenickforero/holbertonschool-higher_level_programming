#!/usr/bin/node
/*  Script that gets the contents of a webpage and stores it in a file.
    - The 1st argument is the URL to request
    - The 2nd argument the file path to store the body response
    - The file must be UTF-8 encoded
*/

const { writeFile } = require('fs');
const { get } = require('request');
const [url, filePath] = process.argv.slice(2);
const responseHandler = error => {
  if (error) console.log(error);
};
const requestHandler = (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    writeFile(filePath, body, 'utf8', responseHandler);
  }
};

get(url, requestHandler);
