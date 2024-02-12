#!/usr/bin/node
const argv = process.argv;
if ((argv.length < 4)) {
  console.log(0);
} else {
  let max = -Infinity; let max2 = -Infinity;
  const size = argv.length;
  for (let i = 2; i < size; i++) {
    const num = parseInt(argv[i]);
    if (num > max) {
      max2 = max;
      max = num;
    } else if (num > max2 && num < max) { // Update max2 if num is greater than max2 but less than max
      max2 = num;
    }
  }
  if (max2 === -Infinity) {
    console.log(0);
  } else {
    console.log(max2);
  }
}
