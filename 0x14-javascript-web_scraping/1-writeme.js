#!/usr/bin/node
// A script that writes a string to a file

// Create file stream
const fs = require('fs');

// Read the cmd line
const args = process.argv;

// Get file name
const file = args[2];

// Get the string to write
const string = args[3];

if (file !== undefined || string !== undefined) {
  // Write the string into the file
  fs.writeFile(file, string, { encoding: 'utf8' }, (err) => {
    if (err) {
      // Error writing into the file
      console.log(err);
    }
  });
} else {
  console.log('Usage: ./1-writeme.js file_path string_to_write');
}
