#!/usr/bin/node

/* write a script that prints the number of completed tasks by user id.
   The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
   You must use the module request
*/

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const completed = tasks.filter(task => task.completed);
    const completedByUser = completed.reduce((acc, task) => {
      if (!acc[task.userId]) {
        acc[task.userId] = 1;
      } else {
        acc[task.userId]++;
      }
      return acc;
    }, {});
    console.log(completedByUser);
  }
});
