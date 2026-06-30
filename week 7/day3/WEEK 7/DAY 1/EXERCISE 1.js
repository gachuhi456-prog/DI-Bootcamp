const express = require('express');
const app = express();

const indexRouter = require('./routes/index');

app.use('/', indexRouter);

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.send('Welcome to the Homepage');
});

  todo.task = req.body.task;
  res.json(todo);
});

// DELETE todo
router.delete('/:id', (req, res) => {
  todos = todos.filter(t => t.id != req.params.id);
  res.send('Todo deleted');
});

module.exports = router;

const express = require('express');
const app = express();

app.use(express.json());

const booksRouter = require('./routes/books');

app.use('/books', booksRouter);

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

const express = require('express');
const router = express.Router();

let books = [];
let id = 1;

// GET all books
router.get('/', (req, res) => {
  res.json(books);
});

// CREATE book
router.post('/', (req, res) => {
  const book = {
    id: id++,
    title: req.body.title,
    author: req.body.author
  };
  books.push(book);
  res.json(book);
});

// UPDATE book
router.put('/:id', (req, res) => {
  const book = books.find(b => b.id == req.params.id);
  if (!book) return res.status(404).send('Book not found');

  book.title = req.body.title;
  book.author = req.body.author;

  res.json(book);
});

// DELETE book
router.delete('/:id', (req, res) => {
  books = books.filter(b => b.id != req.params.id);
  res.send('Book deleted');
});

module.exports = router;

