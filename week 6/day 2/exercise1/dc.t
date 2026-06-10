-- 1. Select all columns from the "customer" table
SELECT * FROM customer;

-- 2. Display names using alias "full_name"
SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- 3. All create_date from customer (no duplicates)
SELECT DISTINCT create_date FROM customer;

-- 4. All customer details in descending order by first name
SELECT * FROM customer ORDER BY first_name DESC;

-- 5. Film ID, title, description, release_year, rental_rate in ascending order by rental_rate
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;

-- 6. Address and phone of all customers in Texas district
SELECT address, phone FROM address WHERE district = 'Texas';

-- 7. Movie details where film_id is 15 or 150
SELECT * FROM film WHERE film_id IN (15, 150);

-- 8. Check if your favorite movie exists (replace 'INCEPTION' with your movie)
SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'INCEPTION';

-- 9. Movies starting with first 2 letters of your favorite movie (e.g., 'In')
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'In%';

-- 10. 10 cheapest movies
SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;

-- 11. Next 10 cheapest movies (without LIMIT - use OFFSET with FETCH)
SELECT * FROM film ORDER BY rental_rate ASC OFFSET 10 FETCH NEXT 10 ROWS ONLY;

-- 12. Join customer and payment tables
SELECT c.first_name, c.last_name, p.amount, p.payment_date FROM customer c JOIN payment p ON c.customer_id = p.customer_id ORDER BY c.customer_id ASC;

-- 13. Movies not in inventory
SELECT f.* FROM film f LEFT JOIN inventory i ON f.film_id = i.film_id WHERE i.film_id IS NULL;

-- 14. Which city is in which country
SELECT ci.city, co.country FROM city ci JOIN country co ON ci.country_id = co.country_id;

-- BONUS: Customer's id, names, amount, date of payment ordered by staff_id
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date FROM customer c JOIN payment p ON c.customer_id = p.customer_id ORDER BY p.staff_id ASC;