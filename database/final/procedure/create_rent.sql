CREATE OR REPLACE PROCEDURE create_rent(
    id_customer customers.customer_id%type, id_branche branches.branch_id%type, id_car cars.car_id%type,
    r_price rents.price%type, r_period rents.period%type
)
language plpgsql
AS
$$
DECLARE
    id_rent INT;
BEGIN
    if r_period > 10 then
        raise 'Renting for more than 10 days is not possible';
    end if;

    INSERT INTO rents(price, rent_date, period)
    VALUES (r_price, now(), r_period)
    RETURNING rent_id into id_rent;

    UPDATE customers_branches_cars_rents
    SET
        customers_customer_id = id_customer,
        branches_branch_id = id_branche,
        cars_car_id = id_car
    WHERE rents_rent_id = id_rent;

END
$$;


SELECT customer_id FROM customers LIMIT 1;
SELECT branch_id FROM branches LIMIT 1;
SELECT car_id FROM cars LIMIT 1;


call create_rent(10001, 20061, 20085, 200, 10);
call create_rent(10001, 20061, 20085, 200, 11);


DROP PROCEDURE IF EXISTS update_price(updated_brand brands.brand, updated_model models.model, new_price rents.price);

SELECT * FROM customers_branches_cars_rents ORDER BY rents_rent_id DESC LIMIT 5;
SELECT * FROM rents ORDER BY rent_id DESC LIMIT 5;
