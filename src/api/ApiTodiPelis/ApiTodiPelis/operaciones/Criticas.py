from mariadb import Connection, Cursor
from ApiTodiPelis.types import ListaCriticas, IdUsuarioPelicula
from decimal import Decimal
from typing import List
from datetime import datetime


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
    return IdUsuarioPelicula(1, 1)
