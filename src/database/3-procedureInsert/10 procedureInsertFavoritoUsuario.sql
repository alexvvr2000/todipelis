DELIMITER //

CREATE PROCEDURE procedureInsertFavoritoUsuario(
    IN insertadoIdUsuario INT,
    IN insertadoIdPelicula INT
)
BEGIN
    DECLARE pelicula_existe BOOLEAN;
    DECLARE usuario_existe BOOLEAN;
    DECLARE cantidad_favoritos INT;

    -- Verificar si la película existe
    SET pelicula_existe = funcionPeliculaExiste(insertadoIdPelicula);
    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4200: Favorito.idPelicula no existe';
    END IF;

    -- Verificar si el usuario existe
    SET usuario_existe = funcionUsuarioExiste(insertadoIdUsuario);
    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4300: Favorito.idUsuario no existe';
    END IF;

    -- Obtener cantidad de favoritos del usuario
    SET cantidad_favoritos = funcionCantidadFavoritosUsuario(insertadoIdUsuario);

    -- Verificar límite de favoritos
    IF cantidad_favoritos >= 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4400: Usuario ha alcanzado el límite de películas favoritas';
    END IF;

    -- Insertar favorito
    INSERT INTO ListaFavoritos (idUsuario, idPelicula) VALUES (insertadoIdUsuario, insertadoIdPelicula);
    SELECT insertadoIdPelicula, insertadoIdPelicula;
END//

DELIMITER ;
