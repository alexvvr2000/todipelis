from mariadb import Connection, Cursor
from ApiTodiPelis.ApiTodiPelis.types import (
    Pelicula,
    ListaCriticas,
    ListaFavoritos,
    Usuario,
)


def existePelicula(conexion: Connection, idPelicula: str) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute("select funcionPeliculaExiste(?), as existe", (idPelicula,))
    filaRetornada = cursor.fetchone()
    peliculaExiste: bool = filaRetornada[0] == 1
    return peliculaExiste
