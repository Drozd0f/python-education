-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).
ANALYZE products;
ANALYZE orders;
ANALYZE cart_product;

SET enable_seqscan TO off;
EXPLAIN (ANALYZE, BUFFERS) SELECT product_title, product_description, in_stock, price, slug, category_id
FROM products, cart_product
LEFT JOIN orders
ON cart_product.carts_cart_id=orders.carts_cart_id
WHERE
    products.product_id=cart_product.products_product_id
  AND
    (orders.carts_cart_id is NULL OR orders.order_status_order_status_id=1);
SET enable_seqscan TO on;

-- Without Index

-- Hash Join  (cost=241.75..550.40 rows=2052 width=64) (actual time=3.381..12.441 rows=4362 loops=1)
--   Hash Cond: (cart_product.products_product_id = products.product_id)
--   Buffers: shared hit=167
--   ->  Hash Left Join  (cost=46.75..350.01 rows=2052 width=4) (actual time=0.672..7.336 rows=4362 loops=1)
--         Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--         Filter: ((orders.carts_cart_id IS NULL) OR (orders.order_status_order_status_id = 1))
--         Rows Removed by Filter: 6633
--         Buffers: shared hit=62
--         ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.006..1.204 rows=10995 loops=1)
--               Buffers: shared hit=49
--         ->  Hash  (cost=28.00..28.00 rows=1500 width=8) (actual time=0.629..0.630 rows=1500 loops=1)
--               Buckets: 2048  Batches: 1  Memory Usage: 75kB
--               Buffers: shared hit=13
--               ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=8) (actual time=0.004..0.279 rows=1500 loops=1)
--                     Buffers: shared hit=13
--   ->  Hash  (cost=145.00..145.00 rows=4000 width=68) (actual time=2.700..2.700 rows=4000 loops=1)
--         Buckets: 4096  Batches: 1  Memory Usage: 458kB
--         Buffers: shared hit=105
--         ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=68) (actual time=0.027..1.154 rows=4000 loops=1)
--               Buffers: shared hit=105
-- Planning:
--   Buffers: shared hit=33
-- Planning Time: 0.394 ms
-- Execution Time: 12.786 ms


CREATE INDEX ON cart_product(carts_cart_id, products_product_id);
CREATE INDEX ON orders(carts_cart_id, order_status_order_status_id);

DROP INDEX IF EXISTS orders_carts_cart_id_order_status_order_status_id_idx;
DROP INDEX IF EXISTS cart_product_carts_cart_id_products_product_id_idx;

-- With Index With Seq Scan

-- Hash Join  (cost=241.75..550.40 rows=2052 width=64) (actual time=8.023..26.511 rows=4362 loops=1)
--   Hash Cond: (cart_product.products_product_id = products.product_id)
--   Buffers: shared hit=167
--   ->  Hash Left Join  (cost=46.75..350.01 rows=2052 width=4) (actual time=1.624..15.851 rows=4362 loops=1)
--         Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--         Filter: ((orders.carts_cart_id IS NULL) OR (orders.order_status_order_status_id = 1))
--         Rows Removed by Filter: 6633
--         Buffers: shared hit=62
--         ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.012..2.530 rows=10995 loops=1)
--               Buffers: shared hit=49
--         ->  Hash  (cost=28.00..28.00 rows=1500 width=8) (actual time=1.522..1.524 rows=1500 loops=1)
--               Buckets: 2048  Batches: 1  Memory Usage: 75kB
--               Buffers: shared hit=13
--               ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=8) (actual time=0.009..0.654 rows=1500 loops=1)
--                     Buffers: shared hit=13
--   ->  Hash  (cost=145.00..145.00 rows=4000 width=68) (actual time=6.381..6.381 rows=4000 loops=1)
--         Buckets: 4096  Batches: 1  Memory Usage: 458kB
--         Buffers: shared hit=105
--         ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=68) (actual time=0.054..2.667 rows=4000 loops=1)
--               Buffers: shared hit=105
-- Planning:
--   Buffers: shared hit=56 read=7
-- Planning Time: 1.373 ms
-- Execution Time: 27.142 ms


-- With Index Without Seq Scan

-- Hash Join  (cost=318.84..805.98 rows=2052 width=64) (actual time=3.176..10.731 rows=4362 loops=1)
--   Hash Cond: (cart_product.products_product_id = products.product_id)
--   Buffers: shared hit=84 read=33
--   ->  Merge Right Join  (cost=0.56..482.30 rows=2052 width=4) (actual time=0.055..5.261 rows=4362 loops=1)
--         Merge Cond: (orders.carts_cart_id = cart_product.carts_cart_id)
--         Filter: ((orders.carts_cart_id IS NULL) OR (orders.order_status_order_status_id = 1))
--         Rows Removed by Filter: 6633
--         Buffers: shared hit=7 read=33
--         ->  Index Only Scan using orders_carts_cart_id_order_status_order_status_id_idx on orders  (cost=0.28..50.78 rows=1500 width=8) (actual time=0.016..0.277 rows=1500 loops=1)
--               Heap Fetches: 0
--               Buffers: shared hit=4 read=3
--         ->  Index Only Scan using cart_product_carts_cart_id_products_product_id_idx on cart_product  (cost=0.29..297.21 rows=10995 width=8) (actual time=0.015..2.143 rows=10995 loops=1)
--               Heap Fetches: 0
--               Buffers: shared hit=3 read=30
--   ->  Hash  (cost=268.28..268.28 rows=4000 width=68) (actual time=3.112..3.113 rows=4000 loops=1)
--         Buckets: 4096  Batches: 1  Memory Usage: 458kB
--         Buffers: shared hit=77
--         ->  Index Scan using products_product_id_key on products  (cost=0.28..268.28 rows=4000 width=68) (actual time=0.007..1.549 rows=4000 loops=1)
--               Buffers: shared hit=77
-- Planning:
--   Buffers: shared hit=21
-- Planning Time: 0.337 ms
-- Execution Time: 11.085 ms
