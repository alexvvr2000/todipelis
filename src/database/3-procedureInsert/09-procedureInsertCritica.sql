use todipelis;

DELIMITER //

CREATE PROCEDURE procedureInsertCritica(
    IN insertadoIdUsuario INT,
    IN insertadoIdPelicula VARCHAR(100),
    IN insertadoDescripcion TEXT,
    IN insertadoEstrellas DECIMAL(3,2)
)
BEGIN
    DECLARE pelicula_existe BOOLEAN;
    DECLARE usuario_existe BOOLEAN;
    SET pelicula_existe = funcionPeliculaExiste(insertadoIdPelicula);
    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 3200: Critica.idPelicula no existe';
    END IF;
    SET usuario_existe = funcionUsuarioExiste(insertadoIdUsuario);
    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 3300: Critica.idUsuario no existe';
    END IF;
    IF insertadoDescripcion IS NOT NULL AND LENGTH(insertadoDescripcion) < 2 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 3400: Critica.descripcion debe tener más de un caracter';
    END IF;
    IF insertadoEstrellas < 0 OR insertadoEstrellas > 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 3500: Critica.estrellas debe estar entre 0 y 10';
    END IF;
    INSERT INTO ListaCriticas (idUsuario, idPelicula, descripcion, estrellas, fechaAgregado)
    VALUES (insertadoIdUsuario, insertadoIdPelicula, insertadoDescripcion, insertadoEstrellas, NOW());
    SELECT insertadoIdUsuario, insertadoIdPelicula;
END//

DELIMITER ;
