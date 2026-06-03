exercise1
npx create-react-app redux-todo
cd redux-todo

npm install redux react-redux

src/
│
├── actions/
│   └── todoActions.js
│
├── reducers/
│   ├── todoReducer.js
│   └── index.js
│
├── components/
│   ├── TodoForm.js
│   ├── TodoList.js
│   └── TodoItem.js
│
├── store.js
├── App.js
└── index.js

export const ADD_TODO = "ADD_TODO";
export const TOGGLE_TODO = "TOGGLE_TODO";
export const DELETE_TODO = "DELETE_TODO";

export const addTodo = (text) => ({
  type: ADD_TODO,
  payload: text,
});

export const toggleTodo = (id) => ({
  type: TOGGLE_TODO,
  payload: id,
});

export const deleteTodo = (id) => ({
  type: DELETE_TODO,
  payload: id,
});

import {
  ADD_TODO,
  TOGGLE_TODO,
  DELETE_TODO,
} from "../actions/todoActions";

const initialState = [];

const todoReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_TODO:
      return [
        ...state,
        {
          id: Date.now(),
          text: action.payload,
          completed: false,
        },
      ];

    case TOGGLE_TODO:
      return state.map((todo) =>
        todo.id === action.payload
          ? { ...todo, completed: !todo.completed }
          : todo
      );

    case DELETE_TODO:
      return state.filter(
        (todo) => todo.id !== action.payload
      );

    default:
      return state;
  }
};

export default todoReducer;

 import { combineReducers } from "redux";
import todoReducer from "./todoReducer";

export default combineReducers({
  todos: todoReducer,
});

import { createStore } from "redux";
import rootReducer from "./reducers";

const store = createStore(
  rootReducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ &&
    window.__REDUX_DEVTOOLS_EXTENSION__()
);

export default store;

import React, { useState } from "react";
import { connect } from "react-redux";
import { addTodo } from "../actions/todoActions";

function TodoForm({ addTodo }) {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!text.trim()) return;

    addTodo(text);
    setText("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter Todo"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button type="submit">
        Add Todo
      </button>
    </form>
  );
}

export default connect(
  null,
  { addTodo }
)(TodoForm);

import React from "react";
import { connect } from "react-redux";
import {
  toggleTodo,
  deleteTodo,
} from "../actions/todoActions";

function TodoItem({
  todo,
  toggleTodo,
  deleteTodo,
}) {
  return (
    <li>
      <span
        onClick={() => toggleTodo(todo.id)}
        style={{
          cursor: "pointer",
          textDecoration: todo.completed
            ? "line-through"
            : "none",
        }}
      >
        {todo.text}
      </span>

      <button
        onClick={() => deleteTodo(todo.id)}
      >
        Delete
      </button>
    </li>
  );
}

export default connect(
  null,
  { toggleTodo, deleteTodo }
)(TodoItem);

import React from "react";
import { connect } from "react-redux";
import TodoItem from "./TodoItem";

function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
        />
      ))}
    </ul>
  );
}

const mapStateToProps = (state) => ({
  todos: state.todos,
});

export default connect(
  mapStateToProps
)(TodoList);

import React from "react";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";

import App from "./App";
import store from "./store";

const root = ReactDOM.createRoot(
  document.getElementById("root")
);

root.render(
  <Provider store={store}>
    <App />
  </Provider>
);

