-- 1. Создать функцию, которая сетит shipping_total = 0 в таблице order, если город юзера равен x (аргумент функции),
-- и возвращает сумму всех заказов для поля shipping_total.

CREATE OR REPLACE FUNCTION update_ship_total_by_city(
    name_city varchar,
    new_ship_total orders.shipping_total%type
)
returns numeric
language plpgsql
AS
$$
DECLARE
    temp_order record;
    sum_shipping_total numeric := 0;
BEGIN
    for temp_order in (
        SELECT o.order_id
        FROM users u
        LEFT JOIN carts c ON u.user_id=c.users_user_id
        LEFT JOIN orders o ON c.cart_id=o.carts_cart_id
        WHERE u.city LIKE name_city
    )
    loop
        sum_shipping_total := sum_shipping_total + new_ship_total;
        UPDATE orders
        SET shipping_total = new_ship_total
        WHERE order_id = temp_order.order_id;
    end loop;

    return sum_shipping_total;
END;
$$;


DROP FUNCTION IF EXISTS update_ship_total_by_city(name_city varchar, new_ship_total orders.shipping_total%type);


SELECT o.order_id, shipping_total
FROM users u
LEFT JOIN carts c ON u.user_id=c.users_user_id
LEFT JOIN orders o ON c.cart_id=o.carts_cart_id
WHERE u.city = 'city 6';


SELECT update_ship_total_by_city('city 6', 0);
