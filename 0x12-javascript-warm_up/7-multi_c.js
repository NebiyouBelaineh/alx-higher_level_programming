#!/usr/bin/node
const argv = process.argv;
if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const size = (parseInt(argv[2]));
  for (let i = 0; i < size; i++) {
    console.log('C is fun');
  }
}
