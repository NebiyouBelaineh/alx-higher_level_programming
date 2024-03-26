#!/usr/bin/node
// Script that prints the title of a Start Wars movie where the episode number matches a give integer

const request = require('request');

// first argument is the movieId
// const apiUrl = process.argv[2];

// Url for making a GET request based on movieId
const reqUrl = process.argv[2];
// actorId we are interested in
const actorId = 'people/18';
// Set counter
let count = 0;

// Make request
request(reqUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const responseBody = JSON.parse(body);
  // Isolate results section to get movies
  const results = responseBody.results;
  for (const movie of results) {
    const characters = movie.characters;
    // Check each character item
    for (const person of characters) {
      if (person.includes(actorId)) {
        count++;
      }
    }
  }

  console.log(count);
});
