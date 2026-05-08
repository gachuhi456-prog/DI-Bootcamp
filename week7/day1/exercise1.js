exercise1

mkdir blog-api
cd blog-api
npm init -y
npm install express

const express = require('express');
const app = express();
const PORT = 3000;

// Middleware to parse JSON
app.use(express.json());

// In-memory "database"
let posts = [];
let currentId = 1;

// Router
const router = express.Router();

/**
 * GET /posts - Get all posts
 */
router.get('/posts', (req, res) => {
    res.json(posts);
});

/**
 * GET /posts/:id - Get post by ID
 */
router.get('/posts/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const post = posts.find(p => p.id === id);

    if (!post) {
        return res.status(404).json({ message: 'Post not found' });
    }

    res.json(post);
});

/**
 * POST /posts - Create a new post
 */
router.post('/posts', (req, res) => {
    const { title, content } = req.body;

    // Validation
    if (!title || !content) {
        return res.status(400).json({ message: 'Title and content are required' });
    }

    const newPost = {
        id: currentId++,
        title,
        content,
        timestamp: new Date()
    };

    posts.push(newPost);

    res.status(201).json(newPost);
});

/**
 * PUT /posts/:id - Update a post
 */
router.put('/posts/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const { title, content } = req.body;

    const post = posts.find(p => p.id === id);

    if (!post) {
        return res.status(404).json({ message: 'Post not found' });
    }

    if (!title || !content) {
        return res.status(400).json({ message: 'Title and content are required' });
    }

    post.title = title;
    post.content = content;

    res.json(post);
});

/**
 * DELETE /posts/:id - Delete a post
 */
router.delete('/posts/:id', (req, res) => {
    const id = parseInt(req.params.id);

    const index = posts.findIndex(p => p.id === id);

    if (index === -1) {
        return res.status(404).json({ message: 'Post not found' });
    }

    const deletedPost = posts.splice(index, 1);

    res.json({ message: 'Post deleted', post: deletedPost[0] });
});

// Use router
app.use('/api', router);

// Start server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});

node app.js

POST http://localhost:3000/api/posts
Body (JSON):
{
  "title": "My First Post",
  "content": "Hello world!"
}

GET http://localhost:3000/api/posts


PUT http://localhost:3000/api/posts/1
Body:
{
  "title": "Updated Title",
  "content": "Updated content"
}

DELETE http://localhost:3000/api/posts/1
