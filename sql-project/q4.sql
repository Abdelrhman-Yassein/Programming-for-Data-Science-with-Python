/*query1- query used for the fourth insight*/
SELECT
  date_part('year', r.rental_date) AS rental_year,
  date_part('month', r.rental_date) AS rental_month,
  s.store_id store_id,
  COUNT (r.*) AS rental_count
FROM rental r
JOIN payment py
  ON r.rental_id = py.rental_id
JOIN staff sf
  ON py.staff_id = sf.staff_id
JOIN store s
  ON sf.store_id = s.store_id
GROUP BY 1,
         2,
         3