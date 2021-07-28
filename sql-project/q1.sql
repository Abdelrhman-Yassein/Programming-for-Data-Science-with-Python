/*query1- query used for first insight*/

WITH t1
AS (SELECT
  f.title AS film_title,
  ct.name AS category_name
FROM category ct
JOIN film_category fc
  ON ct.category_id = fc.category_id
JOIN film f
  ON fc.film_id = f.film_id
WHERE ct.name IN ('Animation', 'Children'
, 'Classics', 'Comedy',
'Family ', 'Music')
ORDER BY ct.name),

t2
AS (SELECT
  f.title AS film_title,
  COUNT (r.*) AS rental_count
FROM rental r
JOIN inventory i
  ON r.inventory_id = i.inventory_id
JOIN film f
  ON f.film_id = i.film_id
GROUP BY f.title
ORDER BY rental_count DESC)

SELECT
  t1.film_title,
  t1.category_name,
  t2.rental_count
FROM t1
JOIN t2
  ON t1.film_title = t2.film_title
ORDER BY t1.category_name, t2.rental_count DESC