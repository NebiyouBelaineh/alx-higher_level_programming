#!/usr/bin/node
const argv = process.argv;
const sum = add(argv[2], argv[3]);
console.log(sum);

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
