INSERT INTO potential_customers(email, name, surname, second_name, city)
SELECT
    regexp_replace(email, '\d+', (trunc(random() * 20))::VARCHAR, 'g'),
    regexp_replace(first_name, '\d+', (trunc(random() * 20))::VARCHAR, 'g'),
    regexp_replace(middle_name, '\d+', (trunc(random() * 20))::VARCHAR, 'g'),
    regexp_replace(last_name, '\d+', (trunc(random() * 20))::VARCHAR, 'g'),
    regexp_replace(city, '\d+', (trunc(random() * 20))::VARCHAR, 'g')
FROM users
LIMIT 20;
