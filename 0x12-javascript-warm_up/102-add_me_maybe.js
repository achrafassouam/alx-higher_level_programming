#!/usr/bin/node
//  a function that increments and calls a function

exports.addMeMaybe = function incrementAndCall (number, theFunction) {
  number++;
  theFunction(number);
};
