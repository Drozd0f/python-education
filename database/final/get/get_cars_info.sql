SET enable_seqscan TO off;
EXPLAIN (ANALYZE, BUFFERS) SELECT c.number, m.model, b.brand
FROM cars c
    LEFT JOIN cars_brands cb on c.car_id = cb.cars_car_id
    LEFT JOIN brands_models bm on cb.brands_models_id = bm.brands_models_id
    LEFT JOIN models m on bm.models_model_id = m.model_id
    LEFT JOIN brands b on bm.brands_brand_id = b.brand_id
WHERE b.brand LIKE 'Chevrolet';
SET enable_seqscan TO on;


CREATE INDEX ON cars(car_id, number);
CREATE INDEX ON models(model_id, model);
CREATE INDEX ON brands(brand_id, brand);

DROP INDEX IF EXISTS brands_brand_idx;
DROP INDEX IF EXISTS cars_car_id_number_idx;
DROP INDEX IF EXISTS models_model_id_model_idx;
