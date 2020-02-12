#!/usr/bin/node
/*  Script that prints the title of a Star Wars movie where the episode number
    matches a given integer.

    - The first argument is the movie ID
    - Must use the Star wars API with the endpoint:
      http://swapi.co/api/films/:id
*/

const movieId = process.argv[2];
const url = `http://swapi.co/api/films/${movieId}`;
const { get } = require('request');
const handler = (error, response, body) => {
  if (!error && response.statusCode === 200) {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    console.log(body.title);
  }
};

get(url, handler);
