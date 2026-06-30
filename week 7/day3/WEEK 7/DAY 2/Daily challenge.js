

const knex = require('knex')({
  client: 'sqlite3',
  connection: { filename: './user_db.sqlite' },
  useNullAsDefault: true
});

const initDB = async () => {
  if (!(await knex.schema.hasTable('users'))) {
    await knex.schema.createTable('users', (table) => {
      table.increments('id').primary();
      table.string('email').unique();
      table.string('username').unique();
      table.string('first_name');
      table.string('last_name');
    });
  }
  if (!(await knex.schema.hasTable('hashpwd'))) {
    await knex.schema.createTable('hashpwd', (table) => {
      table.increments('id').primary();
      table.string('username').unique().references('users.username');
      table.string('password').notNullable();
    });
  }
};

initDB();
module.exports = knex;

const db = require('../config/db');

const registerUser = async (userData, hashedPassword) => {
  return await db.transaction(async (trx) => {
    await trx('users').insert({
      email: userData.email,
      username: userData.username,
      first_name: userData.first_name,
      last_name: userData.last_name
    });

    await trx('hashpwd').insert({
      username: userData.username,
      password: hashedPassword
    });
  });
};

const getAllUsers = () => db('users').select('*');
const getUserById = (id) => db('users').where({ id }).first();
const getHashByUsername = (username) => db('hashpwd').where({ username }).first();
const updateUser = (id, data) => db('users').where({ id }).update(data);

module.exports = { registerUser, getAllUsers, getUserById, getHashByUsername, updateUser };

const bcrypt = require('bcrypt');
const userModel = require('../models/userModel');

exports.register = async (req, res) => {
  try {
    const { username, password, email, first_name, last_name } = req.body;
    const hash = await bcrypt.hash(password, 10);
    await userModel.registerUser({ username, email, first_name, last_name }, hash);
    res.status(201).json({ message: "User registered successfully" });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.login = async (req, res) => {
  try {
    const { username, password } = req.body;
    const userRecord = await userModel.getHashByUsername(username);
    if (userRecord && await bcrypt.compare(password, userRecord.password)) {
      res.json({ message: "Login successful" });
    } else {
      res.status(401).json({ message: "Invalid credentials" });
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.getUsers = async (req, res) => {
  const users = await userModel.getAllUsers();
  res.json(users);
};

exports.getUserById = async (req, res) => {
  const user = await userModel.getUserById(req.params.id);
  user ? res.json(user) : res.status(404).json({ message: "Not found" });
};

exports.updateUser = async (req, res) => {
  await userModel.updateUser(req.params.id, req.body);
  res.json({ message: "User updated" });
};

const express = require('express');
const router = express.Router();
const userCtrl = require('../controllers/userController');

router.post('/register', userCtrl.register);
router.post('/login', userCtrl.login);
router.get('/users', userCtrl.getUsers);
router.get('/users/:id', userCtrl.getUserById);
router.put('/users/:id', userCtrl.updateUser);

module.exports = router

const express = require('express');
const userRoutes = require('./routes/userRoutes');

const app = express();
app.use(express.json());

app.use('/', userRoutes);

app.listen(3000, () => console.log('Server running on http://localhost:3000'));