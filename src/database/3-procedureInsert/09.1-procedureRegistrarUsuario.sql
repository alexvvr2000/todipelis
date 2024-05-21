
use todipelis;

DELIMITER //

CREATE PROCEDURE procedureRegistrarUsuario(
    IN insertadoCorreoElectronico VARCHAR(100),
    IN insertadoClaveAcceso VARCHAR(50),
    IN insertadoNombreUsuario VARCHAR(100)
)
BEGIN
    IF funcionCorreoExiste(insertadoCorreoElectronico) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4200: Usuario.Correo ya tiene registro en base';
    END;

    IF insertadoClaveAcceso = "" THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4200: Nueva clave de accesso no puede estar vacia';
    END;

    IF nombreUsuario = "" THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4200: Nuevo nombre de usuario no puede estar vacio';
    END;

    DECLARE insertadoSalt CHAR(30);
    DECLARE claveAccessoHash CHAR(128);

    SET insertadoSalt = CAST(RANDOM_BYTES(32) AS CHAR(30));
    SET claveAccessoHash = SHA2(CONCAT(insertadoClaveAcceso, insertadoSalt),512);

    INSERT INTO Usuario(correoElectronico, claveAccesso, saltClaveAcceso, nombreUsuario) VALUES
        (insertadoCorreoElectronico, claveAccessoHash, insertadoSalt, insertadoNombreUsuario) 
    RETURNING idUsuario;
END//

DELIMITER ;
