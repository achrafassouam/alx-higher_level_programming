#!/usr/bin/node

/*
  write a script that displays the status code of a GET request
  The first argument is the URL to request (GET)
  The status code must be printed like this: code: <status code>
  You must use the module request
 */

const request = require('request');

request(process.argv[2], (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
