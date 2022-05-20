CREATE SEQUENCE IF NOT EXISTS car_number START 1;

CREATE OR REPLACE FUNCTION random_brands_models() returns INT
language plpgsql
AS
$$
BEGIN
    return (
        SELECT brands_models_id
        FROM brands_models
        ORDER BY random() LIMIT 1
    );
END
$$;



CREATE OR REPLACE PROCEDURE generate_cars(count INT)
language plpgsql
AS
$$
DECLARE
    count_decimal INT := 1;
    zero_count INT := 28;
    temp_car_id INT;
BEGIN
    for i in 1..count loop
        if i = 10 ^ count_decimal then
            count_decimal := count_decimal + 1;
            zero_count := zero_count - count_decimal;
        end if;

        INSERT INTO cars(number)
        SELECT ('#' || repeat('0', zero_count) || i)::VARCHAR
        RETURNING car_id INTO temp_car_id;

        INSERT INTO cars_brands(cars_car_id, brands_models_id)
        VALUES (temp_car_id, random_brands_models());

    end loop;
END
$$;


BEGIN;
call generate_cars(10000);
END;
