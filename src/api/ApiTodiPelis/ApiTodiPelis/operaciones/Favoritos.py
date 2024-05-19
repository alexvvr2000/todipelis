from mariadb import Connection, Cursor
from ApiTodiPelis.types import ListaFavoritos, IdUsuarioPelicula
from typing import List


def cantidadFavoritosUsuario(conexion: Connection) -> int:
    cursor: Cursor = conexion.cursor()
    cursor.execute("SELECT funcionCantidadFavoritosUsuario(1) as cantidad")
    valorRetornado = cursor.fetchone()
    return int(valorRetornado[0])


def obtenerFavoritos(conexion: Connection) -> List[ListaFavoritos]:
    cursor: Cursor = conexion.cursor()
    cursor.callproc("procedureObtenerFavoritos", (1,))

    valoresBase: List[ListaFavoritos] = []
    favoritoActual = cursor.fetchone()
    while favoritoActual is not None:
        valoresBase.append(
            ListaFavoritos(idFavorito=IdUsuarioPelicula(1, favoritoActual[0]))
        )
        favoritoActual = cursor.fetchone()
    return valoresBase
