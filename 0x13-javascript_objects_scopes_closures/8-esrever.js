#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  list.forEach(element => {
    reverse.unshift(element);
  });
  return reverse;
};
