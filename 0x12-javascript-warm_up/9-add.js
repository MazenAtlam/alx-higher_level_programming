#!/usr/bin/node

const { argv } = require('node:process');
const num1 = +argv[2];
const num2 = +argv[3];

function add (a, b) {
  console.log(a + b);
}

add(num1, num2);
