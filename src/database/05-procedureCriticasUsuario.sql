DELIMITER //

CREATE PROCEDURE procedureCriticasUsuario(IN idUsuarioBuscado INT)
BEGIN
    DECLARE usuario_existe BOOLEAN;

    -- Verificar si el usuario existe
    SET usuario_existe = funcionUsuarioExiste(idUsuarioBuscado);

    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 1300: Usuario.idUsuario no existe';
    END IF;

    -- Obtener críticas del usuario
    SELECT descripcion, estrellas, fechaAgregado, idPelicula
    FROM ListaCriticas
    WHERE idUsuario = idUsuarioBuscado;
END//

DELIMITER ;
