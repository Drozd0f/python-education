-- 5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).
SELECT email, first_name, last_name, middle_name, sum(orders.total)
FROM users, carts
LEFT JOIN orders
ON carts.cart_id=orders.carts_cart_id
WHERE
    orders.carts_cart_id IS NOT NULL
  AND
    users.user_id=carts.users_user_id
GROUP BY email, first_name, last_name, middle_name
ORDER BY sum(orders.total) DESC LIMIT 5;
