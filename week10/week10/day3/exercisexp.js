exercisexp
npm init -y

npm install express jsonwebtoken bcrypt body-parser cookie-parser dotenv

JWT_SECRET=mySuperSecretKey
REFRESH_SECRET=myRefreshSecretKey
PORT=5000

const users = [];

module.exports = users;

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
  } catch (error) {
    res.status(403).json({
      message: "Invalid token"
    });
  }
};

module.exports = verifyToken;

const express = require("express");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

const users = require("../data/users");
const verifyToken = require("../middleware/authMiddleware");

const router = express.Router();

let refreshTokens = [];

router.post("/register", async (req, res) => {

  const { username, password } = req.body;

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
    { id: newUser.id, username },
    process.env.JWT_SECRET,
    {
      expiresIn: "1h"
    }
  );

  res.cookie("token", accessToken, {
    httpOnly: true
  });

  res.status(201).json({
    message: "Registration successful",
    accessToken
  });
});

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

  res.cookie("token", accessToken, {
    httpOnly: true
  });

  res.cookie("refreshToken", refreshToken, {
    httpOnly: true
  });

  res.json({
    message: "Login successful"
  });
});

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

      res.cookie("token", accessToken, {
        httpOnly: true
      });

      res.json({
        accessToken
      });

    }
  );

});

require("dotenv").config();

const express = require("express");
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");

const authRoutes = require("./routes/authRoutes");

const app = express();

app.use(bodyParser.json());

app.use(cookieParser());

app.use("/api/auth", authRoutes);

app.get("/", (req, res) => {
  res.send("JWT Authentication API");
});

const PORT =
  process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(
    `Server running on port ${PORT}`
  );
});

