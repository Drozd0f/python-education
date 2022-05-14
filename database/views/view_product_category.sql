CREATE OR REPLACE VIEW get_product_with_category AS
SELECT product_title, product_description, in_stock, price, slug, category_title, category_description
FROM products
LEFT JOIN categories
ON products.category_id=categories.category_id;


SELECT *
FROM get_product_with_category
WHERE category_title ~ '\s4$';

SELECT *
FROM get_product_with_category
ORDER BY price DESC LIMIT 10;


SELECT *
FROM get_product_with_category
ORDER BY in_stock DESC LIMIT 10;

DROP VIEW IF EXISTS get_full_product_info;
