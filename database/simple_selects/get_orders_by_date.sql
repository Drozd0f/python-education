SELECT *
FROM orders
WHERE
    order_status_order_status_id = 4
  AND
    updated_at BETWEEN '2020-01-01' AND '2020-07-01';
