#!/usr/bin/node
const argv = process.argv;
if (isNaN(parseInt(argv[2]))) {
  console.log(1);
} else {
  const fact = factorial(parseInt(argv[2]));
  console.log(fact);
}

function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return factorial(num - 1) * num;
}
