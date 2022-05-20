CREATE OR REPLACE PROCEDURE update_price(
    updated_brand brands.brand%type, updated_model models.model%type, new_price rents.price%type
)
language plpgsql
AS
$$
BEGIN
    UPDATE rents SET price = new_price WHERE rent_id IN (get_rent_id(updated_brand, updated_model));
END
$$;


call update_price('Ford', 'Fiesta', '200');


DROP PROCEDURE IF EXISTS update_price(updated_brand brands.brand, updated_model models.model, new_price rents.price);
