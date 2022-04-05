#!/usr/bin/node
// count number of occurrences
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (const i in list) {
    if (searchElement === list[i]) {
      counter++;
    } else { continue; }
  }
  return counter;
};
