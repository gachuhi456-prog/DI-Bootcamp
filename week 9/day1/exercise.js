exercise


export const REGISTER_SUCCESS = "REGISTER_SUCCESS";
export const LOGIN_SUCCESS = "LOGIN_SUCCESS";
export const LOGIN_FAIL = "LOGIN_FAIL";
export const LOGOUT = "LOGOUT";

export const register = (userData) => {
  return {
    type: REGISTER_SUCCESS,
    payload: userData,
  };
};

export const login = (email, password) => {
  const storedUser = JSON.parse(
    localStorage.getItem("user")
  );

  if (
    storedUser &&
    storedUser.email === email &&
    storedUser.password === password
  ) {
    return {
      type: LOGIN_SUCCESS,
      payload: storedUser,
    };
  }

  return {
    type: LOGIN_FAIL,
  };
};

export const logout = () => ({
  type: LOGOUT,
});

export const ADD_TODO = "ADD_TODO";
export const DELETE_TODO = "DELETE_TODO";
export const TOGGLE_TODO = "TOGGLE_TODO";

export const addTodo = (text) => ({
  type: ADD_TODO,
  payload: text,
});

export const deleteTodo = (id) => ({
  type: DELETE_TODO,
  payload: id,
});

export const toggleTodo = (id) => ({
  type: TOGGLE_TODO,
  payload: id,
});

import {
  REGISTER_SUCCESS,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
} from "../actions/authActions";

const initialState = {
  isAuthenticated: false,
  user: null,
  error: null,
};

const authReducer = (
  state = initialState,
  action
) => {
  switch (action.type) {
    case REGISTER_SUCCESS:
      localStorage.setItem(
        "user",
        JSON.stringify(action.payload)
      );

      return {
        ...state,
      };

    case LOGIN_SUCCESS:
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload,
        error: null,
      };

    case LOGIN_FAIL:
      return {
        ...state,
        error: "Invalid Credentials",
      };

    case LOGOUT:
      return {
        ...state,
        isAuthenticated: false,
        user: null,
      };

    default:
      return state;
  }
};

export default authReducer;
import {
  REGISTER_SUCCESS,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
} from "../actions/authActions";

const initialState = {
  isAuthenticated: false,
  user: null,
  error: null,
};

const authReducer = (
  state = initialState,
  action
) => {
  switch (action.type) {
    case REGISTER_SUCCESS:
      localStorage.setItem(
        "user",
        JSON.stringify(action.payload)
      );

      return {
        ...state,
      };

    case LOGIN_SUCCESS:
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload,
        error: null,
      };

    case LOGIN_FAIL:
      return {
        ...state,
        error: "Invalid Credentials",
      };

    case LOGOUT:
      return {
        ...state,
        isAuthenticated: false,
        user: null,
      };

    default:
      return state;
  }
};

export default authReducer;

import {
  ADD_TODO,
  DELETE_TODO,
  TOGGLE_TODO,
} from "../actions/todoActions";

const initialState = [];

const todoReducer = (
  state = initialState,
  action
) => {
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

    case DELETE_TODO:
      return state.filter(
        (todo) => todo.id !== action.payload
      );

    case TOGGLE_TODO:
      return state.map((todo) =>
        todo.id === action.payload
          ? {
              ...todo,
              completed: !todo.completed,
            }
          : todo
      );

    default:
      return state;
  }
};

export default todoReducer;

import { combineReducers } from "redux";
import authReducer from "./authReducer";
import todoReducer from "./todoReducer";

export default combineReducers({
  auth: authReducer,
  todos: todoReducer,
});

import React, { useState } from "react";
import { connect } from "react-redux";
import { register } from "../actions/authActions";

function Register({ register }) {
  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    register(form);

    alert("Registration Successful");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>

      <input
        placeholder="Email"
        onChange={(e) =>
          setForm({
            ...form,
            email: e.target.value,
          })
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setForm({
            ...form,
            password: e.target.value,
          })
        }
      />

      <button>Register</button>
    </form>
  );
}

export default connect(
  null,
  { register }
)(Register);

import React, { useState } from "react";
import { connect } from "react-redux";
import { login } from "../actions/authActions";

function Login({
  login,
  error,
}) {
  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const submitHandler = (e) => {
    e.preventDefault();
    login(email, password);
  };

  return (
    <form onSubmit={submitHandler}>
      <h2>Login</h2>

      <input
        placeholder="Email"
        onChange={(e) =>
          setEmail(e.target.value)
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <button>Login</button>

      {error && <p>{error}</p>}
    </form>
  );
}

const mapStateToProps = (
  state
) => ({
  error: state.auth.error,
});

export default connect(
  mapStateToProps,
  { login }
)(Login);

import React from "react";
import { connect } from "react-redux";
import { logout } from "../actions/authActions";

function Logout({
  logout,
}) {
  return (
    <button onClick={logout}>
      Logout
    </button>
  );
}

export default connect(
  null,
  { logout }
)(Logout);

import React, {
  useState,
} from "react";
import { connect } from "react-redux";
import { addTodo } from "../actions/todoActions";

function TodoForm({
  addTodo,
}) {
  const [text, setText] =
    useState("");

  const submitHandler = (e) => {
    e.preventDefault();

    if (!text.trim()) return;

    addTodo(text);

    setText("");
  };

  return (
    <form onSubmit={submitHandler}>
      <input
        value={text}
        onChange={(e) =>
          setText(e.target.value)
        }
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
  deleteTodo,
  toggleTodo,
} from "../actions/todoActions";

function TodoList({
  todos,
  deleteTodo,
  toggleTodo,
}) {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id}>
          <span
            onClick={() =>
              toggleTodo(todo.id)
            }
            style={{
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
              deleteTodo(todo.id)
            }
          >
            Delete
          </button>
        </li>
      ))}
    </ul>
  );
}

const mapStateToProps = (
  state
) => ({
  todos: state.todos,
});

export default connect(
  mapStateToProps,
  {
    deleteTodo,
    toggleTodo,
  }
)(TodoList);

import React from "react";
import { connect } from "react-redux";

import Login from "./components/Login";
import Register from "./components/Register";
import Logout from "./components/Logout";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";

function App({
  isAuthenticated,
}) {
  if (!isAuthenticated) {
    return (
      <>
        <Register />
        <Login />
      </>
    );
  }

  return (
    <div>
      <h1>Todo Dashboard</h1>

      <Logout />

      <TodoForm />

      <TodoList />
    </div>
  );
}

const mapStateToProps = (
  state
) => ({
  isAuthenticated:
    state.auth.isAuthenticated,
});

export default connect(
  mapStateToProps
)(App);

import React from "react";
import { connect } from "react-redux";

import Login from "./components/Login";
import Register from "./components/Register";
import Logout from "./components/Logout";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";

function App({
  isAuthenticated,
}) {
  if (!isAuthenticated) {
    return (
      <>
        <Register />
        <Login />
      </>
    );
  }

  return (
    <div>
      <h1>Todo Dashboard</h1>

      <Logout />

      <TodoForm />

      <TodoList />
    </div>
  );
}

const mapStateToProps = (
  state
) => ({
  isAuthenticated:
    state.auth.isAuthenticated,
});

export default connect(
  mapStateToProps
)(App);

import React from "react";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";

import App from "./App";
import store from "./store";

const root =
  ReactDOM.createRoot(
    document.getElementById("root")
  );

root.render(
  <Provider store={store}>
    <App />
  </Provider>
);