from flask import Blueprint, jsonify, request, abort
from markupsafe import escape
from mariadb import Connection
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Criticas import (
    obtenerCriticasBase,
    agregarCriticaBase,
    borrarCriticaBase,
    estrellasValidas,
    actualizarEstrellasBase,
    actualizarDescripcionCriticaBase,
    obtenerCriticaUsuarioBase,
)
from ApiTodiPelis.types import ListaCriticas, IdUsuarioPelicula
from typing import List
from decimal import Decimal, getcontext
from datetime import date
from flask_jwt_extended import jwt_required

getcontext().prec = 2

rutasCriticasBlueprint: Blueprint = Blueprint("rutasCritcas", __name__)


@rutasCriticasBlueprint.route("/criticas/", methods=["GET"])
@jwt_required()
def obtenerCriticas():
    conexion: Connection = obtenerConexion()
    criticasBase: List[ListaCriticas] = obtenerCriticasBase(conexion)
    return jsonify(
        {"cantidadCriticas": len(criticasBase), "criticasUsuario": criticasBase}
    )


@rutasCriticasBlueprint.route("/criticas/<string:idPelicula>", methods=["GET"])
@jwt_required()
def obtenerCriticaUsuario(idPelicula: str):
    conexion: Connection = obtenerConexion()
    idUsuarioActual: int = 1
    criticaBase: ListaCriticas = obtenerCriticaUsuarioBase(
        conexion, IdUsuarioPelicula(idUsuarioActual, idPelicula)
    )
    return jsonify(criticaBase)


@rutasCriticasBlueprint.route("/criticas", methods=["POST"])
@jwt_required()
def agregarCritica():
    conexion: Connection = obtenerConexion()
    idUsuarioActual: int = 1
    nuevaCritica: ListaCriticas = ListaCriticas(
        idCritica=IdUsuarioPelicula(idUsuarioActual, request.args.get("idPelicula")),
        descripcion=request.args.get("descripcion"),
        estrellas=Decimal(request.args.get("estrellas")),
        fechaAgregado=date.today(),
        fechaModificado=None,
    )
    criticaBase: IdUsuarioPelicula = agregarCriticaBase(conexion, nuevaCritica)
    return jsonify(criticaBase)


@rutasCriticasBlueprint.route("/criticas", methods=["DELETE"])
@jwt_required()
def borrarCritica():
    conexion: Connection = obtenerConexion()
    peliculaBorrada: str = request.args.get("idPelicula")
    idUsuarioActual: int = 1
    idCriticaBorrada: str = borrarCriticaBase(
        conexion, IdUsuarioPelicula(idUsuarioActual, peliculaBorrada)
    )
    return jsonify(idCriticaBorrada)


@rutasCriticasBlueprint.route("/criticas/<string:idPelicula>", methods=["PUT"])
@jwt_required()
def actualizarCritica(idPelicula: str):
    nuevasEstrellas: Decimal = Decimal(request.args.get("estrellas", "-1.0", type=str))
    nuevaDescripcion: str = request.args.get("descripcion", "", type=str)
    idUsuarioActual: int = 1
    idUsuarioPelicula: IdUsuarioPelicula = IdUsuarioPelicula(
        idUsuarioActual, idPelicula
    )
    conexion: Connection = obtenerConexion()
    respuesta = {
        "idCritica": {
            "idPelicula": idUsuarioPelicula.idPelicula,
            "idUsuario": idUsuarioPelicula.idUsuario,
        },
    }
    if (not nuevasEstrellas == Decimal("-1.0")) and estrellasValidas(nuevasEstrellas):
        viejasEstrellas: Decimal = actualizarEstrellasBase(
            conexion, idUsuarioPelicula, nuevasEstrellas
        )
        respuesta["viejasEstrellas"] = viejasEstrellas
    if not nuevaDescripcion == "":
        viejaDescripcion: str = actualizarDescripcionCriticaBase(
            conexion, idUsuarioPelicula, nuevaDescripcion
        )
        respuesta["viejaDescripcion"] = viejaDescripcion
    return jsonify(respuesta)
