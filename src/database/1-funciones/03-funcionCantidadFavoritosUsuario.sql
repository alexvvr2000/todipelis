use todipelis;

DELIMITER //

CREATE FUNCTION funcionCantidadFavoritosUsuario(buscadoIdUsuario INT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE cantidad_favoritos INT;

    -- Verificar si el usuario existe
    IF NOT funcionUsuarioExiste(buscadoIdUsuario) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 100: ListaFavoritos.idUsuario no existe';
    END IF;

    -- Obtener la cantidad de películas favoritas del usuario
    SELECT COUNT(idPelicula) INTO cantidad_favoritos
    FROM ListaFavoritos
    WHERE idUsuario = buscadoIdUsuario;

    RETURN cantidad_favoritos;
END//

DELIMITER ;
