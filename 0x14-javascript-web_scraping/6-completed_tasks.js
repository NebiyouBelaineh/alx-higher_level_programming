#!/usr/bin/node
// script that computes the number of users completed by user id.

const request = require('request');
const reqUrl = process.argv[2];

request(reqUrl, (err, response, body) => {
  if (err) { console.log(err); }

  const completed = {};
  const responseBody = JSON.parse(body);
  for (const user of responseBody) {
    if (user.completed) {
      if (completed[user.userId]) {
        completed[user.userId]++;
      } else {
        completed[user.userId] = 1;
      }
    }
  }
  console.log(completed);
});
