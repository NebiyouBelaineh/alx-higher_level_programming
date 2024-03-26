#!/usr/bin/node
// Script that display the status code of a GET request

const request = require('request');

const reqUrl = process.argv[2];

request(reqUrl, function (err, response) {
  if (err) {
    console.log(err);
  }
  console.log('code:', response && response.statusCode);
});
