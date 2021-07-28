/*query1- query used for the Fifth insight*/
SELECT
  pay_mon,
  full_name,
  pay_amount,
  pay_countpermon
FROM (SELECT
  date_trunc('month', payment_date) AS pay_mon,
  concat(c.first_name, ' ', c.last_name) AS full_name,
  SUM(py.amount) OVER (PARTITION BY r.customer_id) AS pay_amount,
  COUNT (py.*) OVER (PARTITION BY r.customer_id) AS pay_countpermon
FROM customer c
JOIN rental r
  ON r.customer_id = c.customer_id
JOIN payment py
  ON py.rental_id = r.rental_id
ORDER BY pay_amount DESC) sub
GROUP BY 1,
         2,
         3,
         4
ORDER BY pay_amount DESC
LIMIT 10