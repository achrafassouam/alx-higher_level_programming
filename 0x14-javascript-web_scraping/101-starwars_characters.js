#!/usr/bin/node

/* write a script that prints all characters of a Star Wars movie:
   The first argument is the movie ID
   Display one character name by line in the same order of the list “characters” in the /films/ response
   You must use the Star wars API with the endpoint http://swapi-api.hbtn.io/api/films/:id
   You must use the module request
 */
const request = require('request');
const movieId = process.argv[2];
const url = `http://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
