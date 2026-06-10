exercise
SELECT *
FROM language;

SELECT
    film.title,
    film.description,
    language.name AS language_name
FROM film
INNER JOIN language
ON film.language_id = language.language_id;

SELECT
    film.title,
    film.description,
    language.name AS language_name
FROM language
LEFT JOIN film
ON language.language_id = film.language_id;
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
INSERT INTO new_film (name)
VALUES
('Inception'),
('Avatar'),
('Titanic');
INSERT INTO customer_review
(film_id, language_id, title, score, review_text)
VALUES
(1,1,'Amazing Movie',9,'Excellent story and visuals'),

(2,1,'Great Experience',8,'Very entertaining movie');

DELETE FROM new_film
WHERE id = 1;


UPDATE film
SET language_id = 2
WHERE film_id IN (1,2,3);
customer.address_id
→ address.address_id
DROP TABLE customer_review;
SELECT COUNT(*)
FROM rental
WHERE return_date IS NULL;

SELECT DISTINCT film.title
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE
film.description ILIKE '%sumo%'
AND actor.first_name = 'Penelope'
AND actor.last_name = 'Monroe';
