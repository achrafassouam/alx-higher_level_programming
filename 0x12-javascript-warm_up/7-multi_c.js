#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    if (i === 0) {
      console.log('C is fun');
    } else {
      console.log('C is fun');
    }
    i++;
  }
}
