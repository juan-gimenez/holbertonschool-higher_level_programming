#!/usr/bin/node
// function that increments and calls a function.

exports.addMeMaybe = function (n, fFunction) {
  fFunction(n + 1);
};
