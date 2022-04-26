#!/usr/bin/node
// js adv

const reqdata = require('./100-data').list;

const listp = reqdata.map((element, index) => element * index);
console.log(reqdata);
console.log(listp);
