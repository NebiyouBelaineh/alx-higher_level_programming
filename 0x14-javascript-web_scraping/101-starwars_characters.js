#!/usr/bin/node
// script that prints all characters of a Star Wars movie depending on
// the movie id:
const request = require('request');
const movieId = process.argv[2];
const reqUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(reqUrl, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  const responseBody = JSON.parse(body);
  const characters = responseBody.characters;
  // Make a request for each chatacter to get their name
  characters.forEach(function (element) {
    request(element, function (err, response, body) {
      if (err) {
        console.log(err);
      }
      const resJson = JSON.parse(body);
      const name = resJson.name;
      console.log(name);
    });
  });
});
