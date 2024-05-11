use todipelis;

DELIMITER //

CREATE PROCEDURE procedureActualizarListaCriticasDescripcion(
    IN actualizadoIdUsuario INT,
    IN actualizadoIdPelicula INT,
    IN actualizadoDescripcion TEXT
)
BEGIN
    DECLARE pelicula_existe BOOLEAN;
    DECLARE usuario_existe BOOLEAN;
    DECLARE antiguaDescripcion TEXT;

    -- Check if the movie exists
    SET pelicula_existe = funcionPeliculaExiste(actualizadoIdPelicula);
    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 6200: ListaCriticas.idPelicula no existe';
    END IF;

    -- Check if the user exists
    SET usuario_existe = funcionUsuarioExiste(actualizadoIdUsuario);
    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 6300: ListaCriticas.idUsuario no existe';
    END IF;

    -- Check if the description has more than one character
    IF actualizadoDescripcion IS NULL OR LENGTH(actualizadoDescripcion) < 1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 6400: Critica.descripcion debe tener más de un caracter';
    END IF;

    -- Retrieve the current description
    SELECT descripcion INTO antiguaDescripcion 
    FROM ListaCriticas 
    WHERE idUsuario = actualizadoIdUsuario AND idPelicula = actualizadoIdPelicula
    LIMIT 1;

    -- Update the description and modification date
    UPDATE ListaCriticas 
    SET descripcion = actualizadoDescripcion,
        fechaModificado = NOW()
    WHERE idUsuario = actualizadoIdUsuario AND idPelicula = actualizadoIdPelicula;

    -- Return the old description
    SELECT antiguaDescripcion;
END//

DELIMITER ;
