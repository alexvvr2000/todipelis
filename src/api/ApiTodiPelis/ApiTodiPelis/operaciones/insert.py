from mariadb import Connection, Cursor
from ApiTodiPelis.types import Pelicula
from ApiTodiPelis.conexion import existePeliculaBase, obtenerConexion
from flask import g


def agregarPeliculaBase(pelicula: Pelicula) -> str:
    conexion: Connection = obtenerConexion()
    if existePeliculaBase(pelicula.idPelicula):
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
    conexion.commit()
    idInsertado = cursor.fetchone()
    cursor.close()
    return idInsertado[0]
