from flask import Blueprint, jsonify, request, abort
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Usuario import registrarUsuario, identificarUsuario
from mariadb import Connection
from flask_jwt_extended import create_access_token, jwt_required

rutasUsuarioBlueprint: Blueprint = Blueprint("rutasUsuario", __name__)


@rutasUsuarioBlueprint.route("/", methods=["POST"])
@jwt_required(optional=True)
def registrarUsuarioApi():
    conexion: Connection = obtenerConexion()
    correoElectronicoNuevo: str = request.headers.get("correoElectronico", "")
    claveAccesoNueva: str = request.headers.get("claveAcceso", "")
    nombreUsuarioNuevo: str = request.headers.get("nombreUsuario", "")
    nuevaId: int = registrarUsuario(
        conexion, correoElectronicoNuevo, claveAccesoNueva, nombreUsuarioNuevo
    )
    return jsonify({"key": create_access_token(nuevaId)})


@rutasUsuarioBlueprint.route("/", methods=["GET"])
@jwt_required(optional=True)
def verificarUsuarioBase():
    conexion: Connection = obtenerConexion()
    correoElectronicoUsuario: str = request.headers.get("correoElectronico", "")
    claveAccesoUsuario: str = request.headers.get("claveAcceso", "")
    idUsuarioBase: int = identificarUsuario(
        conexion, correoElectronicoUsuario, claveAccesoUsuario
    )
    return jsonify({"key": create_access_token(idUsuarioBase)})
