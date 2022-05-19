CREATE SEQUENCE phone_number
  START WITH 10000000000
  INCREMENT BY 1
  MINVALUE 10000000000
  MAXVALUE 100000000000
  CACHE 1;


CREATE OR REPLACE PROCEDURE generate_phones(count_cust INT, count_branch INT)
language plpgsql
AS
$$
DECLARE
    id_first_user INT;
    id_first_branch INT;
    id_phone INT;
BEGIN
    SELECT customer_id
    INTO id_first_user
    FROM customers
    LIMIT 1;

    SELECT branch_id
    INTO id_first_branch
    FROM branches
    LIMIT 1;

    for i in 1..(count_cust + count_branch) loop

        INSERT INTO phones(number)
        SELECT ('+' || (SELECT nextval('phone_number')))::VARCHAR
        RETURNING phone_id INTO id_phone;

        if i <= count_cust then
            INSERT INTO phones_customers(phones_phone_id, customers_customer_id)
            VALUES (id_phone, id_first_user);
            id_first_user := id_first_user + 1;
        else
            INSERT INTO phones_branches(phones_phone_id, branches_branch_id)
            VALUES (id_phone, id_first_branch);
            id_first_branch := id_first_branch + 1;
        end if;

    end loop;

END
$$;


BEGIN;
call generate_phones(10000, 30);
END;


TRUNCATE TABLE phones CASCADE;
