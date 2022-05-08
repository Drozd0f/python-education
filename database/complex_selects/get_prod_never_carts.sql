-- 1. Вывести продукты, которые ни разу не попадали в корзину.
SELECT product_title, product_description, in_stock, price, slug, category_id
FROM products
LEFT JOIN cart_product
ON products.product_id=cart_product.products_product_id
WHERE cart_product.products_product_id IS NULL;
