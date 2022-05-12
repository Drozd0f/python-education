-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).
ANALYZE users;
ANALYZE carts;
ANALYZE orders;

SET enable_seqscan TO off;
EXPLAIN (ANALYZE, BUFFERS) SELECT email, first_name, last_name, middle_name, count(order_id)
FROM users, carts
LEFT JOIN orders
ON carts.cart_id=orders.carts_cart_id
WHERE users.user_id=carts.users_user_id
GROUP BY email, first_name, last_name, middle_name
ORDER BY count(order_id) DESC LIMIT 5;
SET enable_seqscan TO on;

-- Without Index

-- Limit  (cost=302.93..302.94 rows=5 width=72) (actual time=7.784..7.789 rows=5 loops=1)
--   Buffers: shared hit=88
--   ->  Sort  (cost=302.93..307.93 rows=2000 width=72) (actual time=7.782..7.786 rows=5 loops=1)
--         Sort Key: (count(orders.order_id)) DESC
--         Sort Method: top-N heapsort  Memory: 25kB
--         Buffers: shared hit=88
--         ->  HashAggregate  (cost=249.71..269.71 rows=2000 width=72) (actual time=6.370..7.089 rows=2000 loops=1)
-- "              Group Key: users.email, users.first_name, users.last_name, users.middle_name"
--               Batches: 1  Memory Usage: 633kB
--               Buffers: shared hit=88
--               ->  Hash Join  (cost=187.50..224.71 rows=2000 width=68) (actual time=2.740..4.915 rows=2000 loops=1)
--                     Hash Cond: (carts.users_user_id = users.user_id)
--                     Buffers: shared hit=88
--                     ->  Hash Right Join  (cost=60.00..91.95 rows=2000 width=8) (actual time=0.822..1.963 rows=2000 loops=1)
--                           Hash Cond: (orders.carts_cart_id = carts.cart_id)
--                           Buffers: shared hit=28
--                           ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=8) (actual time=0.004..0.198 rows=1500 loops=1)
--                                 Buffers: shared hit=13
--                           ->  Hash  (cost=35.00..35.00 rows=2000 width=8) (actual time=0.812..0.813 rows=2000 loops=1)
--                                 Buckets: 2048  Batches: 1  Memory Usage: 95kB
--                                 Buffers: shared hit=15
--                                 ->  Seq Scan on carts  (cost=0.00..35.00 rows=2000 width=8) (actual time=0.007..0.357 rows=2000 loops=1)
--                                       Buffers: shared hit=15
--                     ->  Hash  (cost=90.00..90.00 rows=3000 width=68) (actual time=1.909..1.909 rows=3000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 333kB
--                           Buffers: shared hit=60
--                           ->  Seq Scan on users  (cost=0.00..90.00 rows=3000 width=68) (actual time=0.005..0.875 rows=3000 loops=1)
--                                 Buffers: shared hit=60
-- Planning:
--   Buffers: shared hit=26
-- Planning Time: 0.383 ms
-- Execution Time: 7.850 ms



CREATE INDEX ON orders(carts_cart_id);
CREATE INDEX ON users(user_id, email, first_name, middle_name, last_name);

DROP INDEX IF EXISTS orders_carts_cart_id_idx;
DROP INDEX IF EXISTS users_user_id_email_first_name_middle_name_last_name_idx;

-- With Index With Seq Scan

-- Limit  (cost=302.93..302.94 rows=5 width=72) (actual time=7.694..7.699 rows=5 loops=1)
--   Buffers: shared hit=88
--   ->  Sort  (cost=302.93..307.93 rows=2000 width=72) (actual time=7.692..7.696 rows=5 loops=1)
--         Sort Key: (count(orders.order_id)) DESC
--         Sort Method: top-N heapsort  Memory: 25kB
--         Buffers: shared hit=88
--         ->  HashAggregate  (cost=249.71..269.71 rows=2000 width=72) (actual time=6.251..6.992 rows=2000 loops=1)
-- "              Group Key: users.email, users.first_name, users.last_name, users.middle_name"
--               Batches: 1  Memory Usage: 633kB
--               Buffers: shared hit=88
--               ->  Hash Join  (cost=187.50..224.71 rows=2000 width=68) (actual time=2.682..4.813 rows=2000 loops=1)
--                     Hash Cond: (carts.users_user_id = users.user_id)
--                     Buffers: shared hit=88
--                     ->  Hash Right Join  (cost=60.00..91.95 rows=2000 width=8) (actual time=0.835..1.962 rows=2000 loops=1)
--                           Hash Cond: (orders.carts_cart_id = carts.cart_id)
--                           Buffers: shared hit=28
--                           ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=8) (actual time=0.004..0.195 rows=1500 loops=1)
--                                 Buffers: shared hit=13
--                           ->  Hash  (cost=35.00..35.00 rows=2000 width=8) (actual time=0.825..0.826 rows=2000 loops=1)
--                                 Buckets: 2048  Batches: 1  Memory Usage: 95kB
--                                 Buffers: shared hit=15
--                                 ->  Seq Scan on carts  (cost=0.00..35.00 rows=2000 width=8) (actual time=0.007..0.356 rows=2000 loops=1)
--                                       Buffers: shared hit=15
--                     ->  Hash  (cost=90.00..90.00 rows=3000 width=68) (actual time=1.838..1.839 rows=3000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 333kB
--                           Buffers: shared hit=60
--                           ->  Seq Scan on users  (cost=0.00..90.00 rows=3000 width=68) (actual time=0.005..0.831 rows=3000 loops=1)
--                                 Buffers: shared hit=60
-- Planning:
--   Buffers: shared hit=61 read=7
-- Planning Time: 0.596 ms
-- Execution Time: 7.763 ms


-- With Index Without Seq Scan


-- Limit  (cost=444.07..444.08 rows=5 width=72) (actual time=7.964..7.968 rows=5 loops=1)
--   Buffers: shared hit=108 read=3
--   ->  Sort  (cost=444.07..449.07 rows=2000 width=72) (actual time=7.962..7.965 rows=5 loops=1)
--         Sort Key: (count(orders.order_id)) DESC
--         Sort Method: top-N heapsort  Memory: 25kB
--         Buffers: shared hit=108 read=3
--         ->  HashAggregate  (cost=390.85..410.85 rows=2000 width=72) (actual time=6.537..7.263 rows=2000 loops=1)
-- "              Group Key: users.email, users.first_name, users.last_name, users.middle_name"
--               Batches: 1  Memory Usage: 633kB
--               Buffers: shared hit=108 read=3
--               ->  Hash Join  (cost=190.34..365.85 rows=2000 width=68) (actual time=2.218..5.054 rows=2000 loops=1)
--                     Hash Cond: (carts.users_user_id = users.user_id)
--                     Buffers: shared hit=108 read=3
--                     ->  Merge Left Join  (cost=0.56..170.81 rows=2000 width=8) (actual time=0.019..1.814 rows=2000 loops=1)
--                           Merge Cond: (carts.cart_id = orders.carts_cart_id)
--                           Buffers: shared hit=38 read=3
--                           ->  Index Scan using carts_cart_id_key on carts  (cost=0.28..80.28 rows=2000 width=8) (actual time=0.009..0.458 rows=2000 loops=1)
--                                 Buffers: shared hit=22
--                           ->  Index Scan using orders_carts_cart_id_idx on orders  (cost=0.28..66.78 rows=1500 width=8) (actual time=0.006..0.401 rows=1500 loops=1)
--                                 Buffers: shared hit=16 read=3
--                     ->  Hash  (cost=152.28..152.28 rows=3000 width=68) (actual time=2.192..2.192 rows=3000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 333kB
--                           Buffers: shared hit=70
--                           ->  Index Scan using users_user_id_key on users  (cost=0.28..152.28 rows=3000 width=68) (actual time=0.010..1.159 rows=3000 loops=1)
--                                 Buffers: shared hit=70
-- Planning:
--   Buffers: shared hit=59 read=7
-- Planning Time: 0.624 ms
-- Execution Time: 8.032 ms
