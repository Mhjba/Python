#!/usr/bin/node
const request = require('request');

const process = require('process');
const data_id = process.argv[2];
const data_url = `https://swapi-api.alx-tools.com/api/films/${data_id}`;

request(data_url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
