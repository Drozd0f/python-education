SELECT max(total)
FROM orders
WHERE created_at BETWEEN '2020-07-01' AND '2020-10-01';
