USE todipelis;

DELIMITER //

CREATE PROCEDURE procedureInsertPelicula(
    IN insertadoIdPelicula VARCHAR(100),
    IN nuevoTitulo VARCHAR(255),
    IN nuevoGenero VARCHAR(255),
    IN nuevoUrlPoster VARCHAR(255),
    IN rating DECIMAL(4,2),
    IN sinopsis TEXT
)
BEGIN
    IF LENGTH(nuevoTitulo) = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 2200: Pelicula.titulo debe tener 1 caracter o más';
    END IF;

    IF LENGTH(nuevoGenero) = 0 AND nuevoGenero IS NOT NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 2300: Pelicula.genero debe tener 1 caracter o más';
    END IF;

    IF LENGTH(nuevoUrlPoster) = 0 AND nuevoUrlPoster IS NOT NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 2400: Pelicula.urlPoster debe tener 1 caracter o más';
    END IF;

    IF (rating < 0 OR rating > 10) AND rating IS NOT NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 2500: Pelicula.rating debe estar entre 0 y 10';
    END IF;

    IF LENGTH(sinopsis) = 0 AND sinopsis IS NOT NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 2600: Pelicula.sinopsis debe tener 1 caracter o más';
    END IF;

    IF funcionPeliculaExiste(insertadoIdPelicula) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error 2700: Pelicula.idPelicula ya existe en la base de datos';
    END IF;

    INSERT INTO Pelicula (idPelicula, titulo, genero, urlPoster, rating, sinopsis)
    VALUES (insertadoIdPelicula, nuevoTitulo, nuevoGenero, nuevoUrlPoster, rating, sinopsis);

    SELECT insertadoIdPelicula;
END//

DELIMITER ;
