#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

// Read the cmd line
const args = process.argv;

// Get the movie id
const movieID = args[2];

// Define some constants
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID + '/';

if (movieID !== undefined) {
  // Send a GET request
  const request = require('request');

  request.get(url, { json: true }, (err, res, body) => {
    if (err) {
      // Error while the GET request
      console.log(err);
    } else {
      // Get all characters in this movie
      const allCharacters = body.characters;

      allCharacters.forEach((characterURL) => {
        request.get(characterURL, { json: true }, (err, res, body) => {
          if (err) {
            // Error while the GET request
            console.log(err);
          } else {
            // Print the character name
            console.log(body.name);
	  }
	});
      });
    }
  });
} else {
  // Invalid input format
  console.log('Usage: ./100-starwars_characters.js movie_id');
}
