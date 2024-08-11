#!/usr/bin/node
// A script that computes the number of tasks completed by user id

// Read the cmd line
const args = process.argv;

// Get the todos url
const url = args[2];

if (url !== undefined) {
  // Send a GET request
  const request = require('request');

  request.get(url, { json: true }, (err, res, body) => {
    if (err) {
      // Error while the GET request
      console.log(err);
    } else {
      // Make an array to count completed tasks for each user id
      const completed = {};

      // Compute the number of tasks completed by user id
      body.forEach((tsk) => {
        if (Object.keys(completed).includes(tsk.userId.toString()) === false) {
          completed[tsk.userId] = 0;
        }
        if (tsk.completed === true) {
          completed[tsk.userId] += 1;
        }
      });

      // Filter users who did not complete any task
      Object.keys(completed).forEach((userID) => {
        if (completed[userID] === 0) {
          delete completed[userID];
        }
      });

      // Print the number of completed tasks by user id
      console.log(completed);
    }
  });
} else {
  // Invalid input format
  console.log('Usage: ./6-completed_tasks.js todos_url');
}
