-- Temporary table for tracking user manipulations with mail
CREATE TEMPORARY TABLE IF NOT EXISTS users_actions(
    id serial PRIMARY KEY,
    old_email VARCHAR(255),
    new_email VARCHAR(255)
);


-- Procedure for record user manipulations with mail
CREATE OR REPLACE PROCEDURE record_users_actions(
    o_email users_actions.old_email%type, n_email users_actions.new_email%type
)
language plpgsql
AS
$$
BEGIN
    if o_email != n_email THEN
        INSERT INTO users_actions(old_email, new_email) VALUES (o_email, n_email);
    else
        raise exception 'Email coincides with the previous';
    end if;
END
$$;


CREATE OR REPLACE FUNCTION update_user_email()
returns TRIGGER
language plpgsql
AS
$$
DECLARE
    users_emails record;
BEGIN
     -- Try to found email with existing users
    SELECT email
    INTO users_emails
    FROM users
    WHERE email = new.email;

    -- Check for exists email
    if not found then
        call record_users_actions(old.email, new.email);
    else
        raise exception 'User with this email already exist';
    end if;
    return new;
END
$$;


BEGIN;
CREATE TRIGGER trigger_update_user_email
    BEFORE UPDATE
    ON users
    FOR EACH ROW
    EXECUTE PROCEDURE update_user_email();
END;

BEGIN;
DROP PROCEDURE IF EXISTS record_users_actions(
    o_email users_actions.old_email%type, n_email users_actions.new_email%type
);
DROP TRIGGER trigger_update_user_email ON users;
DROP FUNCTION IF EXISTS update_user_email();
END;


SELECT * FROM users_actions;


UPDATE users
SET email='test_email@gmail.com'
WHERE user_id=2;
