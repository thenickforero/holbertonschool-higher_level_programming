#!/usr/bin/node
/*  Script that computes the number of tasks completed by user id.
    - The first argument is the API URL:
      https://jsonplaceholder.typicode.com/todos
*/

const options = {
  url: process.argv[2],
  qs: { completed: 'true' }
};
const { get } = require('request');
const handler = (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    const tasksCompleted = {};
    for (const todo of body) {
      const key = todo.userId;
      if (key in tasksCompleted) {
        tasksCompleted[key] += 1;
      } else {
        tasksCompleted[key] = 1;
      }
    }
    console.log(tasksCompleted);
  }
};

get(options, handler);
