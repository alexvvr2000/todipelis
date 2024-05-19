from mariadb import Connection, Cursor
from ApiTodiPelis.types import (
    Pelicula,
    ListaCriticas,
    ListaFavoritos,
    Usuario,
)


def existePeliculaBase(conexion: Connection, idPelicula: str) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute("select funcionPeliculaExiste(?) as existe", (idPelicula,))
    filaRetornada = cursor.fetchone()
    peliculaExiste: bool = filaRetornada[0] == 1
    return peliculaExiste


def obtenerPelicula(conexion: Connection, idPelicula: str) -> Pelicula | None:
    peliculaBase: Pelicula | None
    if existePeliculaBase(conexion, idPelicula):
        cursor: Cursor = conexion.cursor()
        cursor.callproc("procedureObtenerPelicula", (idPelicula,))
        filaRetornada = cursor.fetchone()
        print(filaRetornada)
        peliculaBase: Pelicula = Pelicula(
            idPelicula=idPelicula,
            titulo=[0],
            genero=filaRetornada[1],
            urlPoster=filaRetornada[2],
            rating=filaRetornada[3],
            sinopsis=filaRetornada[4],
        )
        return peliculaBase
    else:
        peliculaBase = None
    return peliculaBase
