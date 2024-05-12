use todipelis;

DELIMITER //

CREATE FUNCTION funcionPeliculaExiste(buscadoIdPelicula VARCHAR(100))
RETURNS BOOLEAN
NOT DETERMINISTIC
BEGIN
    DECLARE existe INT;

    SELECT COUNT(*) INTO existe
    FROM Pelicula
    WHERE idPelicula = buscadoIdPelicula;

    IF existe > 0 THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END//

DELIMITER ;
