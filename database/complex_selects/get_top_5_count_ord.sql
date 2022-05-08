-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).
SELECT email, first_name, last_name, middle_name, count(order_id)
FROM users, carts
LEFT JOIN orders
ON carts.cart_id=orders.carts_cart_id
WHERE users.user_id=carts.users_user_id
GROUP BY email, first_name, last_name, middle_name
ORDER BY count(order_id) DESC LIMIT 5;
