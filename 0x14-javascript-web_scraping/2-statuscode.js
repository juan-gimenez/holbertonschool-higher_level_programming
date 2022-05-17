#!/usr/bin/node
const r = require('request');
const route = process.argv[2];
r(route, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
