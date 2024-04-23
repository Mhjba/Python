#!/usr/bin/node

const request = require('request');
const ur_API = process.argv[2];
request.get(ur_API, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }else {
  const tds = JSON.parse(body);
  const users_D = {};
  for (const td of tds) {
    if (!(td.user_Id in users_D) && td.completed) {
      users_D[td.user_Id] = 1;
    } else if (td.completed) {
      users_D[td.user_Id] += 1;
    }
  }
}
  console.log(users_D);
});
