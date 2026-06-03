import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  isAuthenticated: false,
  user: null,
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    loginUser: (state, action) => {
      state.isAuthenticated = true;
      state.user = action.payload;
    },

    logoutUser: (state) => {
      state.isAuthenticated = false;
      state.user = null;
    },
  },
});

export const { loginUser, logoutUser } = authSlice.actions;

export default authSlice.reducer;

import { configureStore } from "@reduxjs/toolkit";
import authReducer from "../features/authSlice";

export const store = configureStore({
  reducer: {
    auth: authReducer,
  },
});
import { useState } from "react";
import { useDispatch } from "react-redux";
import { loginUser } from "../features/authSlice";

function Login() {
  const [username, setUsername] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();

    if (username.trim() === "") {
      alert("Please enter a username");
      return;
    }

    dispatch(
      loginUser({
        id: Date.now(),
        username,
      })
    );

    setUsername("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <button type="submit">Login</button>
    </form>
  );
}

export default Login;

import { useDispatch } from "react-redux";
import { logoutUser } from "../features/authSlice";

function Logout() {
  const dispatch = useDispatch();

  return (
    <button onClick={() => dispatch(logoutUser())}>
      Logout
    </button>
  );
}

export default Logout;

import { useSelector } from "react-redux";
import Logout from "./Logout";

function Dashboard() {
  const user = useSelector((state) => state.auth.user);

  return (
    <div>
      <h2>Dashboard</h2>

      <p>
        Welcome <strong>{user?.username}</strong>
      </p>

      <Logout />
    </div>
  );
}

export default Dashboard;


import { useSelector } from "react-redux";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";
import "./App.css";

function App() {
  const isAuthenticated = useSelector(
    (state) => state.auth.isAuthenticated
  );

  return (
    <div className="container">
      <h1>User Authentication App</h1>

      {isAuthenticated ? <Dashboard /> : <Login />}
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
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
}

.container {
  max-width: 500px;
  margin: 50px auto;
  padding: 20px;
  background: white;
  border-radius: 10px;
  text-align: center;
}

input {
  padding: 10px;
  width: 70%;
  margin-right: 10px;
}

button {
  padding: 10px 15px;
  cursor: pointer;
}

