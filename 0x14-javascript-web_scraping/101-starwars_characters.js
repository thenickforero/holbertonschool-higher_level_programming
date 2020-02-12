#!/usr/bin/node

const movieId = process.argv[2];
const url = `http://swapi.co/api/films/${movieId}`;
const { get } = require('request');
const { promisify } = require('util');
const getCharacter = promisify(get);

async function getCharacterName(url) {
  try {
    const character = await getCharacter(url);
    console.log(JSON.parse(character.body).name);
  } catch (error) {
    console.log(error);
  }
}
const filmHandler = async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    const characters = body.characters;
    for (const character of characters) {
      await getCharacterName(character);
    }
  }
};
get(url, filmHandler);
