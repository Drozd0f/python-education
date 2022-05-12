-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.
ANALYZE products;
ANALYZE cart_product;

SET enable_seqscan TO off;
EXPLAIN (ANALYZE, BUFFERS) SELECT product_title, product_description, in_stock, price, slug, category_id, count(product_id)
FROM products
INNER JOIN cart_product
ON cart_product.products_product_id=products.product_id
GROUP BY product_title, product_description, in_stock, price, slug, category_id
ORDER BY count(product_id) DESC LIMIT 10;
SET enable_seqscan TO on;

-- Without Index

-- Limit  (cost=701.70..701.72 rows=10 width=72) (actual time=24.206..24.212 rows=10 loops=1)
--   Buffers: shared hit=154
--   ->  Sort  (cost=701.70..711.70 rows=4000 width=72) (actual time=24.205..24.208 rows=10 loops=1)
--         Sort Key: (count(products.product_id)) DESC
--         Sort Method: top-N heapsort  Memory: 26kB
--         Buffers: shared hit=154
--         ->  HashAggregate  (cost=575.26..615.26 rows=4000 width=72) (actual time=21.083..22.750 rows=3742 loops=1)
-- "              Group Key: products.product_title, products.product_description, products.in_stock, products.price, products.slug, products.category_id"
--               Batches: 1  Memory Usage: 985kB
--               Buffers: shared hit=154
--               ->  Hash Join  (cost=195.00..382.85 rows=10995 width=68) (actual time=2.663..10.744 rows=10995 loops=1)
--                     Hash Cond: (cart_product.products_product_id = products.product_id)
--                     Buffers: shared hit=154
--                     ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.006..1.363 rows=10995 loops=1)
--                           Buffers: shared hit=49
--                     ->  Hash  (cost=145.00..145.00 rows=4000 width=68) (actual time=2.648..2.649 rows=4000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 458kB
--                           Buffers: shared hit=105
--                           ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=68) (actual time=0.028..1.139 rows=4000 loops=1)
--                                 Buffers: shared hit=105
-- Planning:
--   Buffers: shared hit=8
-- Planning Time: 0.203 ms
-- Execution Time: 24.278 ms


CREATE INDEX ON cart_product(products_product_id);
CREATE INDEX ON products(product_id, product_title, product_description, in_stock, price, slug, category_id);

DROP INDEX IF EXISTS cart_product_products_product_id_idx;
DROP INDEX IF EXISTS products_product_id_product_title_product_description_in_st_idx;


-- With Index Without Seq Scan

-- Limit  (cost=701.70..701.72 rows=10 width=72) (actual time=34.942..34.947 rows=10 loops=1)
--   Buffers: shared hit=154
--   ->  Sort  (cost=701.70..711.70 rows=4000 width=72) (actual time=34.940..34.944 rows=10 loops=1)
--         Sort Key: (count(products.product_id)) DESC
--         Sort Method: top-N heapsort  Memory: 26kB
--         Buffers: shared hit=154
--         ->  HashAggregate  (cost=575.26..615.26 rows=4000 width=72) (actual time=32.018..33.504 rows=3742 loops=1)
-- "              Group Key: products.product_title, products.product_description, products.in_stock, products.price, products.slug, products.category_id"
--               Batches: 1  Memory Usage: 985kB
--               Buffers: shared hit=154
--               ->  Hash Join  (cost=195.00..382.85 rows=10995 width=68) (actual time=5.583..17.233 rows=10995 loops=1)
--                     Hash Cond: (cart_product.products_product_id = products.product_id)
--                     Buffers: shared hit=154
--                     ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.013..2.053 rows=10995 loops=1)
--                           Buffers: shared hit=49
--                     ->  Hash  (cost=145.00..145.00 rows=4000 width=68) (actual time=5.554..5.555 rows=4000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 458kB
--                           Buffers: shared hit=105
--                           ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=68) (actual time=0.052..2.342 rows=4000 loops=1)
--                                 Buffers: shared hit=105
-- Planning:
--   Buffers: shared hit=61 read=8
-- Planning Time: 1.353 ms
-- Execution Time: 35.054 ms

-- With Index With Seq Scan

-- Limit  (cost=923.24..923.26 rows=10 width=72) (actual time=23.746..23.751 rows=10 loops=1)
--   Buffers: shared hit=81 read=19
--   ->  Sort  (cost=923.24..933.24 rows=4000 width=72) (actual time=23.745..23.748 rows=10 loops=1)
--         Sort Key: (count(products.product_id)) DESC
--         Sort Method: top-N heapsort  Memory: 26kB
--         Buffers: shared hit=81 read=19
--         ->  HashAggregate  (cost=796.80..836.80 rows=4000 width=72) (actual time=20.713..22.308 rows=3742 loops=1)
-- "              Group Key: products.product_title, products.product_description, products.in_stock, products.price, products.slug, products.category_id"
--               Batches: 1  Memory Usage: 985kB
--               Buffers: shared hit=81 read=19
--               ->  Hash Join  (cost=318.56..604.39 rows=10995 width=68) (actual time=3.110..10.637 rows=10995 loops=1)
--                     Hash Cond: (cart_product.products_product_id = products.product_id)
--                     Buffers: shared hit=81 read=19
--                     ->  Index Only Scan using cart_product_products_product_id_idx on cart_product  (cost=0.29..257.21 rows=10995 width=4) (actual time=0.015..2.076 rows=10995 loops=1)
--                           Heap Fetches: 0
--                           Buffers: shared hit=4 read=19
--                     ->  Hash  (cost=268.28..268.28 rows=4000 width=68) (actual time=3.085..3.086 rows=4000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 458kB
--                           Buffers: shared hit=77
--                           ->  Index Scan using products_product_id_key on products  (cost=0.28..268.28 rows=4000 width=68) (actual time=0.012..1.540 rows=4000 loops=1)
--                                 Buffers: shared hit=77
-- Planning:
--   Buffers: shared hit=14
-- Planning Time: 0.275 ms
-- Execution Time: 23.833 ms
