#!/usr/bin/node

/*
  write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
  The first argument is the episode number
  You must use the Star wars API with the endpoint http://swapi.co/api/films/:episode_id
  You must use the module request
*/

const request = require('request');
const episode = process.argv[2];
const url = `http://swapi-api.hbtn.io/api/films/${episode}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
