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
  // Make a request for each chatacter to get their name in an asynchronous way
  characters.forEach(async function (element) {
    await new Promise(function (resolve, reject) {
      request(element, function (err, response, body) {
        if (err) {
          reject(err);
        }
        const resJson = JSON.parse(body);
        const name = resJson.name;
        console.log(name);
        resolve();
      });
    });
  });
});
