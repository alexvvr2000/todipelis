from flask import Blueprint, jsonify, request, abort
from markupsafe import escape
from mariadb import Connection
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Criticas import (
    obtenerCriticasBase,
    agregarCriticaBase,
    borrarCriticaBase,
    estrellasValidas,
)
from ApiTodiPelis.types import ListaCriticas, IdUsuarioPelicula
from typing import List
from decimal import Decimal, getcontext
from datetime import date

getcontext().prec = 2

rutasCriticasBlueprint: Blueprint = Blueprint("rutasCritcas", __name__)


@rutasCriticasBlueprint.route("/1/criticas/", methods=["GET"])
def obtenerCriticas():
    conexion: Connection = obtenerConexion()
    criticasBase: List[ListaCriticas] = obtenerCriticasBase(conexion)
    return jsonify(
        {"cantidadCriticas": len(criticasBase), "criticasUsuario": criticasBase}
    )


@rutasCriticasBlueprint.route("/1/criticas", methods=["POST"])
def agregarCritica():
    conexion: Connection = obtenerConexion()
    nuevaCritica: ListaCriticas = ListaCriticas(
        idCritica=IdUsuarioPelicula(1, request.args.get("idPelicula")),
        descripcion=request.args.get("descripcion"),
        estrellas=Decimal(request.args.get("estrellas")),
        fechaAgregado=date.today(),
        fechaModificado=None,
    )
    criticaBase: IdUsuarioPelicula = agregarCriticaBase(conexion, nuevaCritica)
    return jsonify(criticaBase)


@rutasCriticasBlueprint.route("/1/criticas", methods=["DELETE"])
def borrarCritica():
    conexion: Connection = obtenerConexion()
    peliculaBorrada: str = request.args.get("idPelicula")
    idCriticaBorrada: str = borrarCriticaBase(
        conexion, IdUsuarioPelicula(1, peliculaBorrada)
    )
    return jsonify(idCriticaBorrada)


@rutasCriticasBlueprint.route("/1/criticas/<string:idPelicula>", methods=["PUT"])
def actualizarCritica(idPelicula: str):
    nuevasEstrellas: Decimal = Decimal(request.args.get("estrellas", "-1.0", type=str))
    nuevaDescripcion: str = request.args.get("descripcion", "", type=str)
    if not estrellasValidas(nuevasEstrellas):
        raise Exception("Estrellas deben estar entre 0 y 5")
    if (not nuevasEstrellas == Decimal("-1.0")) and estrellasValidas(nuevasEstrellas):
        pass
    if not nuevaDescripcion == "":
        pass
