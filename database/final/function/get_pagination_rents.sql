CREATE OR REPLACE FUNCTION get_cars_brands_models()
RETURNS text
language plpgsql
AS
$$
DECLARE
    titles text default '';
    rec_rent record;
    brand_name VARCHAR;
    model_name VARCHAR;
    cur_rents cursor IS
        SELECT brands_brand_id, models_model_id
        FROM brands_models;
BEGIN
    OPEN cur_rents;
    titles := 'Cars: ';
    loop
      FETCH cur_rents INTO rec_rent;
      EXIT WHEN NOT found;
      SELECT brand INTO brand_name FROM brands WHERE brand_id = rec_rent.brands_brand_id;
      SELECT model INTO model_name FROM models WHERE model_id = rec_rent.models_model_id;
      titles := titles || ' ' || brand_name || ' ' || model_name || ', ';
    end loop;
    close cur_rents;
    return titles;
END
$$;


SELECT get_cars_brands_models();
