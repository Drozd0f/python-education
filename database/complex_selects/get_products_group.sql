SELECT product_title, count(product_title)
FROM products
GROUP BY product_title
ORDER BY count(product_title) DESC;
