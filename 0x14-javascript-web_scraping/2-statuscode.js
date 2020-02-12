#!/usr/bin/node
/*  Script that display the status code of a GET request.
    - The first argument is the URL to request (GET)
    - The status code must be printed like this: code: <status code>
*/

const url = process.argv[2];
const { get } = require('request');
const handler = (error, response) => {
  if (!error) {
    console.log(`code: ${response.statusCode}`);
  }
};

get(url, handler);
