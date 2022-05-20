CREATE OR REPLACE FUNCTION create_rent()
returns TRIGGER
language plpgsql
AS
$$
BEGIN
    if new.price > 1000 then
        raise exception 'At the moment, the rent cannot exceed 1000$';
    end if;
    return new;
END
$$;


BEGIN;
CREATE TRIGGER trigger_create_rent
    BEFORE INSERT
    ON rents
    FOR EACH ROW
    EXECUTE PROCEDURE create_rent();
END;
