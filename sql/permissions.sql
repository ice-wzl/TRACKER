-- Flush privileges to make sure changes take effect
FLUSH PRIVILEGES;

-- Create roles
CREATE ROLE 'admin_role';
CREATE ROLE 'read_role';
CREATE ROLE 'modify_role';

-- Granting admin_role all privileges on the SCHOOL database with the ability to grant further
GRANT ALL PRIVILEGES ON TRACKER.* TO 'admin_role' WITH GRANT OPTION;

-- Granting read_role the SELECT privilege on the SCHOOL database
GRANT SELECT ON TRACKER.* TO 'read_role';

GRANT EXECUTE ON PROCEDURE TRACKER.GetDeploymentDetails TO 'read_role';


GRANT SELECT, INSERT, UPDATE, DELETE ON TRACKER.* TO 'modify_user'@'%';
GRANT EXECUTE ON PROCEDURE TRACKER.AddImplant TO 'modify_user';
GRANT EXECUTE ON PROCEDURE TRACKER.AddDeployment TO 'modify_user';
GRANT EXECUTE ON PROCEDURE TRACKER.AddLocation TO 'modify_user';
GRANT EXECUTE ON PROCEDURE TRACKER.GetDeploymentDetails TO 'modify_user';

GRANT ALL PRIVILEGES ON TRACKER.* TO 'admin_user'@'dev.space' WITH GRANT OPTION;

-- Grant roles to users
GRANT 'admin_role' TO 'admin_user';
GRANT 'read_role' TO 'read_only';
GRANT 'modify_role' TO 'modify_user';

-- Set default roles
SET DEFAULT ROLE 'admin_role' TO 'admin_user';
SET DEFAULT ROLE 'read_role' TO 'read_only';
SET DEFAULT ROLE 'modify_role' TO 'modify_user';

-- Flush privileges to make sure all changes are applied
FLUSH PRIVILEGES;
