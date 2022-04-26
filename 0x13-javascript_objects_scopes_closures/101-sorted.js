#!/usr/bin/node
// computes a dictionary of user ids by occurrence.

const reqdic = require('./101-data').dict;
const emptdic = {};
for (const usrid in reqdic) {
  if (reqdic[usrid] in emptdic) {
    emptdic[reqdic[usrid]].push(usrid);
  } else {
    emptdic[reqdic[usrid]] = [usrid];
  }
}
console.log(emptdic);
