CREATE DATABASE IF NOT EXISTS todipelis;
use todopelis;

-- Crear la tabla Usuario
CREATE TABLE Usuario (
    idUsuario INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    urlFotoPerfil CHAR(255) NULL
);

-- Crear la tabla Pelicula
CREATE TABLE Pelicula (
    idPelicula VARCHAR(100) PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    genero VARCHAR(255) NOT NULL,
    urlPoster VARCHAR(255) NOT NULL,
    rating DECIMAL(4,2) NOT NULL,
    sinopsis TEXT NOT NULL
);

-- Crear la tabla ListaCriticas
CREATE TABLE ListaCriticas (
    idUsuario INT UNSIGNED,
    idPelicula VARCHAR(100),
    descripcion TEXT NULL,
    estrellas DECIMAL(3,2) UNSIGNED NOT NULL,
    fechaAgregado DATE NOT NULL,
    fechaModificado DATETIME NULL,
    PRIMARY KEY (idUsuario, idPelicula),
    FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario) ON DELETE CASCADE,
    FOREIGN KEY (idPelicula) REFERENCES Pelicula(idPelicula) ON DELETE CASCADE
);

-- Crear la tabla ListaFavoritos
CREATE TABLE ListaFavoritos (
    idUsuario INT UNSIGNED,
    idPelicula VARCHAR(100),
    PRIMARY KEY (idUsuario, idPelicula),
    FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario) ON DELETE CASCADE,
    FOREIGN KEY (idPelicula) REFERENCES Pelicula(idPelicula) ON DELETE CASCADE
);

INSERT INTO Usuario(urlFotoPerfil) VALUES(NULL);

INSERT INTO Pelicula (idPelicula, titulo, genero, urlPoster, rating, sinopsis)
VALUES
    ('tt0133093', 'The Matrix', 'Action, Sci-Fi', 'https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg', 8.7, 'When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.'),
    ('tt0167260', 'The Lord of the Rings: The Return of the King', 'Action, Adventure, Drama', 'https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg', 9.0, 'Gandalf and Aragorn lead the World of Men against Sauron''s army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.'),
    ('tt0120737', 'The Lord of the Rings: The Fellowship of the Ring', 'Action, Adventure, Drama', 'https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SX300.jpg', 8.9, 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.'),
    ('tt0137523', 'Fight Club', 'Drama', 'https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg', 8.8, 'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.'),
    ('tt0110912', 'Pulp Fiction', 'Crime, Drama', 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg', 8.9, 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'),
    ('tt0109830', 'Forrest Gump', 'Drama, Romance', 'https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 8.8, 'The history of the United States from the 1950s to the ''70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.'),
    ('tt0120815', 'Saving Private Ryan', 'Drama, War', 'https://m.media-amazon.com/images/M/MV5BZjhkMDM4MWItZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SX300.jpg', 8.6, 'Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.'),
    ('tt0241527', 'Harry Potter and the Sorcerer''s Stone', 'Adventure, Family, Fantasy', 'https://m.media-amazon.com/images/M/MV5BNmQ0ODBhMjUtNDRhOC00MGQzLTk5MTAtZDliODg5NmU5MjZhXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_SX300.jpg', 7.6, 'An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.'),
    ('tt0120586', 'American History X', 'Crime, Drama', 'https://m.media-amazon.com/images/M/MV5BZTJhN2FkYWEtMGI0My00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNjc3MjQzNTI@._V1_SX300.jpg', 8.5, 'Living a life marked by violence, neo-Nazi Derek finally goes to prison after killing two black youths. Upon his release, Derek vows to change; he hopes to prevent his brother, Danny, who idolizes Derek, from following in his foot...'),
    ('tt0167261', 'The Lord of the Rings: The Two Towers', 'Action, Adventure, Drama', 'https://m.media-amazon.com/images/M/MV5BZGMxZTdjZmYtMmE2Ni00ZTdkLWI5NTgtNjlmMjBiNzU2MmI5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg', 8.8, 'While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron''s new ally, Saruman, and his hordes of Isengard.');