CREATE OR REPLACE PROCEDURE update_order_status(
    ord_id orders.order_id%type
)
language plpgsql
AS $$
DECLARE
    current_status_id orders.order_status_order_status_id%type;
BEGIN
    -- Query for check order status
    SELECT order_status_order_status_id
    INTO current_status_id
    FROM orders
    WHERE orders.order_id = ord_id;

    -- Order status check
    if current_status_id = 5 then
        raise exception 'Cannot update closed order';
    elseif current_status_id = 4 then
        raise exception 'Cannot update finished order';
    else
        UPDATE orders
        SET order_status_order_status_id = current_status_id + 1
        WHERE order_id = ord_id;
        COMMIT;
    end if;

END $$;


DROP procedure if exists update_order_status(ord_id orders.order_id%type);


call update_order_status(2);
