#!/usr/bin/node
// A script that displays the status code of a GET request

// Read the cmd line
const args = process.argv;

// Get the URL
const url = args[2];

if (url !== undefined) {
  // Send a GET request
  const request = require('request');

  request.get(url, (err, res, body) => {
    if (err) {
      // Error while the GET request
      console.log(err);

    } else {
      // Print yhe status code
      console.log('code: ', res.statusCode);
    }
  });

} else {
  // Invalid input format
  console.log('Usage: ./2-statuscode.js url');
}
