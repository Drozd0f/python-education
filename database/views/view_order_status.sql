CREATE OR REPLACE VIEW get_order_in_progress AS
SELECT *
FROM orders
WHERE order_status_order_status_id=2;


SELECT *
FROM get_order_in_progress
ORDER BY total LIMIT 5;


SELECT *
FROM get_order_in_progress
ORDER BY total LIMIT 5;

SELECT *
FROM get_order_in_progress
WHERE created_at >= '2020-10-01'
ORDER BY total LIMIT 5;


SELECT *
FROM get_order_in_progress
WHERE shipping_total != 60;


DROP VIEW IF EXISTS get_full_product_info;
