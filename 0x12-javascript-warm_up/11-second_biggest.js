#!/usr/bin/node
const argv = process.argv;
if ((argv.length < 3)) {
  console.log(0);
} else {
  let max = 0; let max2;
  const size = argv.length;
  for (let i = 2; i < size; i++) {
    const num = parseInt(argv[i]);
    if (num > max) {
      max2 = max;
      max = num;
    }
  }
  console.log(max2);
}
