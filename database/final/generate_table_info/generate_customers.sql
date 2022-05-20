CREATE OR REPLACE PROCEDURE generate_customers(count INT)
language plpgsql
AS
$$
BEGIN
    for i in 1..count loop
        INSERT INTO customers(name, surname)
        SELECT ('Name ' || i)::VARCHAR, ('Surname ' || i)::VARCHAR;
    end loop;
END
$$;


BEGIN;
call generate_customers(10000);
END;
