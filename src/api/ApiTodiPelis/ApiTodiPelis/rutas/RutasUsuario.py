from flask import Blueprint, jsonify, request, abort
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Usuario import registrarUsuario, identificarUsuario
from mariadb import Connection
from flask_jwt_extended import create_access_token

rutasUsuarioBlueprint: Blueprint = Blueprint("rutasUsuario", __name__)


@rutasUsuarioBlueprint.route("/", methods=["POST"])
def registrarUsuarioApi():
    conexion: Connection = obtenerConexion()
    correoElectronicoNuevo: str = request.args.get("correoElectronico", "")
    claveAccesoNueva: str = request.args.get("claveAcceso", "")
    nombreUsuarioNuevo: str = request.args.get("nombreUsuario", "")
    nuevaId: int = registrarUsuario(
        conexion, correoElectronicoNuevo, claveAccesoNueva, nombreUsuarioNuevo
    )
    return jsonify({"key": create_access_token(nuevaId)})


@rutasUsuarioBlueprint.route("/", methods=["GET"])
def verificarUsuarioBase():
    conexion: Connection = obtenerConexion()
    correoElectronicoUsuario: str = request.headers.get("correoElectronico", "")
    claveAccesoUsuario: str = request.headers.get("claveAcceso", "")
    if correoElectronicoUsuario == "":
        abort(500)
    if claveAccesoUsuario == "":
        abort(500)
    idUsuarioBase: int = identificarUsuario(
        conexion, correoElectronicoUsuario, claveAccesoUsuario
    )
    return jsonify({"key": create_access_token(idUsuarioBase)})
