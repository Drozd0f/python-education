-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).
SELECT product_title, product_description, in_stock, price, slug, category_id
FROM products, cart_product
LEFT JOIN orders
ON cart_product.carts_cart_id=orders.carts_cart_id
WHERE
    products.product_id=cart_product.products_product_id
  AND
    (orders.carts_cart_id is NULL OR orders.order_status_order_status_id=1);
