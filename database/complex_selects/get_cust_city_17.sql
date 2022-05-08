SELECT first_name, email
FROM users
WHERE city = 'city 17'
UNION
SELECT name, email
FROM potential_customers
WHERE city = 'city 17';
