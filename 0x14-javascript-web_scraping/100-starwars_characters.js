#!/usr/bin/node

const r = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

r(url, function (err, response, body) {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      r(character, function (err, response, body) {
        if (err) console.log(err);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
