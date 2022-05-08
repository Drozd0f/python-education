SELECT carts.cart_id
FROM carts
LEFT JOIN orders
ON carts.cart_id=orders.order_id
WHERE orders.order_id IS NULL OR orders.order_status_order_status_id = 1;
