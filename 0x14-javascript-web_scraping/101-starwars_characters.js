#!/usr/bin/node

/* write a script that prints all characters of a Star Wars movie:
   The first argument is the movie ID
   You must use the Star wars API with the endpoint http://swapi-api.hbtn.io/api/films/:id
   You must use the module request
 */

const request = require('request');
const movieId = process.argv[2];
const url = `http://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
