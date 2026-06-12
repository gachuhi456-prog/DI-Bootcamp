exercise2:
npm install @reduxjs/toolkit react-redux axios

import { configureStore } from "@reduxjs/toolkit";
import todoReducer from "../features/todos/todoSlice";

export const store = configureStore({
  reducer: {
    todos: todoReducer,
  },
});

export default store;

import { createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const initialState = {
  todos: [],
  loading: false,
  error: null,
};

const todoSlice = createSlice({
  name: "todos",
  initialState,
  reducers: {
    addTodo: (state, action) => {
      state.todos.push({
        id: Date.now(),
        title: action.payload,
        completed: false,
      });
    },

    removeTodo: (state, action) => {
      state.todos = state.todos.filter(
        (todo) => todo.id !== action.payload
      );
    },

    toggleTodo: (state, action) => {
      const todo = state.todos.find(
        (todo) => todo.id === action.payload
      );

      if (todo) {
        todo.completed = !todo.completed;
      }
    },

    setTodos: (state, action) => {
      state.todos = action.payload;
    },

    setLoading: (state, action) => {
      state.loading = action.payload;
    },

    setError: (state, action) => {
      state.error = action.payload;
    },
  },
});

export const {
  addTodo,
  removeTodo,
  toggleTodo,
  setTodos,
  setLoading,
  setError,
} = todoSlice.actions;

export default todoSlice.reducer;

export const fetchTodos = () => async (dispatch) => {
  try {
    dispatch(setLoading(true));

    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos?_limit=10"
    );

    dispatch(setTodos(response.data));
  } catch (error) {
    dispatch(setError("Failed to fetch todos"));
  } finally {
    dispatch(setLoading(false));
  }
};

import { createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const initialState = {
  todos: [],
  loading: false,
  error: null,
};

const todoSlice = createSlice({
  name: "todos",
  initialState,
  reducers: {
    addTodo: (state, action) => {
      state.todos.push({
        id: Date.now(),
        title: action.payload,
        completed: false,
      });
    },

    removeTodo: (state, action) => {
      state.todos = state.todos.filter(
        (todo) => todo.id !== action.payload
      );
    },

    toggleTodo: (state, action) => {
      const todo = state.todos.find(
        (todo) => todo.id === action.payload
      );

      if (todo) {
        todo.completed = !todo.completed;
      }
    },

    setTodos: (state, action) => {
      state.todos = action.payload;
    },

    setLoading: (state, action) => {
      state.loading = action.payload;
    },

    setError: (state, action) => {
      state.error = action.payload;
    },
  },
});

export const {
  addTodo,
  removeTodo,
  toggleTodo,
  setTodos,
  setLoading,
  setError,
} = todoSlice.actions;

export const fetchTodos = () => async (dispatch) => {
  try {
    dispatch(setLoading(true));

    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos?_limit=10"
    );

    dispatch(setTodos(response.data));
  } catch (error) {
    dispatch(setError("Failed to fetch todos"));
  } finally {
    dispatch(setLoading(false));
  }
};

export default todoSlice.reducer;

import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addTodo } from "../features/todos/todoSlice";

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

export default AddTodo;

import React from "react";
import { useDispatch } from "react-redux";
import {
  toggleTodo,
  removeTodo,
} from "../features/todos/todoSlice";

function TodoItem({ todo }) {
  const dispatch = useDispatch();

  return (
    <li>
      <span
        style={{
          textDecoration: todo.completed
            ? "line-through"
            : "none",
          cursor: "pointer",
        }}
        onClick={() =>
          dispatch(toggleTodo(todo.id))
        }
      >
        {todo.title}
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

import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchTodos } from "../features/todos/todoSlice";
import TodoItem from "./TodoItem";

function TodoList() {
  const dispatch = useDispatch();

  const { todos, loading, error } = useSelector(
    (state) => state.todos
  );

  useEffect(() => {
    dispatch(fetchTodos());
  }, [dispatch]);

  if (loading) return <h3>Loading...</h3>;

  if (error) return <h3>{error}</h3>;

  return (
    <div>
      <button
        onClick={() => dispatch(fetchTodos())}
      >
        Fetch Todos
      </button>

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

function App() {
  return (
    <div style={{ padding: "20px" }}>
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
import store from "./app/store";

const root = ReactDOM.createRoot(
  document.getElementById("root")
);

root.render(
  <Provider store={store}>
    <App />
  </Provider>
);


