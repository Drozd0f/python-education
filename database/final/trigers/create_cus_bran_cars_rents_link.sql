CREATE OR REPLACE FUNCTION create_cus_bran_cars_rents_link()
returns TRIGGER
language plpgsql
AS
$$
BEGIN
    INSERT INTO customers_branches_cars_rents(customers_customer_id, branches_branch_id, cars_car_id, rents_rent_id)
    VALUES (NULL, NULL, NULL, new.rent_id);
    return new;
END
$$;


BEGIN;
CREATE TRIGGER trigger_cus_bran_cars_rents_link
    AFTER INSERT
    ON rents
    FOR EACH ROW
    EXECUTE PROCEDURE create_cus_bran_cars_rents_link();
END;


BEGIN;
DROP TRIGGER trigger_cus_bran_cars_rents_link ON rents;
DROP FUNCTION IF EXISTS create_cus_bran_cars_rents_link();
END;
