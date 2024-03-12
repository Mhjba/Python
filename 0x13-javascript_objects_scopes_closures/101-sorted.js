#!/usr/bin/node
// function that returns the number of occurrences in a list

const dict = require('./100-data').dict;
console.log(dict);
const newdict = dict.map (function (e, index) {
  return (e * index);
});
console.log(newdict);
