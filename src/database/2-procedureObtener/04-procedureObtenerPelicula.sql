use todipelis;

DELIMITER //

CREATE PROCEDURE procedureObtenerPelicula(IN idPeliculaBuscada VARCHAR(100))
BEGIN
    DECLARE pelicula_existe BOOLEAN;

    SET pelicula_existe = funcionPeliculaExiste(idPeliculaBuscada);

    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 200: Pelicula.idPelicula no existe';
    END IF;

    SELECT titulo, genero, urlPoster, rating
    FROM Pelicula
    WHERE idPelicula = idPeliculaBuscada;
END//

DELIMITER ;
