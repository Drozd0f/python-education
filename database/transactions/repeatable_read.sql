-- Использовать транзакции для insert, update, delete на 3х таблицах.
-- Предоставить разнообразные примеры включая возврат к savepoints.

BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

SELECT * FROM potential_customers ORDER BY potential_customer_id DESC;
INSERT INTO potential_customers(email, name, surname, second_name, city)
VALUES ('test_transactions@test.com', 'test_transactions', 'test_transactions', 'test_transactions', 'test_transactions');

UPDATE potential_customers
SET city='new_test_transactions'
WHERE name='test_transactions';

ROLLBACK;

DELETE FROM potential_customers WHERE city='new_test_transactions';

COMMIT;


BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

INSERT INTO order_status(order_status_id, status_name) VALUES (6, 'test_status');

UPDATE order_status SET status_name='new_test_status' WHERE order_status_id=6;

DELETE FROM order_status WHERE order_status_id=6;

ROLLBACK;
COMMIT;
