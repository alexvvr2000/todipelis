from flask import Blueprint, jsonify, request, abort
from markupsafe import escape
from mariadb import Connection
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Criticas import (
    obtenerCriticasBase,
    agregarCriticaBase,
    borrarCriticaBase,
)
from ApiTodiPelis.types import ListaCriticas, IdUsuarioPelicula
from typing import List
from decimal import Decimal
from datetime import date

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


@rutasCriticasBlueprint.route("/1/criticas", methods=["PUT"])
def actualizarCritica():
    valorActualizableUsuario: str = request.args.get("campo")

    match valorActualizableUsuario:
        case "descripcion":
            descripcionNueva: str = request.args.get("descripcionNueva")
        case "estrellas":
            estrellasNuevas: str = request.args.get("estrellasNuevas")
        case _:
            abort(500)
