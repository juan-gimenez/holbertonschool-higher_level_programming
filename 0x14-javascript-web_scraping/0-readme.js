#!/usr/bin/node
const fs = require('fs');
const f = process.argv[2];

fs.readFile(f, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
