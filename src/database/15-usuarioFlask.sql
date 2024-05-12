CREATE USER 'api'@'%' IDENTIFIED BY 'pass218';

GRANT INSERT, UPDATE, DELETE, SELECT ON todipelis.* TO 'api'@'%';

GRANT EXECUTE ON PROCEDURE todipelis.* TO 'api'@'%';