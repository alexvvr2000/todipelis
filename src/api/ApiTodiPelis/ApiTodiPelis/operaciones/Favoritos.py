from mariadb import Connection, Cursor
from ApiTodiPelis.types import (
    ListaFavoritos,
    IdUsuarioPelicula,
    Pelicula,
)
from ApiTodiPelis.operaciones.Pelicula import (
    existePeliculaBase,
    existePeliculaApi,
    agregarPeliculaBase,
    obtenerPeliculaIdApi,
)
from typing import List


def peliculaEnFavoritos(conexion: Connection, idPelicula: str) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute("SELECT funcionEstaEnFavoritos(?, ?) as existe", [idPelicula, 1])
    filaRetornada = cursor.fetchone()
    cursor.close()
    return filaRetornada[0] == 1


def cantidadFavoritosUsuario(conexion: Connection) -> int:
    cursor: Cursor = conexion.cursor()
    cursor.execute("SELECT funcionCantidadFavoritosUsuario(?) as cantidad", [1])
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


def agregarFavoritoBase(conexion: Connection, idPelicula: str) -> IdUsuarioPelicula:
    if cantidadFavoritosUsuario(conexion) == 5:
        raise Exception("Ya se llego al limite de favoritos en usuario")
    if peliculaEnFavoritos(conexion, idPelicula):
        raise Exception("Pelicula ya esta incluida en favoritos de usuario")
    if not existePeliculaApi(idPelicula):
        raise Exception("Pelicula no existe en base")
    if not existePeliculaBase(conexion, idPelicula):
        peliculaNueva: Pelicula = obtenerPeliculaIdApi(idPelicula)
        agregarPeliculaBase(conexion, peliculaNueva)
    cursor: Cursor = conexion.cursor()
    cursor.callproc("procedureInsertFavoritoUsuario", [1, idPelicula])
    filaRetornada = cursor.fetchone()
    cursor.close()
    conexion.commit()
    return IdUsuarioPelicula(filaRetornada[0], filaRetornada[1])


def borrarFavoritoBase(
    conexion: Connection, idUsuarioPelicula: IdUsuarioPelicula
) -> IdUsuarioPelicula:
    if not existePeliculaBase(conexion, idUsuarioPelicula.idPelicula):
        raise Exception("Pelicula no existe en base")
    cursor: Cursor = conexion.cursor()
    cursor.callproc(
        "procedureBorrarFavorito",
        [idUsuarioPelicula.idUsuario, idUsuarioPelicula.idPelicula],
    )
    filaRetornada = cursor.fetchone()
    cursor.close()
    conexion.commit()
    return IdUsuarioPelicula(filaRetornada[0], filaRetornada[1])
