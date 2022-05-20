SET enable_seqscan TO off;
EXPLAIN (ANALYZE, BUFFERS) SELECT c.name, c.surname, r.price, b.name
FROM customers_branches_cars_rents cbcr
    LEFT JOIN customers c ON cbcr.customers_customer_id = c.customer_id
    LEFT JOIN branches b ON cbcr.branches_branch_id = b.branch_id
    LEFT JOIN rents r ON cbcr.rents_rent_id = r.rent_id
WHERE r.period BETWEEN 2 AND 4;
SET enable_seqscan TO on;


CREATE INDEX ON rents(rent_id, period);

DROP INDEX IF EXISTS rents_period_idx;
