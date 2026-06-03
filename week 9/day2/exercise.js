exercise
npx create-react-app redux-toolkit-todo
cd redux-toolkit-todo

npm install @reduxjs/toolkit react-redux

src/
│
├── app/
│   └── store.js
│
├── features/
│   └── todoSlice.js
│
├── components/
│   ├── AddTodo.js
│   ├── TodoItem.js
│   └── TodoList.js
│
├── App.js
├── App.css
└── index.js

import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  todos: []
};

const todoSlice = createSlice({
  name: "todos",
  initialState,

  reducers: {
    addTodo: (state, action) => {
      state.todos.push({
        id: Date.now(),
        text: action.payload,
        completed: false
      });
    },

    toggleTodo: (state, action) => {
      const todo = state.todos.find(
        (todo) => todo.id === action.payload
      );

      if (todo) {
        todo.completed = !todo.completed;
      }
    },

    removeTodo: (state, action) => {
      state.todos = state.todos.filter(
        (todo) => todo.id !== action.payload
      );
    }
  }
});

export const {
  addTodo,
  toggleTodo,
  removeTodo
} = todoSlice.actions;

export default todoSlice.reducer;

import { configureStore } from "@reduxjs/toolkit";
import todoReducer from "../features/todoSlice";

export const store = configureStore({
  reducer: {
    todo: todoReducer
  }
});

import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addTodo } from "../features/todoSlice";

function AddTodo() {
  const [text, setText] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!text.trim()) return;

    dispatch(addTodo(text));
    setText("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter a todo"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button type="submit">
        Add Todo
      </button>
    </form>
  );
}

export default AddTodo;

import React from "react";
import { useDispatch } from "react-redux";
import {
  toggleTodo,
  removeTodo
} from "../features/todoSlice";

function TodoItem({ todo }) {
  const dispatch = useDispatch();

  return (
    <li>
      <span
        style={{
          textDecoration: todo.completed
            ? "line-through"
            : "none",
          cursor: "pointer"
        }}
        onClick={() =>
          dispatch(toggleTodo(todo.id))
        }
      >
        {todo.text}
      </span>

      <button
        onClick={() =>
          dispatch(removeTodo(todo.id))
        }
      >
        Delete
      </button>
    </li>
  );
}

export default TodoItem;

import React from "react";
import { useSelector } from "react-redux";
import TodoItem from "./TodoItem";

function TodoList() {
  const todos = useSelector(
    (state) => state.todo.todos
  );

  return (
    <div>
      <h2>Todo List</h2>

      <ul>
        {todos.map((todo) => (
          <TodoItem
            key={todo.id}
            todo={todo}
          />
        ))}
      </ul>
    </div>
  );
}

export default TodoList;

import React from "react";
import AddTodo from "./components/AddTodo";
import TodoList from "./components/TodoList";
import "./App.css";

function App() {
  return (
    <div className="container">
      <h1>Redux Toolkit Todo App</h1>

      <AddTodo />

      <TodoList />
    </div>
  );
}

export default App;

import React from "react";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";
import App from "./App";
import { store } from "./app/store";

const root = ReactDOM.createRoot(
  document.getElementById("root")
);

root.render(
  <Provider store={store}>
    <App />
  </Provider>
);

body {
  margin: 0;
  background-color: #f4f4f4;
  font-family: Arial, sans-serif;
}

.container {
  width: 500px;
  margin: 40px auto;
  background: white;
  padding: 20px;
  border-radius: 10px;
}

input {
  padding: 10px;
  width: 70%;
}

button {
  padding: 10px;
  margin-left: 5px;
  cursor: pointer;
}

ul {
  padding: 0;
}

li {
  list-style: none;
  padding: 10px;
  margin-top: 10px;
  background: #eee;
  display: flex;
  justify-content: space-between;
}