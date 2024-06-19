#!/usr/bin/node

const { argv } = require('node:process');
let numList;
let i;
let max;
let second;

function toIntegerArray (array) {
  const intList = [];
  let num;

  for (i = 2; i < array.length; i++) {
    num = +array[i];
    intList.push(num);
  }
  return (intList);
}

if (argv.length < 4) {
  console.log(0);
} else {
  numList = toIntegerArray(argv);

  if (numList[0] > numList[1]) {
    max = numList[0];
    second = numList[1];
  } else {
    max = numList[1];
    second = numList[0];
  }

  for (i = 2; i < numList.length; i++) {
    if (numList[i] > max) {
      second = max;
      max = numList[i];
    } else if (numList[i] > second) {
      second = numList[i];
    }
  }
  console.log(second);
}
