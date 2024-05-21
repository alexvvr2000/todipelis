USE todipelis;

DELIMITER //

CREATE FUNCTION funcionCorreoExiste(buscadoCorreoElectronico VARCHAR(255))
RETURNS BOOLEAN
NOT DETERMINISTIC
BEGIN
    DECLARE existe BOOLEAN;

    SELECT EXISTS(SELECT 1 FROM Usuario WHERE correoElectronico = buscadoCorreoElectronico) INTO existe;

    RETURN existe;
END//

DELIMITER ;
