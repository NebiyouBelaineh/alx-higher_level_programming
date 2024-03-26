#!/usr/bin/node
// Script that prints the title of a Start Wars movie where the episode number matches a give integer

const request = require('request');

// first argument is the movieId
const movieId = process.argv[2];

// Url for making a GET request based on movieId
const reqUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(reqUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const responseBody = JSON.parse(body);
  console.log(responseBody.title);
});
