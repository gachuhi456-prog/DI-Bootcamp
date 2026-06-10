exercsexp
const products = [
  {
    name: "Laptop",
    price: 1200,
    category: "Electronics"
  },
  {
    name: "Phone",
    price: 800,
    category: "Electronics"
  },
  {
    name: "Book",
    price: 20,
    category: "Education"
  }
];

module.exports = products;

const people = [
  {
    name: "John",
    age: 20,
    location: "New York"
  },
  {
    name: "Alice",
    age: 25,
    location: "London"
  },
  {
    name: "Peter",
    age: 30,
    location: "Paris"
  }
];

export default people;

const fs = require("fs");

function readFile(fileName) {
  fs.readFile(fileName, "utf8", (err, data) => {
    if (err) {
      console.log(err);
      return;
    }

    console.log(data);
  });
}

function writeFile(fileName, content) {
  fs.writeFile(fileName, content, err => {
    if (err) {
      console.log(err);
      return;
    }

    console.log("File written successfully.");
  });
}

module.exports = {
  readFile,
  writeFile
};

export class TodoList {
  constructor() {
    this.tasks = [];
  }

  addTask(task) {
    this.tasks.push({
      name: task,
      completed: false
    });
  }

  completeTask(taskName) {
    const task = this.tasks.find(
      task => task.name === taskName
    );

    if (task) {
      task.completed = true;
    }
  }

  listTasks() {
    console.log("Todo List:");

    this.tasks.forEach(task => {
      console.log(
        `${task.name} - ${
          task.completed ? "Completed" : "Pending"
        }`
      );
    });
  }
}

mkdir math-app
cd math-app

npm init -y

npm install lodash

mkdir npm-beginner
cd npm-beginner

npm init -y

npm install chalk

This is the source file.


node shop.js
node app.js
node app.js
node app.js
node app.js
node app.js
node copy-file.js
node copy-file.js

node read-directory.js