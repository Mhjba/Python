#!/usr/bin/node
const request = require('request');

const id_data = process.argv[2];
const url_data = 'https://swapi-api.hbtn.io/api/films/';
request.get(url_data + id_data, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const dt = JSON.parse(body);
  const todos = dt.characters;
  for (const i of todos) {
    request.get(i, function (error, response, bodys) {
      if (error) {
        console.log(error);
      }
      const data = JSON.parse(bodys);
      console.log(data.name);
    });
  }
});
