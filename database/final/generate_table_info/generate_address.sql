CREATE OR REPLACE FUNCTION generate_address_id() returns INT
language plpgsql
AS
$$
BEGIN
    return (
        SELECT streets_city_id
        FROM streets_city
        ORDER BY random() LIMIT 1
    );
END
$$;



CREATE OR REPLACE PROCEDURE generate_address(count_user INT, count_branch INT)
language plpgsql
AS
$$
DECLARE
    first_customers_id INT;
    first_branch_id INT;
BEGIN
    SELECT customer_id
    INTO first_customers_id
    FROM customers
    LIMIT 1;

    SELECT branch_id
    INTO first_branch_id
    FROM branches
    LIMIT 1;

    for i in 1..(count_user + count_branch) loop
        if i <= count_user then
            INSERT INTO address_customers(address_id, customers_id)
            VALUES (generate_address_id(), first_customers_id);
            first_customers_id := first_customers_id + 1;
        else
            INSERT INTO address_branches(address_id, branches_id)
            VALUES (generate_address_id(), first_branch_id);
            first_branch_id := first_branch_id + 1;
        end if;

    end loop;
END
$$;


BEGIN;
call generate_address(10000, 30);
END;


TRUNCATE TABLE address_branches CASCADE;
TRUNCATE TABLE address_customers CASCADE;
