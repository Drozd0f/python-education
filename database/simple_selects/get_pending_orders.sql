SELECT *
FROM orders
WHERE
    order_status_order_status_id < 4
  AND
    updated_at <= '2020-12-31';
