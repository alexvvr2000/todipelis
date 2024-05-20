use todipelis;

DELIMITER //

CREATE PROCEDURE procedureInsertFavoritoUsuario(
    IN insertadoIdUsuario INT,
    IN insertadoIdPelicula INT
)
BEGIN
    DECLARE pelicula_existe BOOLEAN;
    DECLARE usuario_existe BOOLEAN;
    DECLARE cantidad_favoritos INT;
    SET pelicula_existe = funcionPeliculaExiste(insertadoIdPelicula);
    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4200: Favorito.idPelicula no existe';
    END IF;
    SET usuario_existe = funcionUsuarioExiste(insertadoIdUsuario);
    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4300: Favorito.idUsuario no existe';
    END IF;
    SET cantidad_favoritos = funcionCantidadFavoritosUsuario(insertadoIdUsuario);
    IF cantidad_favoritos >= 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 4400: Usuario ha alcanzado el límite de películas favoritas';
    END IF;
    INSERT INTO ListaFavoritos (idUsuario, idPelicula) VALUES (insertadoIdUsuario, insertadoIdPelicula);
    SELECT insertadoIdUsuario, insertadoIdPelicula;
END//

DELIMITER ;
