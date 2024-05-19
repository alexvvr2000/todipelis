from mariadb import Connection, Cursor
from ApiTodiPelis.types import Pelicula
from ApiTodiPelis.conexion import existePeliculaBase, obtenerConexion
from flask import g


def agregarPeliculaBase(conexion: Connection, pelicula: Pelicula) -> str:
    if existePeliculaBase(conexion, pelicula.idPelicula):
        raise Exception(f"Pelicula con id {pelicula.idPelicula} ya esta en base")
    cursor: Cursor = conexion.cursor()
    cursor.callproc(
        "procedureInsertPelicula",
        (
            pelicula.idPelicula,
            pelicula.titulo,
            pelicula.genero,
            pelicula.urlPoster,
            pelicula.rating,
            pelicula.sinopsis,
        ),
    )
    idInsertado = cursor.fetchone()
    cursor.close()
    conexion.commit()
    return idInsertado[0]
