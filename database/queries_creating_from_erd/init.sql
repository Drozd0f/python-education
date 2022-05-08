CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER UNIQUE,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff BOOLEAN,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT
);

CREATE TABLE IF NOT EXISTS Carts(
    cart_id INTEGER UNIQUE,
    Users_user_id INTEGER REFERENCES Users(user_id),
    subtotal DECIMAL,
    total DECIMAL,
    cart_timestamp TIMESTAMP(2)
);

CREATE TABLE IF NOT EXISTS Categories(
    category_id INTEGER UNIQUE,
    category_title VARCHAR(255),
    category_description TEXT
);

CREATE TABLE IF NOT EXISTS Products(
    product_id INTEGER UNIQUE,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock INTEGER,
    price FLOAT,
    slug VARCHAR(45),
    category_id INTEGER REFERENCES Categories(category_id)
);

CREATE TABLE IF NOT EXISTS Cart_product(
    carts_cart_id INTEGER REFERENCES Carts(cart_id),
    products_product_id INTEGER REFERENCES Products(product_id)
);

CREATE TABLE IF NOT EXISTS Order_status(
    order_status_id INTEGER UNIQUE,
    status_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Orders(
    order_id INTEGER UNIQUE,
    Carts_cart_id INTEGER REFERENCES Carts(cart_id),
    Order_status_order_status_id INTEGER REFERENCES Order_status(order_status_id),
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2)
);
