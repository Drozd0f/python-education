CREATE OR REPLACE PROCEDURE generate_branches(count INT)
language plpgsql
AS
$$
BEGIN
    for i in 1..count loop
        INSERT INTO branches(name)
        SELECT ('Branch ' || i)::VARCHAR;
    end loop;
END
$$;


BEGIN;
call generate_branches(30);
END;


TRUNCATE TABLE branches CASCADE;
