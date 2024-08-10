#!/usr/bin/node
// A script that prints the title of a Star Wars movie
// Where the episode number matches a given integer

// Read the cmd line
const args = process.argv;

// Get the movie id
const movieID = args[2];

// Define the URL
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

if (movieID !== undefined) {
  // Send a GET request
  const request = require('request');

  request.get(url, { json: true }, (err, res, body) => {
    if (err) {
      // Error while the GET request
      console.log(err);
    } else {
      // Print the title
      console.log(body.title);
    }
  });
} else {
  // Invalid input format
  console.log('Usage: ./3-starwars_title.js movie_id');
}
