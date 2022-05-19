SET enable_seqscan TO off;
EXPLAIN (ANALYZE, BUFFERS) SELECT c.name, c.surname, c2.name, s.name
FROM customers c
    LEFT JOIN address_customers ac on c.customer_id = ac.customers_id
    LEFT JOIN streets_city sc on ac.address_id = sc.streets_city_id
    LEFT JOIN cities c2 on sc.cities_city_id = c2.city_id
    LEFT JOIN streets s on sc.streets_street_id = s.street_id
WHERE c2.name LIKE 'Clovis' AND s.name LIKE 'Street 1';
SET enable_seqscan TO on;


CREATE INDEX ON cities USING hash(name);
CREATE INDEX ON streets USING hash(name);

DROP INDEX IF EXISTS cities_name_idx;
DROP INDEX IF EXISTS streets_name_idx;
