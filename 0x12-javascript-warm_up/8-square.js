#!/usr/bin/node
const argv = process.argv;
if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  const size = parseInt(argv[2]);
  for (let i = 0; i < size; i++) {
    let square = '';
    for (let j = 0; j < size; j++) {
      square = square + 'X';
    }
    console.log(square);
  }
}
