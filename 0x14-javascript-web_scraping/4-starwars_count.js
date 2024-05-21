#!/usr/bin/node

/* write a script that prints the number of movies where the character “Wedge Antilles” is present.
   The first argument is the API URL of the Star wars API: http://swapi-api.hbtn.io/api/films/
   Wedge Antilles is character ID 18
   You must use the module request
*/

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
