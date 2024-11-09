-- Flush privileges to make sure changes take effect
FLUSH PRIVILEGES;

-- Create roles
CREATE ROLE 'admin_role';

GRANT SELECT, INSERT, UPDATE, DELETE ON TRACKER.* TO 'admin_user'@'%';
GRANT EXECUTE ON PROCEDURE TRACKER.AddImplant TO 'admin_user';
GRANT EXECUTE ON PROCEDURE TRACKER.AddDeployment TO 'admin_user';
GRANT EXECUTE ON PROCEDURE TRACKER.AddLocation TO 'admin_user';
GRANT EXECUTE ON PROCEDURE TRACKER.GetDeploymentDetails TO 'admin_user';

GRANT ALL PRIVILEGES ON TRACKER.* TO 'admin_user'@'%';
-- Grant roles to users
GRANT 'admin_role' TO 'admin_user';

-- Set default roles
SET DEFAULT ROLE 'admin_role' TO 'admin_user';

-- Flush privileges to make sure all changes are applied
FLUSH PRIVILEGES;
