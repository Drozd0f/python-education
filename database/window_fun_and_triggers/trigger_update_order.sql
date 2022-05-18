CREATE OR REPLACE FUNCTION update_order()
returns TRIGGER
language plpgsql
AS
$$
BEGIN
    -- Order status check
    if old.order_status_order_status_id = 5 then
        raise exception 'Cannot update closed order';
    elseif old.order_status_order_status_id = 4 then
        raise exception 'Cannot update finished order';
    else
        -- Update date in row updated_at
        SELECT now()::TIMESTAMP(2) INTO new.updated_at;
    end if;
    return new;
END
$$;


BEGIN;
CREATE TRIGGER trigger_update_order
    BEFORE UPDATE
    ON orders
    FOR EACH ROW
    EXECUTE PROCEDURE update_order();
END;


BEGIN;
DROP TRIGGER trigger_update_order ON orders;
DROP FUNCTION IF EXISTS update_order();
END;


UPDATE orders SET order_status_order_status_id = order_status_order_status_id + 1 WHERE order_id=4;


SELECT * FROM orders WHERE order_id=4;
