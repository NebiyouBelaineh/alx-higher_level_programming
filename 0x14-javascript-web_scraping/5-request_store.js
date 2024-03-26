#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

// Url for making a GET request
const reqUrl = process.argv[2];
// file to store the text obtained
const filename = process.argv[3];

// Make request
request(reqUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  //  const responseBody = body;
  //  console.log(responseBody);
  fs.writeFile(filename, body, function (err) {
    if (err) {
      console.log(err);
    }
  });
});
