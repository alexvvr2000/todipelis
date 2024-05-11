GRANT INSERT, UPDATE, DELETE, SELECT ON todipelis.* TO 'api'@'%';

GRANT EXECUTE ON PROCEDURE todipelis.* TO 'api'@'%';

REVOKE CREATE ROUTINE ON todipelis.* FROM 'api'@'%';
