#!/usr/bin/node
// script that searches the second biggest
// integer in the list of arguments.

let line = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  line = args[args.length - 2];
}
console.log(line);
