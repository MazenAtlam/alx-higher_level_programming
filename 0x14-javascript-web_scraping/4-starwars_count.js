#!/usr/bin/node
// A script that prints the number of movies
// Where the character “Wedge Antilles” is present

// Read the cmd line
const args = process.argv;

// Get the films url
const url = args[2];

if (url !== undefined) {
  // Send a GET request
  const request = require('request');

  request.get(url, { json: true }, (err, res, body) => {
    if (err) {
      // Error while the GET request
      console.log(err);
    } else {
      // Find the movies where the character “Wedge Antilles” is present
      const allMovies = body.results;
      const characterID = "https://swapi-api.alx-tools.com/api/people/18/";
      let moviesCount = 0;

      allMovies.forEach((movie) => {
        if (movie.characters.includes(characterID)) {
          moviesCount += 1;
	}
      });

      // Print the number of movies
      console.log(moviesCount);
    }
  });
} else {
  // Invalid input format
  console.log('Usage: ./4-starwars_count.js films_url');
}
