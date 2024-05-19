from mariadb import Connection, Cursor
from ApiTodiPelis.ApiTodiPelis.types import (
    Pelicula,
    ListaCriticas,
    ListaFavoritos,
    Usuario,
)


def existeUsuario(conexion: Connection, idUsuario: int) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute("select funcionUsuarioExiste(?) as existe", (idUsuario,))
    filaRetornada = cursor.fetchone()
    usuarioExiste: bool = filaRetornada[0] == 1
    return usuarioExiste


def existePelicula(conexion: Connection, idPelicula: str) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute("select funcionPeliculaExiste(?), as existe", (idPelicula,))
    filaRetornada = cursor.fetchone()
    peliculaExiste: bool = filaRetornada[0] == 1
    return peliculaExiste
