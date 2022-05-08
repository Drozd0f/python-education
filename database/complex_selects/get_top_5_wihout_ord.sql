-- 7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.
SELECT email, first_name, last_name, middle_name
FROM users, carts
LEFT JOIN orders
ON carts.cart_id=orders.carts_cart_id
WHERE
    users.user_id=carts.users_user_id
  AND
    (orders.order_id IS NULL OR orders.order_status_order_status_id = 1)
ORDER BY users.user_id LIMIT 5;
