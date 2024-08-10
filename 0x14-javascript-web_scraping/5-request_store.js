#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file

// Read the cmd line
const args = process.argv;

// Get the url to request
const url = args[2];

// Get the file path to store the body response
const filePath = args[3];

if (url !== undefined && filePath !== undefined) {
  // Create file stream
  const fs = require('fs');

  // Send a GET request
  const request = require('request');

  request.get(url, (err, res, body) => {
    if (err) {
      // Error while the GET request
      console.log(err);
    } else {
      // Store the body in the file
      fs.writeFile(filePath, body, { encoding: 'utf8' }, (err) => {
        if (err) {
          // Error Writing into the file
          console.log(err);
        }
      });
    }
  });
} else {
  // Invalid input format
  console.log('Usage: ./5-request_store.js webpage_url file_path');
}
