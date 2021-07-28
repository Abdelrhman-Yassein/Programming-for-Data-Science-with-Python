/*query1- query used for second insight*/
SELECT
  f.title AS film_title,
  ct.name AS category_name,
  f.rental_duration,
  NTILE(4) OVER (ORDER BY f.title) AS standard_quartile
FROM category ct
JOIN film_category fc
  ON ct.category_id = fc.category_id
JOIN film f
  ON fc.film_id = f.film_id
WHERE ct.name IN ('Animation', 'Children'
, 'Classics', 'Comedy',
'Family ', 'Music')
ORDER BY f.title