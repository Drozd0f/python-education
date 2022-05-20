CREATE OR REPLACE VIEW get_over_price_rents AS
SELECT rent_id, price
FROM rents r
WHERE price > 900;


SELECT count(*) FROM get_over_price_rents;


DROP VIEW IF EXISTS get_over_price_rents;
