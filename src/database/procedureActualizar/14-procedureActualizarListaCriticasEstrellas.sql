DELIMITER //

CREATE PROCEDURE procedureActualizarListaCriticasEstrellas(
    IN actualizadoIdUsuario INT,
    IN actualizadoIdPelicula INT,
    IN actualizadoEstrellas DECIMAL(3,2)
)
BEGIN
    DECLARE pelicula_existe BOOLEAN;
    DECLARE usuario_existe BOOLEAN;
    DECLARE antiguaEstrellas DECIMAL(3,2);

    -- Check if the movie exists
    SET pelicula_existe = funcionPeliculaExiste(actualizadoIdPelicula);
    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 7200: ListaCriticas.idPelicula no existe';
    END IF;

    -- Check if the user exists
    SET usuario_existe = funcionUsuarioExiste(actualizadoIdUsuario);
    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 7300: ListaCriticas.idUsuario no existe';
    END IF;

    -- Check if the rating is between 0 and 10
    IF actualizadoEstrellas < 0 OR actualizadoEstrellas > 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 7500: Critica.estrellas debe estar entre 0 y 10';
    END IF;

    -- Retrieve the current rating
    SELECT estrellas INTO antiguaEstrellas 
    FROM ListaCriticas 
    WHERE idUsuario = actualizadoIdUsuario AND idPelicula = actualizadoIdPelicula
    LIMIT 1;

    -- Update the rating and modification date
    UPDATE ListaCriticas 
    SET estrellas = actualizadoEstrellas,
        fechaModificado = NOW()
    WHERE idUsuario = actualizadoIdUsuario AND idPelicula = actualizadoIdPelicula;

    -- Return the old rating
    SELECT antiguaEstrellas;
END//

DELIMITER ;
