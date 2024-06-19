#!/usr/bin/node

const { argv } = require('node:process');
const times = +argv[2];
let i;

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
