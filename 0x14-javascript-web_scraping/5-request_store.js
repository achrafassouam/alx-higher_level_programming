#!/usr/bin/node

/* a script that gets the contents of a webpage and stores it in a file
   The first argument is the URL to request
   The second argument the file path to store the body response
   You must use the module request
 */

const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
