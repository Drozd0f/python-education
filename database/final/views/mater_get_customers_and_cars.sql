CREATE MATERIALIZED VIEW IF NOT EXISTS get_customers_and_cars AS
SELECT c.name, c.surname, r.rent_id, c2.number, b.brand, m.model
FROM customers c
    LEFT JOIN customers_branches_cars_rents cbcr ON c.customer_id = cbcr.customers_customer_id
    LEFT JOIN rents r on cbcr.rents_rent_id = r.rent_id
    LEFT JOIN cars c2 on cbcr.cars_car_id = c2.car_id
    LEFT JOIN cars_brands cb on c2.car_id = cb.cars_car_id
    LEFT JOIN brands_models bm on cb.brands_models_id = bm.brands_models_id
    LEFT JOIN brands b on bm.brands_brand_id = b.brand_id
    LEFT JOIN models m on bm.models_model_id = m.model_id;


SELECT * FROM get_customers_and_cars WHERE brand LIKE 'BMW';


DROP MATERIALIZED VIEW IF EXISTS get_customers_and_cars;
