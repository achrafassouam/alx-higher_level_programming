#!/usr/bin/node

const dict = require('./101-data.js').dict;

const inverted = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!inverted[occurrences]) {
    inverted[occurrences] = [];
  }
  inverted[occurrences].push(userId);
}

console.log(inverted);
