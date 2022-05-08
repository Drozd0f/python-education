-- 4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.
SELECT product_title, product_description, in_stock, price, slug, category_id, count(products_product_id)
FROM products, cart_product
LEFT JOIN orders
ON cart_product.carts_cart_id=orders.carts_cart_id
WHERE products.product_id=cart_product.products_product_id AND order_status_order_status_id > 1
GROUP BY product_title, product_description, in_stock, price, slug, category_id
ORDER BY count(products_product_id) DESC LIMIT 10;
