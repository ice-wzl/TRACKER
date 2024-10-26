
-- Drop users
DROP USER IF EXISTS 'admin_user'@'%';
DROP USER IF EXISTS 'read_only'@'%';
DROP USER IF EXISTS 'modify_user'@'%';

-- Drop roles
DROP ROLE IF EXISTS 'admin_role';
DROP ROLE IF EXISTS 'read_role';
DROP ROLE IF EXISTS 'modify_role';



CREATE USER 'admin_user'@'%' IDENTIFIED BY 'admin1234';
CREATE USER 'read_only'@'%' IDENTIFIED BY 'read1234';
CREATE USER 'modify_user'@'%' IDENTIFIED BY 'modify1234';