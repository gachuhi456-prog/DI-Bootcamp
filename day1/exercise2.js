exercise2
{
  todos: []
}

{
  categories: [
    {
      id: 1,
      name: "Work",
      todos: []
    },
    {
      id: 2,
      name: "Personal",
      todos: []
    }
  ]
}

export const ADD_TODO = "ADD_TODO";
export const TOGGLE_TODO = "TOGGLE_TODO";
export const DELETE_TODO = "DELETE_TODO";
export const ADD_CATEGORY = "ADD_CATEGORY";

export const addCategory = (name) => ({
  type: ADD_CATEGORY,
  payload: name,
});

export const addTodo = (categoryId, text) => ({
  type: ADD_TODO,
  payload: {
    categoryId,
    text,
  },
});

export const toggleTodo = (categoryId, todoId) => ({
  type: TOGGLE_TODO,
  payload: {
    categoryId,
    todoId,
  },
});

export const deleteTodo = (categoryId, todoId) => ({
  type: DELETE_TODO,
  payload: {
    categoryId,
    todoId,
  },
});

export const ADD_TODO = "ADD_TODO";
export const TOGGLE_TODO = "TOGGLE_TODO";
export const DELETE_TODO = "DELETE_TODO";
export const ADD_CATEGORY = "ADD_CATEGORY";

export const addCategory = (name) => ({
  type: ADD_CATEGORY,
  payload: name,
});

export const addTodo = (categoryId, text) => ({
  type: ADD_TODO,
  payload: {
    categoryId,
    text,
  },
});

export const toggleTodo = (categoryId, todoId) => ({
  type: TOGGLE_TODO,
  payload: {
    categoryId,
    todoId,
  },
});

export const deleteTodo = (categoryId, todoId) => ({
  type: DELETE_TODO,
  payload: {
    categoryId,
    todoId,
  },
});

import {
  ADD_CATEGORY,
  ADD_TODO,
  TOGGLE_TODO,
  DELETE_TODO,
} from "../actions/todoActions";

const initialState = [
  {
    id: 1,
    name: "Work",
    todos: [],
  },
  {
    id: 2,
    name: "Personal",
    todos: [],
  },
];

const categoryReducer = (
  state = initialState,
  action
) => {
  switch (action.type) {
    case ADD_CATEGORY:
      return [
        ...state,
        {
          id: Date.now(),
          name: action.payload,
          todos: [],
        },
      ];

    case ADD_TODO:
      return state.map((category) =>
        category.id === action.payload.categoryId
          ? {
              ...category,
              todos: [
                ...category.todos,
                {
                  id: Date.now(),
                  text: action.payload.text,
                  completed: false,
                },
              ],
            }
          : category
      );

    case TOGGLE_TODO:
      return state.map((category) =>
        category.id === action.payload.categoryId
          ? {
              ...category,
              todos: category.todos.map((todo) =>
                todo.id === action.payload.todoId
                  ? {
                      ...todo,
                      completed: !todo.completed,
                    }
                  : todo
              ),
            }
          : category
      );

    case DELETE_TODO:
      return state.map((category) =>
        category.id === action.payload.categoryId
          ? {
              ...category,
              todos: category.todos.filter(
                (todo) =>
                  todo.id !== action.payload.todoId
              ),
            }
          : category
      );

    default:
      return state;
  }
};

export default categoryReducer;

import { combineReducers } from "redux";
import categoryReducer from "./categoryReducer";

export default combineReducers({
  categories: categoryReducer,
});

import React, { useState } from "react";
import { connect } from "react-redux";
import { addCategory } from "../actions/todoActions";

function CategoryForm({ addCategory }) {
  const [name, setName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!name.trim()) return;

    addCategory(name);
    setName("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Category Name"
        value={name}
        onChange={(e) =>
          setName(e.target.value)
        }
      />

      <button>Add Category</button>
    </form>
  );
}

export default connect(
  null,
  { addCategory }
)(CategoryForm);
import React, { useState } from "react";
import { connect } from "react-redux";
import { addTodo } from "../actions/todoActions";

function TodoForm({
  categoryId,
  addTodo,
}) {
  const [text, setText] = useState("");

  const submitHandler = (e) => {
    e.preventDefault();

    if (!text.trim()) return;

    addTodo(categoryId, text);
    setText("");
  };

  return (
    <form onSubmit={submitHandler}>
      <input
        value={text}
        onChange={(e) =>
          setText(e.target.value)
        }
        placeholder="Add Todo"
      />

      <button>Add</button>
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
  categoryId,
  todo,
  toggleTodo,
  deleteTodo,
}) {
  return (
    <li>
      <span
        onClick={() =>
          toggleTodo(
            categoryId,
            todo.id
          )
        }
        style={{
          cursor: "pointer",
          textDecoration:
            todo.completed
              ? "line-through"
              : "none",
        }}
      >
        {todo.text}
      </span>

      <button
        onClick={() =>
          deleteTodo(
            categoryId,
            todo.id
          )
        }
      >
        Delete
      </button>
    </li>
  );
}

export default connect(
  null,
  {
    toggleTodo,
    deleteTodo,
  }
)(TodoItem);

import React from "react";
import { connect } from "react-redux";
import Category from "./Category";

function CategoryList({
  categories,
}) {
  return (
    <>
      {categories.map((category) => (
        <Category
          key={category.id}
          category={category}
        />
      ))}
    </>
  );
}

const mapStateToProps = (state) => ({
  categories: state.categories,
});

export default connect(
  mapStateToProps
)(CategoryList);

import React from "react";
import CategoryForm from "./components/CategoryForm";
import CategoryList from "./components/CategoryList";

function App() {
  return (
    <div
      style={{
        width: "80%",
        margin: "auto",
      }}
    >
      <h1>
        Todo List With Categories
      </h1>

      <CategoryForm />

      <CategoryList />
    </div>
  );
}

export default App;

