CREATE TABLE IF NOT EXISTS potential_customers(
    potential_customer_id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255),
    surname VARCHAR(255),
    second_name VARCHAR(255),
    city VARCHAR(255)
);
