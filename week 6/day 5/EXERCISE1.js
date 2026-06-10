EXERCISE1
mkdir blog-api
cd blog-api
npm init -y
npm install express

const express = require("express");

const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());

// Simulated database
let posts = [
  {
    id: 1,
    title: "First Post",
    content: "This is the first blog post."
  },
  {
    id: 2,
    title: "Second Post",
    content: "This is the second blog post."
  }
];

// GET all posts
app.get("/posts", (req, res) => {
  res.status(200).json(posts);
});

// GET one post
app.get("/posts/:id", (req, res) => {
  const id = parseInt(req.params.id);

  const post = posts.find(post => post.id === id);

  if (!post) {
    return res.status(404).json({
      message: "Post not found"
    });
  }

  res.status(200).json(post);
});

// CREATE a new post
app.post("/posts", (req, res) => {
  const { title, content } = req.body;

  const newPost = {
    id: posts.length + 1,
    title,
    content
  };

  posts.push(newPost);

  res.status(201).json({
    message: "Post created successfully",
    post: newPost
  });
});

// UPDATE a post
app.put("/posts/:id", (req, res) => {
  const id = parseInt(req.params.id);

  const post = posts.find(post => post.id === id);

  if (!post) {
    return res.status(404).json({
      message: "Post not found"
    });
  }

  post.title = req.body.title || post.title;
  post.content = req.body.content || post.content;

  res.status(200).json({
    message: "Post updated successfully",
    post
  });
});

// DELETE a post
app.delete("/posts/:id", (req, res) => {
  const id = parseInt(req.params.id);

  const index = posts.findIndex(post => post.id === id);

  if (index === -1) {
    return res.status(404).json({
      message: "Post not found"
    });
  }

  posts.splice(index, 1);

  res.status(200).json({
    message: "Post deleted successfully"
  });
});

// Invalid routes
app.use((req, res) => {
  res.status(404).json({
    message: "Route not found"
  });
});

// Server errors
app.use((err, req, res, next) => {
  console.error(err.stack);

  res.status(500).json({
    message: "Internal server error"
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

node server.js

mkdir crud-api
cd crud-api
npm init -y
npm install express axios

const axios = require("axios");

async function fetchPosts() {
  try {
    const response = await axios.get(
    "https://jsonplaceholder.typicode.com/posts"
    );

    return response.data;

  } catch (error) {
    throw error;
  }
}

module.exports = {
  fetchPosts
};

const express = require("express");
const { fetchPosts } = require("./data/dataService");

const app = express();
const PORT = 5000;

// Endpoint
app.get("/posts", async (req, res) => {
  try {
    const posts = await fetchPosts();

    console.log("Data successfully retrieved and sent.");

    res.status(200).json(posts);

  } catch (error) {
    console.error(error);

    res.status(500).json({
      message: "Failed to retrieve posts"
    });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

node app.js