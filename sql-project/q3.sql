/*query1- query used for the third insight*/
SELECT
  ct.name,
  NTILE(4) OVER (ORDER BY f.title) AS standard_quartile,
  COUNT (f.*) OVER (PARTITION BY fc.category_id) AS COUNT
FROM category ct
JOIN film_category fc
  ON ct.category_id = fc.category_id
JOIN film f
  ON fc.film_id = f.film_id
WHERE ct.name IN ('Animation', 'Children'
, 'Classics', 'Comedy',
'Family ', 'Music')
ORDER BY ct.name