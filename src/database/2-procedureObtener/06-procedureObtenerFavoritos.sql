DELIMITER //

CREATE PROCEDURE procedureObtenerFavoritos(IN idUsuarioBuscado INT)
BEGIN
    DECLARE usuario_existe BOOLEAN;

    -- Verificar si el usuario existe
    SET usuario_existe = funcionUsuarioExiste(idUsuarioBuscado);

    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 1300: Usuario.idUsuario no existe';
    END IF;

    -- Obtener películas favoritas del usuario
    SELECT idPelicula
    FROM ListaFavoritos
    WHERE idUsuario = idUsuarioBuscado;
END//

DELIMITER ;
