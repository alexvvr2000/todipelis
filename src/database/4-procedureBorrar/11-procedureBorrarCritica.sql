use todipelis;

DELIMITER //

CREATE PROCEDURE procedureBorrarCritica(
    IN borradoIdUsuario INT,
    IN borradoIdPelicula VARCHAR(100)
)
BEGIN
    DECLARE pelicula_existe BOOLEAN;
    DECLARE usuario_existe BOOLEAN;
    SET pelicula_existe = funcionPeliculaExiste(borradoIdPelicula);
    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 5200: ListaCriticas.idPelicula no existe';
    END IF;
    SET usuario_existe = funcionUsuarioExiste(borradoIdUsuario);
    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 5300: ListaCriticas.idUsuario no existe';
    END IF;
    DELETE FROM ListaCriticas WHERE idUsuario = borradoIdUsuario AND idPelicula = borradoIdPelicula;
    SELECT borradoIdUsuario, borradoIdPelicula;
END//

DELIMITER ;
