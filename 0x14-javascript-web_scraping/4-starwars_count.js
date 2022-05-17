#!/usr/bin/node

const r = require('request');
const id = '/18/';
const url = process.argv[2];

r(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }

  let count = 0;
  for (const movie of JSON.parse(body).results) {
    for (const char of movie.characters) {
      if (char.includes(id)) {
        count += 1;
      }
    }
  }
  console.log(count);
});
