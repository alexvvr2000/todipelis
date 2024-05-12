use todipelis;

DELIMITER //

CREATE FUNCTION funcionUsuarioExiste(buscadoIdUsuario INT)
RETURNS BOOLEAN
NOT DETERMINISTIC
BEGIN
    DECLARE existe INT;

    SELECT COUNT(*) INTO existe
    FROM Usuario
    WHERE idUsuario = buscadoIdUsuario;

    IF existe > 0 THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END//

DELIMITER ;

