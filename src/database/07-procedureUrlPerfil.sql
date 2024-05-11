DELIMITER //

CREATE PROCEDURE procedureUrlPerfil(IN idUsuarioBuscado INT)
BEGIN
    DECLARE usuario_existe BOOLEAN;

    -- Verificar si el usuario existe
    SET usuario_existe = funcionUsuarioExiste(idUsuarioBuscado);

    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 1400: Usuario.idUsuario no existe';
    END IF;

    -- Obtener la URL del perfil del usuario
    SELECT urlFotoPerfil
    FROM Usuario
    WHERE idUsuario = idUsuarioBuscado;
END//

DELIMITER ;
