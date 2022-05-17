CREATE OR REPLACE PROCEDURE update_user_email(
    id_user int, new_email users.email%type
)
language plpgsql
AS $$
BEGIN
    -- Try to found email with existing users
    SELECT *
    FROM users
    WHERE email = new_email;

    -- Check for exists email
    if not found then
        UPDATE users SET email=new_email WHERE user_id=id_user;
        COMMIT;
    else
        raise exception 'User with this email already exist';
    end if;

END $$;


DROP procedure if exists update_user_email(id_user int, new_email users.email%type);


call update_user_email(2, 'new_test_email@gmail.com');
