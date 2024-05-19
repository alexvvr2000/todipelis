from mariadb import Connection, Cursor
from ApiTodiPelis.types import IdUsuarioPelicula


def cantidadFavoritosUsuario(conexion: Connection) -> int:
    cursor: Cursor = conexion.cursor()
    cursor.execute("SELECT funcionCantidadFavoritosUsuario(1) as cantidad")
    valorRetornado = cursor.fetchone()
    return int(valorRetornado[0])
