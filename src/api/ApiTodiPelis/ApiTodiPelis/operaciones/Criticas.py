from mariadb import Connection, Cursor
from ApiTodiPelis.types import ListaCriticas, IdUsuarioPelicula, Pelicula
from ApiTodiPelis.operaciones.Pelicula import (
    existePeliculaApi,
    existePeliculaBase,
    agregarPeliculaBase,
    obtenerPeliculaIdApi,
)
from decimal import Decimal, getcontext
from typing import List
from datetime import datetime

getcontext().prec = 2


def estrellasValidas(estrellas: Decimal) -> bool:
    return Decimal("0.0") <= estrellas and estrellas <= Decimal("5.0")


def existeCriticaBase(conexion: Connection, idPeliculaIdApi: IdUsuarioPelicula) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute(
        "select funcionExisteCritica(?,?) as existe",
        [idPeliculaIdApi.idPelicula, idPeliculaIdApi.idUsuario],
    )
    filaRetornada = cursor.fetchone()
    return filaRetornada[0] == 1


def obtenerCriticasBase(conexion: Connection) -> List[ListaCriticas]:
    cursor: Cursor = conexion.cursor()
    cursor.callproc("procedureCriticasUsuario", (1,))

    valoresBase: List[ListaCriticas] = []
    criticaActual = cursor.fetchone()
    while criticaActual is not None:
        fechaModificado: datetime | None = None
        if criticaActual[4] is not None:
            fechaModificado = datetime.strptime(
                str(criticaActual[4]), "%Y-%m-%d %H:%M:%S"
            )
        valoresBase.append(
            ListaCriticas(
                idCritica=IdUsuarioPelicula(1, criticaActual[0]),
                descripcion=criticaActual[1],
                estrellas=Decimal(criticaActual[2]),
                fechaAgregado=datetime.strptime(
                    str(criticaActual[3]), "%Y-%m-%d"
                ).date(),
                fechaModificado=fechaModificado,
            )
        )
        criticaActual = cursor.fetchone()
    return valoresBase


def agregarCriticaBase(
    conexion: Connection, criticaNueva: ListaCriticas
) -> IdUsuarioPelicula:
    if existeCriticaBase(conexion, criticaNueva.idCritica):
        raise Exception("Usuario ya tiene una critica de la pelicula dada")
    if not existePeliculaApi(criticaNueva.idCritica.idPelicula):
        raise Exception("Pelicula no existe en base")
    if not existePeliculaBase(conexion, criticaNueva.idCritica.idPelicula):
        peliculaNueva: Pelicula = obtenerPeliculaIdApi(
            criticaNueva.idCritica.idPelicula
        )
        agregarPeliculaBase(conexion, peliculaNueva)

    cursor: Cursor = conexion.cursor()
    cursor.callproc(
        "procedureInsertCritica",
        [
            criticaNueva.idCritica.idUsuario,
            criticaNueva.idCritica.idPelicula,
            criticaNueva.descripcion,
            criticaNueva.estrellas,
        ],
    )
    cursor.close()
    conexion.commit()
    return criticaNueva.idCritica


def borrarCriticaBase(conexion: Connection, idUsuarioPelicula: IdUsuarioPelicula):
    if not existeCriticaBase(conexion, idUsuarioPelicula):
        raise Exception("Critica no existe en base")
    cursor: Cursor = conexion.cursor()
    cursor.callproc(
        "procedureBorrarCritica",
        [idUsuarioPelicula.idUsuario, idUsuarioPelicula.idPelicula],
    )
    cursor.close()
    conexion.commit()
    return idUsuarioPelicula


def actualizarEstrellasBase(
    conexion: Connection, idUsuarioPelicula: IdUsuarioPelicula, nuevasEstrellas: Decimal
) -> Decimal:
    if not estrellasValidas(nuevasEstrellas):
        raise Exception("Estrellas deben estar entre 0 y 5")
    cursor: Cursor = conexion.cursor()
    cursor.callproc(
        "procedureActualizarListaCriticasEstrellas",
        [idUsuarioPelicula.idUsuario, idUsuarioPelicula.idPelicula, nuevasEstrellas],
    )
    filaRetornada = cursor.fetchone()
    cursor.close()
    conexion.commit()
    return Decimal(filaRetornada[0])


def actualizarDescripcionCriticaBase(
    conexion: Connection, idUsuarioPelicula: IdUsuarioPelicula, nuevaDescripcion: str
) -> str:
    if nuevaDescripcion == "":
        raise Exception("Descripcion nueva invalida")
    cursor: Cursor = conexion.cursor()
    cursor.callproc(
        "procedureActualizarListaCriticasDescripcion",
        [idUsuarioPelicula.idUsuario, idUsuarioPelicula.idPelicula, nuevaDescripcion],
    )
    filaRetornada = cursor.fetchone()
    cursor.close()
    conexion.commit()
    return filaRetornada[0]
