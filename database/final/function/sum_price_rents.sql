CREATE OR REPLACE FUNCTION sum_price_rents()
returns numeric
language plpgsql
AS
$$
DECLARE
    temp_price numeric;
    sum_price numeric := 0;
BEGIN
    for temp_price in (
        SELECT price
        FROM rents
    )
    loop
        sum_price := sum_price + temp_price;
    end loop;

    return sum_price;
END;
$$;


SELECT sum_price_rents();
