use todipelis;

DELIMITER //

CREATE PROCEDURE procedureActualizarListaCriticasEstrellas(
    IN actualizadoIdUsuario INT,
    IN actualizadoIdPelicula VARCHAR(100),
    IN actualizadoEstrellas DECIMAL(3,2)
)
BEGIN
    DECLARE pelicula_existe BOOLEAN;
    DECLARE usuario_existe BOOLEAN;
    DECLARE antiguaEstrellas DECIMAL(3,2);
    SET pelicula_existe = funcionPeliculaExiste(actualizadoIdPelicula);
    IF NOT pelicula_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 7200: ListaCriticas.idPelicula no existe';
    END IF;
    SET usuario_existe = funcionUsuarioExiste(actualizadoIdUsuario);
    IF NOT usuario_existe THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 7300: ListaCriticas.idUsuario no existe';
    END IF;
    IF actualizadoEstrellas < 0 OR actualizadoEstrellas > 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 7500: Critica.estrellas debe estar entre 0 y 10';
    END IF;
    SELECT estrellas INTO antiguaEstrellas 
    FROM ListaCriticas 
    WHERE idUsuario = actualizadoIdUsuario AND idPelicula = actualizadoIdPelicula
    LIMIT 1;
    UPDATE ListaCriticas 
    SET estrellas = actualizadoEstrellas,
        fechaModificado = NOW()
    WHERE idUsuario = actualizadoIdUsuario AND idPelicula = actualizadoIdPelicula;
    SELECT antiguaEstrellas;
END//

DELIMITER ;
