BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

SELECT * FROM potential_customers ORDER BY potential_customer_id DESC;
INSERT INTO potential_customers(email, name, surname, second_name, city)
VALUES ('test_transactions@test.com', 'test_transactions', 'test_transactions', 'test_transactions', 'test_transactions');

SAVEPOINT NEW_POTENT_CUST;

UPDATE potential_customers
SET city='new_test_transactions'
WHERE name='test_transactions';

SAVEPOINT CHANGE_CITY_COMPL;
RELEASE NEW_POTENT_CUST;

DELETE FROM potential_customers WHERE city='new_test_transactions';

ROLLBACK TO CHANGE_CITY_COMPL;
COMMIT;



BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;

INSERT INTO order_status(order_status_id, status_name) VALUES (6, 'test_status');

SAVEPOINT CREATE_STATUS;

UPDATE order_status SET status_name='new_test_status' WHERE order_status_id=6;

ROLLBACK TO CREATE_STATUS;
SAVEPOINT NEW_STATUS;
RELEASE CREATE_STATUS;

DELETE FROM order_status WHERE order_status_id=6;

ROLLBACK TO NEW_STATUS;
COMMIT;
