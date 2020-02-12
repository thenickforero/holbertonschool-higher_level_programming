#!/usr/bin/node

const movieId = process.argv[2];
const url = `http://swapi.co/api/films/${movieId}`;
const { get } = require('request');
const characterHandler = (error, response, body) => {
  if (error) console.log(error);
  console.log(JSON.parse(body).name);
};
const filmHandler = (error, response, body) => {
  if (!error && response.statusCode === 200) {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    const characters = body.characters;
    for (const character of characters) {
      get(character, characterHandler);
    }
  }
};

get(url, filmHandler);
