USE todipelis;

DELIMITER //

CREATE FUNCTION funcionEstaEnFavoritos(buscadoIdPelicula VARCHAR(100), buscadoIdUsuario INT)
RETURNS BOOLEAN
NOT DETERMINISTIC
BEGIN
    DECLARE existe BOOLEAN;

    SELECT EXISTS(
        SELECT 1 FROM ListaFavoritos
        WHERE idUsuario = buscadoIdUsuario AND idPelicula = buscadoIdPelicula
    ) INTO existe;

    RETURN existe;
END//

DELIMITER ;
