SELECT
    category_title,
    product_title,
    price,
    avg(price) OVER (
        PARTITION BY products.category_id
    )
FROM products
LEFT JOIN categories
ON products.category_id = categories.category_id;
