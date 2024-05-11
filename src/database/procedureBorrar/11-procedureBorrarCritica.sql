DELIMITER //

CREATE PROCEDURE procedureBorrarCritica(
    IN borradoIdUsuario INT,
    IN borradoIdPelicula INT
)
BEGIN
    DECLARE pelicula_existe BOOLEAN;
    DECLARE usuario_existe BOOLEAN;

    -- Check if the movie exists
    SET pelicula_existe = funcionPeliculaExiste(borradoIdPelicula);
    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 5200: ListaCriticas.idPelicula no existe';
    END IF;

    -- Check if the user exists
    SET usuario_existe = funcionUsuarioExiste(borradoIdUsuario);
    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 5300: ListaCriticas.idUsuario no existe';
    END IF;

    -- Attempt to delete the review
    DELETE FROM ListaCriticas WHERE idUsuario = borradoIdUsuario AND idPelicula = borradoIdPelicula;
    SELECT borradoIdUsuario, borradoIdPelicula;
END//

DELIMITER ;
