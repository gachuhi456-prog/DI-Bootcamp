exercise3
import { configureStore } from "@reduxjs/toolkit";

import authReducer from "./features/auth/authSlice";
import productReducer from "./features/products/productSlice";
import cartReducer from "./features/cart/cartSlice";

const store = configureStore({
  reducer: {
    auth: authReducer,
    products: productReducer,
    cart: cartReducer,
  },
});

export default store;

import { configureStore } from "@reduxjs/toolkit";

import authReducer from "./features/auth/authSlice";
import productReducer from "./features/products/productSlice";
import cartReducer from "./features/cart/cartSlice";

export const store = configureStore({
  reducer: {
    auth: authReducer,
    products: productReducer,
    cart: cartReducer,
  },
});


import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  products: [],
  loading: false,
  error: null,
};

const productSlice = createSlice({
  name: "products",

  initialState,

  reducers: {
    fetchProductsStart: (state) => {
      state.loading = true;
      state.error = null;
    },

    fetchProductsSuccess: (
      state,
      action
    ) => {
      state.loading = false;
      state.products = action.payload;
    },

    fetchProductsFailure: (
      state,
      action
    ) => {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const {
  fetchProductsStart,
  fetchProductsSuccess,
  fetchProductsFailure,
} = productSlice.actions;

export default productSlice.reducer;

import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  cartItems: [],
  totalAmount: 0,
};

const calculateTotal = (items) => {
  return items.reduce(
    (total, item) =>
      total +
      item.price * item.quantity,
    0
  );
};

const cartSlice = createSlice({
  name: "cart",

  initialState,

  reducers: {
    addToCart: (state, action) => {
      const item =
        state.cartItems.find(
          (product) =>
            product.id ===
            action.payload.id
        );

      if (item) {
        item.quantity += 1;
      } else {
        state.cartItems.push({
          ...action.payload,
          quantity: 1,
        });
      }

      state.totalAmount =
        calculateTotal(
          state.cartItems
        );
    },

    removeFromCart: (
      state,
      action
    ) => {
      state.cartItems =
        state.cartItems.filter(
          (item) =>
            item.id !==
            action.payload
        );

      state.totalAmount =
        calculateTotal(
          state.cartItems
        );
    },

    increaseQuantity: (
      state,
      action
    ) => {
      const item =
        state.cartItems.find(
          (item) =>
            item.id ===
            action.payload
        );

      if (item) {
        item.quantity += 1;
      }

      state.totalAmount =
        calculateTotal(
          state.cartItems
        );
    },

    decreaseQuantity: (
      state,
      action
    ) => {
      const item =
        state.cartItems.find(
          (item) =>
            item.id ===
            action.payload
        );

      if (
        item &&
        item.quantity > 1
      ) {
        item.quantity -= 1;
      }

      state.totalAmount =
        calculateTotal(
          state.cartItems
        );
    },
  },
});

export const {
  addToCart,
  removeFromCart,
  increaseQuantity,
  decreaseQuantity,
} = cartSlice.actions;

export default cartSlice.reducer;

import React, {
  useState,
} from "react";

import {
  useDispatch,
  useSelector,
} from "react-redux";

import {
  loginUser,
} from "../features/auth/authThunks";

import {
  logout,
} from "../features/auth/authSlice";

function AuthForm() {
  const [username,
    setUsername] =
    useState("");

  const dispatch =
    useDispatch();

  const {
    isAuthenticated,
    user,
    loading,
  } = useSelector(
    (state) =>
      state.auth
  );

  return (
    <div>
      {!isAuthenticated ? (
        <>
          <input
            type="text"
            placeholder="Username"
            value={
              username
            }
            onChange={(e) =>
              setUsername(
                e.target
                  .value
              )
            }
          />

          <button
            onClick={() =>
              dispatch(
                loginUser(
                  username
                )
              )
            }
          >
            Login
          </button>

          {loading && (
            <p>
              Logging in...
            </p>
          )}
        </>
      ) : (
        <>
          <h3>
            Welcome{" "}
            {
              user.username
            }
          </h3>

          <button
            onClick={() =>
              dispatch(
                logout()
              )
            }
          >
            Logout
          </button>
        </>
      )}
    </div>
  );
}

export default AuthForm;

import React, {
  useEffect,
} from "react";

import {
  useDispatch,
  useSelector,
} from "react-redux";

import {
  fetchProducts,
} from "../features/products/productThunks";

import {
  addToCart,
} from "../features/cart/cartSlice";

function ProductListing() {
  const dispatch =
    useDispatch();

  const {
    products,
    loading,
    error,
  } = useSelector(
    (state) =>
      state.products
  );

  useEffect(() => {
    dispatch(
      fetchProducts()
    );
  }, [dispatch]);

  if (loading)
    return (
      <h2>
        Loading Products...
      </h2>
    );

  if (error)
    return <h2>{error}</h2>;

  return (
    <div>
      <h2>Products</h2>

      {products.map(
        (product) => (
          <div
            key={
              product.id
            }
            style={{
              border:
                "1px solid #ccc",
              padding:
                "10px",
              margin:
                "10px",
            }}
          >
            <h4>
              {
                product.title
              }
            </h4>

            <p>
              $
              {
                product.price
              }
            </p>

            <button
              onClick={() =>
                dispatch(
                  addToCart(
                    product
                  )
                )
              }
            >
              Add To Cart
            </button>
          </div>
        )
      )}
    </div>
  );
}

export default ProductListing;

import React from "react";

import {
  useDispatch,
  useSelector,
} from "react-redux";

import {
  removeFromCart,
  increaseQuantity,
  decreaseQuantity,
} from "../features/cart/cartSlice";

function ShoppingCart() {
  const dispatch =
    useDispatch();

  const {
    cartItems,
    totalAmount,
  } = useSelector(
    (state) =>
      state.cart
  );

  return (
    <div>
      <h2>
        Shopping Cart
      </h2>

      {cartItems.length ===
        0 && (
        <p>
          Cart is empty
        </p>
      )}

      {cartItems.map(
        (item) => (
          <div
            key={item.id}
          >
            <h4>
              {
                item.title
              }
            </h4>

            <p>
              Qty:
              {
                item.quantity
              }
            </p>

            <button
              onClick={() =>
                dispatch(
                  increaseQuantity(
                    item.id
                  )
                )
              }
            >
              +
            </button>

            <button
              onClick={() =>
                dispatch(
                  decreaseQuantity(
                    item.id
                  )
                )
              }
            >
              -
            </button>

            <button
              onClick={() =>
                dispatch(
                  removeFromCart(
                    item.id
                  )
                )
              }
            >
              Remove
            </button>
          </div>
        )
      )}

      <h3>
        Total: $
        {totalAmount.toFixed(
          2
        )}
      </h3>
    </div>
  );
}

export default ShoppingCart;


import React from "react";

import AuthForm from "./components/AuthForm";
import ProductListing from "./components/ProductListing";
import ShoppingCart from "./components/ShoppingCart";

function App() {
  return (
    <div
      style={{
        padding: "20px",
      }}
    >
      <h1>
        Simulated E-Commerce Platform
      </h1>

      <AuthForm />

      <hr />

      <ProductListing />

      <hr />

      <ShoppingCart />
    </div>
  );
}

export default App;

import React from "react";
import ReactDOM from "react-dom/client";

import { Provider } from "react-redux";

import store from "./store";
import App from "./App";

const root =
  ReactDOM.createRoot(
    document.getElementById(
      "root"
    )
  );

root.render(
  <Provider store={store}>
    <App />
  </Provider>
);