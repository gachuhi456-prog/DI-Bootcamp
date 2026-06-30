
const pool = require('../config/db');

const getAllPosts = async () => {
    const result = await pool.query('SELECT * FROM posts');
    return result.rows;
};

const getPostById = async (id) => {
    const result = await pool.query('SELECT * FROM posts WHERE id = $1', [id]);
    return result.rows[0];
};

const createPost = async (title, content) => {
    const result = await pool.query(
        'INSERT INTO posts (title, content) VALUES ($1, $2) RETURNING *',
        [title, content]
    );
    return result.rows[0];
};

const updatePost = async (id, title, content) => {
    const result = await pool.query(
        'UPDATE posts SET title = $1, content = $2 WHERE id = $3 RETURNING *',
        [title, content, id]
    );
    return result.rows[0];
};

const deletePost = async (id) => {
    await pool.query('DELETE FROM posts WHERE id = $1', [id]);
};

module.exports = { getAllPosts, getPostById, createPost, updatePost, deletePost };

const express = require('express');
const app = express();
app.use(express.json());

const postRoutes = require('./server/routes/postRoutes');
app.use('/posts', postRoutes);

// Error Handling
app.use((req, res) => res.status(404).send("Route not found"));

app.listen(3000, () => console.log('Blog API running on port 3000'));

app.get('/api/books', async (req, res) => {
    const result = await pool.query('SELECT * FROM books');
    res.status(200).json(result.rows);
});

app.get('/api/books/:bookId', async (req, res) => {
    const { bookId } = req.params;
    const result = await pool.query('SELECT * FROM books WHERE id = $1', [bookId]);
    
    if (result.rows.length > 0) {
        res.status(200).json(result.rows[0]);
    } else {
        res.status(404).json({ message: "Book not found" });
    }
});

app.post('/api/books', async (req, res) => {
    const { title, author, publishedYear } = req.body;
    const result = await pool.query(
        'INSERT INTO books (title, author, "publishedYear") VALUES ($1, $2, $3) RETURNING *',
        [title, author, publishedYear]
    );
    res.status(201).json(result.rows[0]);
});

