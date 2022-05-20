CREATE OR REPLACE PROCEDURE generate_streets(count INT)
language plpgsql
AS
$$
BEGIN
    for i in 1..count loop
        INSERT INTO streets(name)
        SELECT ('Street ' || i)::VARCHAR;
    end loop;

END
$$;


CREATE OR REPLACE PROCEDURE generate_streets_cities(count INT)
language plpgsql
AS
$$
DECLARE
    first_street_id INT;
    first_cities_id INT;
BEGIN

    SELECT city_id
    INTO first_cities_id
    FROM cities
    LIMIT 1;

    for i in 1..10 loop
        SELECT street_id
        INTO first_street_id
        FROM streets
        LIMIT 1;
        for j in 1..count loop
            INSERT INTO streets_city(cities_city_id, streets_street_id)
            VALUES (first_cities_id, first_street_id);
            first_street_id := first_street_id + 1;
        end loop;
    first_cities_id := first_cities_id + 1;
    end loop;
END
$$;


BEGIN;
call generate_streets(2000);
call generate_streets_cities(2000);
END;


TRUNCATE TABLE streets CASCADE;
TRUNCATE TABLE streets_city CASCADE;
