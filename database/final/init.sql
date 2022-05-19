CREATE TABLE IF NOT EXISTS streets(
    street_id serial PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS cities(
    city_id serial PRIMARY KEY,
    name VARCHAR(255),
    initials VARCHAR(4)
);


CREATE TABLE IF NOT EXISTS streets_city(
    streets_city_id serial PRIMARY KEY,
    cities_city_id INTEGER REFERENCES cities(city_id),
    streets_street_id INTEGER REFERENCES streets(street_id)
);


CREATE TABLE IF NOT EXISTS address_customers(
    address_id INTEGER REFERENCES streets_city(streets_city_id),
    customers_id INTEGER REFERENCES customers(customer_id)
);


CREATE TABLE IF NOT EXISTS address_branches(
    address_id INTEGER REFERENCES streets_city(streets_city_id),
    branches_id INTEGER REFERENCES branches(branch_id)
);


CREATE TABLE IF NOT EXISTS phones(
    phone_id serial PRIMARY KEY,
    number VARCHAR(30) UNIQUE
);


CREATE TABLE IF NOT EXISTS customers(
    customer_id serial PRIMARY KEY,
    name VARCHAR(255),
    surname VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS branches(
    branch_id serial PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS phones_customers(
    phones_phone_id INTEGER REFERENCES phones(phone_id),
    customers_customer_id INTEGER REFERENCES customers(customer_id)
);


CREATE TABLE IF NOT EXISTS phones_branches(
    phones_phone_id INTEGER REFERENCES phones(phone_id),
    branches_branch_id INTEGER REFERENCES branches(branch_id)
);


CREATE TABLE IF NOT EXISTS cities_customers(
    cities_city_id INTEGER REFERENCES cities(city_id),
    customers_customer_id INTEGER REFERENCES customers(customer_id)
);


CREATE TABLE IF NOT EXISTS cities_branches(
    cities_city_id INTEGER REFERENCES cities(city_id),
    branches_branch_id INTEGER REFERENCES branches(branch_id)
);


CREATE TABLE IF NOT EXISTS models(
    model_id serial PRIMARY KEY,
    model VARCHAR(255) UNIQUE
);


CREATE TABLE IF NOT EXISTS brands(
    brand_id serial PRIMARY KEY,
    brand VARCHAR(255) UNIQUE
);


CREATE TABLE IF NOT EXISTS brands_models(
    brands_models_id serial PRIMARY KEY,
    brands_brand_id INTEGER REFERENCES brands(brand_id),
    models_model_id INTEGER REFERENCES models(model_id)
);


CREATE TABLE IF NOT EXISTS cars(
    car_id serial PRIMARY KEY,
    number VARCHAR(30) UNIQUE
);


CREATE TABLE IF NOT EXISTS cars_brands(
    cars_car_id INTEGER REFERENCES cars(car_id),
    brands_models_id INTEGER REFERENCES brands_models(brands_models_id)
);


CREATE TABLE IF NOT EXISTS rents(
    rent_id serial PRIMARY KEY,
    price INTEGER,
    rent_date DATE,
    period INTEGER
);


CREATE TABLE IF NOT EXISTS customers_branches_cars_rents(
    customers_customer_id INTEGER REFERENCES customers(customer_id),
    branches_branch_id INTEGER REFERENCES branches(branch_id),
    cars_car_id INTEGER REFERENCES cars(car_id),
    rents_rent_id INTEGER REFERENCES rents(rent_id)
);
