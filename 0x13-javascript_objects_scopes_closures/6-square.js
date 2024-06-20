#!/usr/bin/node
const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i; let j;

      for (i = 0; i < this.height; i++) {
        for (j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
};
