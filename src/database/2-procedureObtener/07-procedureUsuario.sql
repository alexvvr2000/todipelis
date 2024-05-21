use todipelis;

DELIMITER //

CREATE PROCEDURE procedureUsuario(IN idUsuarioBuscado INT)
BEGIN
    DECLARE usuario_existe BOOLEAN;

    SET usuario_existe = funcionUsuarioExiste(idUsuarioBuscado);

    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 1400: Usuario.idUsuario no existe';
    END IF;

    SELECT nombreUsuario, urlFotoPerfil, correoElectronico
    FROM Usuario
    WHERE idUsuario = idUsuarioBuscado;
END//

DELIMITER ;
