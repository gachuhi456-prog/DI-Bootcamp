exercise1:
import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../features/user/userSlice";

export const store = configureStore({
  reducer: {
    user: userReducer,
  },
});

export default store;

import { createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const initialState = {
  user: null,
  loading: false,
  error: null,
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    fetchUserStart: (state) => {
      state.loading = true;
      state.error = null;
    },

    fetchUserSuccess: (state, action) => {
      state.loading = false;
      state.user = action.payload;
    },

    fetchUserFailure: (state, action) => {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const {
  fetchUserStart,
  fetchUserSuccess,
  fetchUserFailure,
} = userSlice.actions;

export default userSlice.reducer;

export const fetchUser = () => async (dispatch) => {
  try {
    dispatch(fetchUserStart());

    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/users/1"
    );

    dispatch(fetchUserSuccess(response.data));
  } catch (error) {
    dispatch(fetchUserFailure("Failed to fetch user data"));
  }
};

import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchUser } from "../features/user/userSlice";

const UserData = () => {
  const dispatch = useDispatch();

  const { user, loading, error } = useSelector(
    (state) => state.user
  );

  return (
    <div style={{ padding: "20px" }}>
      <h2>User Information</h2>

      <button onClick={() => dispatch(fetchUser())}>
        Fetch User
      </button>

      {loading && <p>Loading...</p>}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {user && (
        <div>
          <h3>{user.name}</h3>
          <p>Email: {user.email}</p>
          <p>Username: {user.username}</p>
          <p>Phone: {user.phone}</p>
          <p>Website: {user.website}</p>
        </div>
      )}
    </div>
  );
};

export default UserData;

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

import React from "react";
import UserData from "./components/UserData";

function App() {
  return (
    <div>
      <h1>Redux Thunk User Fetch Example</h1>
      <UserData />
    </div>
  );
}

export default App;


