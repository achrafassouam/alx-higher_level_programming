#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) throw err;

  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) throw err;

    fs.writeFile(dest, data1 + data2, err => {
      if (err) throw err;

      console.log(`Concatenated ${file1} and ${file2} into ${dest}`);
    });
  });
});
