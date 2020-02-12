#!/usr/bin/node
/*  Script that prints the number of movies where the character “Wedge Antilles” is present.

    - The first argument is the API URL of the Star wars API:
      http://swapi.co/api/films/
    - Wedge Antilles is character ID 18
*/

const url = process.argv[2];
const wedge = 'https://swapi.co/api/people/18/';
const { get } = require('request');
const handler = (error, response, body) => {
  if (!error && response.statusCode === 200) {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    let count = 0;
    const movies = body.results;
    for (const movie of movies) {
      const characters = movie.characters;
      if (characters.includes(wedge)) {
        count++;
      }
    }
    console.log(count);
  }
};

get(url, handler);
