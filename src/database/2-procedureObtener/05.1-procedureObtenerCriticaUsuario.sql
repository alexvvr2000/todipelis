use todipelis;

DELIMITER //

CREATE PROCEDURE procedureObtenerCriticaUsuario(IN idPeliculaBuscado VARCHAR(100), IN idUsuarioBuscado INT)
BEGIN
    DECLARE usuario_existe BOOLEAN;
    DECLARE critica_existe BOOLEAN;

    SET usuario_existe = funcionUsuarioExiste(idUsuarioBuscado);
    SET critica_existe = funcionExisteCritica(idPeliculaBuscado, idUsuarioBuscado);

    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 1300: Usuario.idUsuario no existe';
    END IF;

    IF NOT critica_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 1300: Critica.idPelicula no existe';
    END IF;

    SELECT descripcion, estrellas, fechaAgregado, fechaModificado
    FROM ListaCriticas
    WHERE idUsuario = idUsuarioBuscado AND idPelicula = idPeliculaBuscado;
END//

DELIMITER ;
