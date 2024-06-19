#!/usr/bin/node

const { argv } = require('node:process');
const size = +argv[2];
let i; let j;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
