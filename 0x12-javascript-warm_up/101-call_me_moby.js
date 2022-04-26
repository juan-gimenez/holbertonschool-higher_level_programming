#!/usr/bin/node
// function that executes x times a function.

exports.callMeMoby = function (x, fFunction) {
  while (x-- > 0) {
    fFunction();
  }
};
