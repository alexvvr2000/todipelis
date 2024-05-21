from flask import Blueprint, jsonify, request
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Usuario import registrarUsuario
from mariadb import Connection
from flask_jwt_extended import create_access_token

rutasUsuarioBlueprint: Blueprint = Blueprint("rutasUsuario", __name__)


@rutasUsuarioBlueprint.route("/registro", methods=["POST"])
def registrarUsuarioApi():
    conexion: Connection = obtenerConexion()
    correoElectronicoNuevo: str = request.args.get("correoElectronico", "")
    claveAccesoNueva: str = request.args.get("claveAcceso", "")
    nombreUsuarioNuevo: str = request.args.get("nombreUsuario", "")
    nuevaId: int = registrarUsuario(
        conexion, correoElectronicoNuevo, claveAccesoNueva, nombreUsuarioNuevo
    )
    return jsonify({"key": create_access_token(nuevaId)})
