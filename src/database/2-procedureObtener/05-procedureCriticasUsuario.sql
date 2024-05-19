use todipelis;

DELIMITER //

CREATE PROCEDURE procedureCriticasUsuario(IN idUsuarioBuscado INT)
BEGIN
    DECLARE usuario_existe BOOLEAN;

    SET usuario_existe = funcionUsuarioExiste(idUsuarioBuscado);

    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 1300: Usuario.idUsuario no existe';
    END IF;

    SELECT idPelicula, descripcion, estrellas, fechaAgregado, fechaModificado
    FROM ListaCriticas
    WHERE idUsuario = idUsuarioBuscado;
END//

DELIMITER ;
