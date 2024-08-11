#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

// Read the cmd line
const args = process.argv;

// Get the movie id
const movieID = args[2];

// Define some constants
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID + '/';
const start = 0;
const request = require('request');

if (movieID !== undefined) {
  // Send a GET request
  request.get(url, { json: true }, (err, res, body) => {
    if (err) {
      // Error while the GET request
      console.log(err);
    } else {
      // Get all characters in this movie
      const allCharacters = body.characters;

      // Iterate over all chracters to request them in same order
      printCharacters(allCharacters, start);
    }
  });
} else {
  // Invalid input format
  console.log('Usage: ./101-starwars_characters.js movie_id');
}

/**
 * printCharacters - A function to print all characters by requesting their URL
 *
 * @charactersURL: An array of all characters url
 * @currIndex: The index of the current character to request
 *
 * Return: nothing
 */
function printCharacters (charactersURL, currIndex) {
  // Send a GET request
  request(charactersURL[currIndex], { json: true }, (err, res, body) => {
    if (err) {
      // Error while the GET request
      console.log(err);
    } else {
      // Print the character name
      console.log(body.name);
      if (currIndex + 1 < charactersURL.length) {
        printCharacters(charactersURL, currIndex + 1);
      }
    }
  });
}
