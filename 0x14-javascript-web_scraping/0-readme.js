#!/usr/bin/node
// A script that reads and prints the content of a file

// Create file stream
const fs = require('fs')

// Read the cmd line
const args = process.argv

// Get file name
const file = args[2]

if (file != undefined)
{
  // Read data from the file
  fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
      // Error reading the file
      console.log(err)
    } else {
      // Print the content of the file
      console.log(data)
    }
  })
} else {
	console.log('Usage: ./0-readme.js file_path')
}
