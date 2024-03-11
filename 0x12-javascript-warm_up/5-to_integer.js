#!/usr/bin/node
// script that prints My number

const argv = parseInt(process.argv[2]);
if (Number.isNaN(argv)) {
	  console.log('Not a number');
} else {
	  console.log('My number: ' + argv);
}
