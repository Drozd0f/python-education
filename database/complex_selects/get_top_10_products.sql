-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.
SELECT product_title, product_description, in_stock, price, slug, category_id, count(product_id)
FROM products
INNER JOIN cart_product
ON cart_product.products_product_id=products.product_id
GROUP BY product_title, product_description, in_stock, price, slug, category_id
ORDER BY count(product_id) DESC LIMIT 10;
