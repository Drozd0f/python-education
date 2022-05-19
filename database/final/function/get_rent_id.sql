CREATE OR REPLACE FUNCTION get_rent_id(
    rent_brand brands.brand%type, rent_model models.model%type
)
RETURNS record
language plpgsql
AS
$$
BEGIN
    return (
        SELECT r.rent_id
        FROM rents r
            LEFT JOIN customers_branches_cars_rents cbcr on r.rent_id = cbcr.rents_rent_id
            LEFT JOIN cars c on cbcr.cars_car_id = c.car_id
            LEFT JOIN cars_brands cb on c.car_id = cb.cars_car_id
            LEFT JOIN brands_models bm on cb.brands_models_id = bm.brands_models_id
            LEFT JOIN brands b on bm.brands_brand_id = b.brand_id
            LEFT JOIN models m on bm.models_model_id = m.model_id
        WHERE b.brand = rent_brand AND m.model = rent_model
    );
END
$$;


DROP FUNCTION IF EXISTS get_rent_id(rent_brand brands.brand, rent_model models.model);
