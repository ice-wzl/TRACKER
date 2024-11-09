
-- Drop users
DROP USER IF EXISTS 'admin_user'@'%';
DROP USER IF EXISTS 'read_only'@'%';
DROP USER IF EXISTS 'modify_user'@'%';

-- Drop roles
DROP ROLE IF EXISTS 'admin_role';
DROP ROLE IF EXISTS 'read_role';
DROP ROLE IF EXISTS 'modify_role';


CREATE USER 'admin_user'@'%' IDENTIFIED WITH mysql_native_password BY 'admin1234';