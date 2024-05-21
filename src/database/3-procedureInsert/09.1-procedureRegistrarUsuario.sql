use todipelis;

DELIMITER //

CREATE PROCEDURE procedureRegistrarUsuario(
    IN insertadoCorreoElectronico VARCHAR(100),
    IN insertadoClaveAcceso VARCHAR(50),
    IN insertadoNombreUsuario VARCHAR(100)
)
BEGIN
    DECLARE insertadoSalt CHAR(30);
    DECLARE claveAccessoHash CHAR(128);

    IF funcionCorreoExiste(insertadoCorreoElectronico) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4200: Usuario.Correo ya tiene registro en base';
    END IF;

    IF insertadoClaveAcceso = "" THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4200: Nueva clave de accesso no puede estar vacia';
    END IF;

    IF insertadoNombreUsuario = "" THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4200: Nuevo nombre de usuario no puede estar vacio';
    END IF;

    SET insertadoSalt = SUBSTRING(HEX(RANDOM_BYTES(32)), 1, 30);
    SET claveAccessoHash = SHA2(CONCAT(insertadoClaveAcceso, insertadoSalt),512);

    INSERT INTO Usuario(correoElectronico, claveAccesso, saltClaveAcceso, nombreUsuario) VALUES
        (insertadoCorreoElectronico, claveAccessoHash, insertadoSalt, insertadoNombreUsuario);

    SELECT LAST_INSERT_ID() as idUsuarioNuevo;
END//

DELIMITER ;
