#!/usr/bin/node
const request = require('request');

const process = require('process');
const id_data = process.argv[2];
const url_data = `https://swapi-api.alx-tools.com/api/films/${id_data}`;

request(url_data, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
