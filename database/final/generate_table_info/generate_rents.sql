CREATE OR REPLACE FUNCTION random_cars() returns INT
language plpgsql
AS
$$
BEGIN
    return (
        SELECT car_id
        FROM cars
        ORDER BY random() LIMIT 1
    );
END
$$;


CREATE OR REPLACE FUNCTION random_branches() returns INT
language plpgsql
AS
$$
BEGIN
    return (
        SELECT branch_id
        FROM branches
        ORDER BY random() LIMIT 1
    );
END
$$;


CREATE OR REPLACE FUNCTION random_customers() returns INT
language plpgsql
AS
$$
BEGIN
    return (
        SELECT customer_id
        FROM customers
        ORDER BY random() LIMIT 1
    );
END
$$;


CREATE OR REPLACE FUNCTION random_between(low INT ,high INT)
returns INT
language 'plpgsql'
AS
$$
BEGIN
   return floor(random() * (high-low + 1) + low);
END
$$;


CREATE OR REPLACE PROCEDURE generate_rents(count INT)
language plpgsql
AS
$$
DECLARE
    id_rent INT;
BEGIN
    for i in 1..count loop
        INSERT INTO rents(price, rent_date, period)
        VALUES (random_between(100, 1000), now(), random_between(1, 10))
        RETURNING rent_id INTO id_rent;

        INSERT INTO customers_branches_cars_rents(customers_customer_id, branches_branch_id, cars_car_id, rents_rent_id)
        VALUES (random_customers(), random_branches(), random_cars(), id_rent);
    end loop;
END
$$;


BEGIN;
call generate_rents(100000);
END;


TRUNCATE TABLE rents CASCADE;
