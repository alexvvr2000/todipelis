DELIMITER //

CREATE FUNCTION funcionUsuarioExiste(buscadoIdUsuario INT)
RETURNS BOOLEAN
NOT DETERMINISTIC
BEGIN
    DECLARE existe INT;

    -- Verificar si el usuario existe
    SELECT COUNT(*) INTO existe
    FROM Usuario
    WHERE idUsuario = buscadoIdUsuario;

    -- Retornar TRUE si el usuario existe, FALSE si no
    IF existe > 0 THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END//

DELIMITER ;

