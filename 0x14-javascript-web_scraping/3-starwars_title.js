#!/usr/bin/node
const r = require('request');
const film = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
r(url + film, function (err, r, body) {
  if (err) {
    console.log(err);
  } else if (r.statusCode === 200) {
    const tojson = JSON.parse(body);
    console.log(tojson.title);
  } else {
    console.log(err);
  }
});
