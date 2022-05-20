CREATE OR REPLACE VIEW get_customers_address AS
SELECT ac.customers_id, c.name as city, s.name as street
FROM address_customers ac
    LEFT JOIN streets_city sc on ac.address_id = sc.streets_city_id
    LEFT JOIN streets s on sc.streets_street_id = s.street_id
    LEFT JOIN cities c on sc.cities_city_id = c.city_id;


SELECT count(customers_id) FROM get_customers_address WHERE city LIKE 'New York';


DROP VIEW IF EXISTS get_customers_address;
