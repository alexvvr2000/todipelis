use todipelis;

DELIMITER //

CREATE FUNCTION funcionPeliculaExiste(buscadoIdPelicula VARCHAR(100))
RETURNS BOOLEAN
NOT DETERMINISTIC
BEGIN
    DECLARE existe INT;

    -- Verificar si la película existe
    SELECT COUNT(*) INTO existe
    FROM Pelicula
    WHERE idPelicula = buscadoIdPelicula;

    -- Retornar TRUE si la película existe, FALSE si no
    IF existe > 0 THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END//

DELIMITER ;
