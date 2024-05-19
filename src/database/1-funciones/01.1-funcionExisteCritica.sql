USE todipelis;

DELIMITER //

CREATE FUNCTION funcionExisteCritica(buscadoIdPelicula VARCHAR(100), buscadoIdUsuario INT)
RETURNS BOOLEAN
NOT DETERMINISTIC
BEGIN
    DECLARE existe BOOLEAN;

    SELECT EXISTS(
        SELECT 1 FROM ListaCriticas
        WHERE idUsuario = buscadoIdUsuario AND idPelicula = buscadoIdPelicula
    ) INTO existe;

    RETURN existe;
END//

DELIMITER ;
