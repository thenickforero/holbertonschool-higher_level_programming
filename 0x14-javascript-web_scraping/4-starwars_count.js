#!/usr/bin/node
/*  Script that prints the number of movies where the character “Wedge Antilles” is present.

    - The first argument is the API URL of the Star wars API:
      http://swapi.co/api/films/
    - Wedge Antilles is character ID 18
*/

const url = process.argv[2];
const wedgeId = '18';
const { get } = require('request');
const handler = (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    let count = 0;
    const movies = body.results;
    for (const movie of movies) {
      const characterCount = movie.characters.filter((data) => {
        return data.includes(wedgeId);
      });
      count += characterCount.length;
    }
    console.log(count);
  }
};

get(url, handler);
