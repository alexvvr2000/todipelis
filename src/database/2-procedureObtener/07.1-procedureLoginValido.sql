use todipelis;

DELIMITER //

CREATE PROCEDURE procedureLoginValido(
    IN buscadoCorreoElectronico VARCHAR(255), 
    IN buscadoClaveAccesso VARCHAR(50)
)
BEGIN
    DECLARE saltUsuario CHAR(30);
    DECLARE hashClaveBuscada CHAR(128);
    DECLARE datosConcuerdan BOOLEAN;

    IF NOT funcionCorreoExiste(buscadoCorreoElectronico) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El usuario buscado no existe en base';
    END IF;

    SET saltUsuario = (
        SELECT saltClaveAcceso 
        FROM Usuario 
        WHERE correoElectronico = buscadoCorreoElectronico 
        LIMIT 1
    );

    SET hashClaveBuscada = SHA2(CONCAT(buscadoClaveAccesso, saltUsuario), 512);

    SET datosConcuerdan = EXISTS(
        SELECT 1 
        FROM Usuario 
        WHERE correoElectronico = buscadoCorreoElectronico 
        AND claveAccesso = hashClaveBuscada
    );

    IF NOT datosConcuerdan THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Credenciales inválidas';
    END IF;

    SELECT idUsuario 
    FROM Usuario 
    WHERE correoElectronico = buscadoCorreoElectronico;
END//

DELIMITER ;