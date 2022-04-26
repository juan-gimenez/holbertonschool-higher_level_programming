#!/usr/bin/node
// script that concats 2 files

const impfs = require('fs');
const text1 = impfs.readFileSync(process.argv[2], 'utf-8');
const text2 = impfs.readFileSync(process.argv[3], 'utf-8');
impfs.writeFileSync(process.argv[4], text1 + text2, 'utf-8');
