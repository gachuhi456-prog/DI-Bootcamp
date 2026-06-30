CREATE DATABASE blog_platform;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);

mkdir blog-api && cd blog-api
npm init -y
npm install express pg dotenv

const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
    user: 'your_user',
    host: 'localhost',
    database: 'blog_platform',
    password: 'your_password',
    port: 5432,
});

module.exports = pool;

const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
    user: 'your_user',
    host: 'localhost',
    database: 'blog_platform',
    password: 'your_password',
    port: 5432,
});

module.exports = pool;