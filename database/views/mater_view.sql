CREATE MATERIALIZED VIEW get_user_waiting_order AS
SELECT u.first_name, u.last_name, u.middle_name, o.total, os.status_name, o.updated_at
FROM users u
LEFT JOIN carts c ON u.user_id=c.users_user_id
LEFT JOIN orders o ON c.cart_id=o.carts_cart_id
LEFT JOIN order_status os ON o.order_status_order_status_id=os.order_status_id
WHERE os.order_status_id < 4;


SELECT first_name, middle_name, middle_name, sum(total)
FROM get_user_waiting_order
GROUP BY first_name, middle_name, middle_name
ORDER BY sum(total) DESC LIMIT 10;


DROP MATERIALIZED VIEW get_user_waiting_order;


