#!/usr/bin/node

/*  script that writes a string to a file of a file
    first argument is the file path
	second argument is the string to write
    The content of the file must be read in utf-8
    If an error occurred during the reading, print the error object
*/

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
	console.error(err);
  }
});

