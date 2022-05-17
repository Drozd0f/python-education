CREATE OR REPLACE PROCEDURE create_cart(
    user_id int, products_title varchar[]
)
language plpgsql
AS $$
DECLARE
    new_cart_id int;
    prod_id int;
    prod_title varchar;
    product_price numeric;
    total_price numeric := 0;
BEGIN
    -- Create with new id
    SELECT count(cart_id) + 1
    INTO new_cart_id
    FROM carts;

    INSERT INTO carts(cart_id, users_user_id)
    VALUES (new_cart_id, user_id);
    -- End create

    -- Counting total price by name product
    foreach prod_title in array products_title
    loop
        SELECT price, product_id
        INTO product_price, prod_id
        FROM products
        WHERE products.product_title = prod_title;
        -- If not found product cancel create cart
        if not found then
            ROLLBACK;
        end if;
        total_price := total_price + product_price;
        -- Create link in intermediate table
        INSERT INTO cart_product(carts_cart_id, products_product_id) VALUES (new_cart_id, prod_id);
    end loop;
    -- End counting

    -- If total_price > 0 then create carts else cancel create cart
    if total_price > 0 then
        UPDATE carts SET subtotal=total_price, total=total_price WHERE cart_id=new_cart_id;
        COMMIT;
    else
        ROLLBACK;
    end if;

END $$;


SELECT *
FROM products
ORDER BY product_id LIMIT 5;


SELECT *
FROM carts
ORDER BY cart_id DESC LIMIT 10;


DROP procedure if exists create_cart(user_id int, products_title varchar[]);


call create_cart(1, '{"Product 1", "Product 2", "Product 3", "Product 4", "Product 5"}');

