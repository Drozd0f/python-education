CREATE OR REPLACE VIEW get_products AS
SELECT product_title, product_description, in_stock, price, slug
FROM products;

SELECT * FROM get_products;

SELECT *
FROM get_products
WHERE in_stock=0;

SELECT *
FROM get_products
ORDER BY price DESC LIMIT 10;

DROP VIEW IF EXISTS get_products;
