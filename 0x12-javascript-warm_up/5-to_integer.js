#!/usr/bin/node
const argv = process.argv;
if (!isNaN(parseInt(argv[2]))) {
  const myNum = parseInt(argv[2]);
  console.log('My number: ' + myNum);
} else {
  console.log('Not a number');
}
