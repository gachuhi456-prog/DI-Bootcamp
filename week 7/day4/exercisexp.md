exercisexp
# Project Structure

```text
jwt-auth
│
├── app.js
├── .env
│
├── routes
│     └── authRoutes.js
│
├── middleware
│     └── authMiddleware.js
│
├── data
│     └── users.js
│
└── package.json
```

---

# Step 1: Initialize Project

```bash
npm init -y
```

Install Express:

```bash
npm install express --save
```

Install dependencies:

```bash
npm install jsonwebtoken bcrypt body-parser cookie-parser dotenv
```

---

# Step 2: Create .env

```env
JWT_SECRET=mySecretKey
REFRESH_SECRET=myRefreshSecretKey
PORT=5000
```

---

# Step 3: Create Users Table

## data/users.js

```js
const users = [];

module.exports = users;
```

---

# Step 4: Create Authentication Middleware

## middleware/authMiddleware.js

```js
const jwt = require("jsonwebtoken");

const verifyToken = (req, res, next) => {

    const token = req.cookies.token;

    if (!token) {
        return res.status(401).json({
            message: "Access denied"
        });
    }

    try {

        const decoded = jwt.verify(
            token,
            process.env.JWT_SECRET
        );

        req.user = decoded;

        next();

    } catch (err) {

        res.status(403).json({
            message: "Invalid token"
        });

    }

};

module.exports = verifyToken;
```

---

# Step 5: Create Routes

## routes/authRoutes.js

```js
const express = require("express");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

const users = require("../data/users");
const verifyToken = require("../middleware/authMiddleware");

const router = express.Router();

let refreshTokens = [];
```

---

# Register Endpoint

```js
router.post("/register", async (req, res) => {

    const { username, password } = req.body;

    if (!username || !password) {

        return res.status(400).json({
            message: "All fields are required"
        });

    }

    const userExists = users.find(
        user => user.username === username
    );

    if (userExists) {

        return res.status(400).json({
            message: "User already exists"
        });

    }

    const hashedPassword = await bcrypt.hash(
        password,
        10
    );

    const newUser = {
        id: Date.now(),
        username,
        password: hashedPassword
    };

    users.push(newUser);

    const accessToken = jwt.sign(
        {
            id: newUser.id,
            username: newUser.username
        },
        process.env.JWT_SECRET,
        {
            expiresIn: "1h"
        }
    );

    res.cookie("token", accessToken, {
        httpOnly: true
    });

    res.status(201).json({
        message: "Registration successful"
    });

});
```

---

# Login Endpoint

```js
router.post("/login", async (req, res) => {

    const { username, password } = req.body;

    const user = users.find(
        user => user.username === username
    );

    if (!user) {

        return res.status(404).json({
            message: "User not found"
        });

    }

    const validPassword = await bcrypt.compare(
        password,
        user.password
    );

    if (!validPassword) {

        return res.status(401).json({
            message: "Wrong password"
        });

    }

    const accessToken = jwt.sign(
        {
            id: user.id,
            username: user.username
        },
        process.env.JWT_SECRET,
        {
            expiresIn: "1h"
        }
    );

    const refreshToken = jwt.sign(
        {
            id: user.id,
            username: user.username
        },
        process.env.REFRESH_SECRET,
        {
            expiresIn: "7d"
        }
    );

    refreshTokens.push(refreshToken);

    res.cookie(
        "token",
        accessToken,
        {
            httpOnly: true
        }
    );

    res.cookie(
        "refreshToken",
        refreshToken,
        {
            httpOnly: true
        }
    );

    res.json({
        message: "Login successful"
    });

});
```

---

# Protected Route

```js
router.get(
    "/profile",
    verifyToken,
    (req, res) => {

        res.json({
            message: "Protected route",
            user: req.user
        });

    }
);
```

---

# Refresh Token Endpoint

```js
router.post("/refresh", (req, res) => {

    const refreshToken =
        req.cookies.refreshToken;

    if (!refreshToken) {
        return res.sendStatus(401);
    }

    if (!refreshTokens.includes(refreshToken)) {
        return res.sendStatus(403);
    }

    jwt.verify(
        refreshToken,
        process.env.REFRESH_SECRET,
        (err, user) => {

            if (err) {
                return res.sendStatus(403);
            }

            const accessToken = jwt.sign(
                {
                    id: user.id,
                    username: user.username
                },
                process.env.JWT_SECRET,
                {
                    expiresIn: "1h"
                }
            );

            res.cookie(
                "token",
                accessToken,
                {
                    httpOnly: true
                }
            );

            res.json({
                accessToken
            });

        }
    );

});
```

---

# Logout Endpoint

```js
router.post("/logout", (req, res) => {

    const refreshToken =
        req.cookies.refreshToken;

    refreshTokens = refreshTokens.filter(
        token => token !== refreshToken
    );

    res.clearCookie("token");

    res.clearCookie("refreshToken");

    res.json({
        message: "Logged out successfully"
    });

});
```

---

# Export Router

```js
module.exports = router;
```

---

# Step 6: Create app.js

```js
require("dotenv").config();

const express = require("express");
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");

const authRoutes =
    require("./routes/authRoutes");

const app = express();

app.use(bodyParser.json());

app.use(cookieParser());

app.use(
    "/api/auth",
    authRoutes
);

app.get("/", (req, res) => {

    res.send(
        "JWT Authentication API"
    );

});

const PORT =
    process.env.PORT || 5000;

app.listen(PORT, () => {

    console.log(
        `Server running on port ${PORT}`
    );

});
```

---

# Endpoints

### Register

```http
POST /api/auth/register
```

Body:

```json
{
    "username": "alex",
    "password": "123456"
}
```

---

### Login

```http
POST /api/auth/login
```

Body:

```json
{
    "username": "alex",
    "password": "123456"
}
```

---

### Protected Route

```http
GET /api/auth/profile
```

---

### Refresh Token

```http
POST /api/auth/refresh
```

---

### Logout

```http
POST /api/auth/logout
```

---

# Improvements

You can further enhance the project by adding:

* Username and password validation.
* Update profile route.
* Token revocation.
* MongoDB or PostgreSQL database.
* Email verification.
* Rate limiting using `express-rate-limit`.
* Role-based authorization.
* Refresh token rotation.

# Key Takeaways

✅ Password hashing with bcrypt.

✅ Access tokens and refresh tokens.

✅ Protected routes using middleware.

✅ HTTP-only cookies for security.

✅ Token verification with jsonwebtoken.

✅ Logout and token refresh support.

These are the core features used in production authentication systems.
