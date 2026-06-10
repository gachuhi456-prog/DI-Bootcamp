-- ============================================
-- Exercise 1: Items and Customers
-- ============================================

-- Drop tables if they already exist (prevents "relation already exists" error)
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS customers;

-- Create items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL
);

-- Create customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);

-- Insert items
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large desk', 300),
('Fan', 80);

-- Insert customers
INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

-- ============================================
-- FETCH DATA
-- ============================================

-- 1. All the items
SELECT * FROM items;

-- 2. All items with price above 80 (80 not included)
SELECT * FROM items WHERE price > 80;

-- 3. All items with price below 300 (300 included)
SELECT * FROM items WHERE price <= 300;

-- 4. All customers whose last name is 'Smith'
-- Outcome: No results (empty set) - no customer has last name 'Smith'
SELECT * FROM customers WHERE last_name = 'Smith';

-- 5. All customers whose last name is 'Jones'
SELECT * FROM customers WHERE last_name = 'Jones';

-- 6. All customers whose first name is not 'Scott'
SELECT * FROM customers WHERE first_name != 'Scott';