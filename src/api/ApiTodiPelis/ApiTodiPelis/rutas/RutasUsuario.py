from flask import Blueprint, jsonify, request
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Usuario import registrarUsuario
from mariadb import Connection

rutasUsuarioBlueprint: Blueprint = Blueprint("rutasUsuario", __name__)


@rutasUsuarioBlueprint.route("/", methods=["GET"])
def obtenerDatosUsuario():
    return jsonify({"Conexion": "establecida"})


@rutasUsuarioBlueprint.route("/registro", methods=["POST"])
def registrarUsuarioApi():
    conexion: Connection = obtenerConexion()
    correoElectronicoNuevo: str = request.args.get("correoElectronico", "")
    claveAccesoNueva: str = request.args.get("claveAccesso", "")
    nombreUsuarioNuevo: str = request.args.get("nombreUsuario", "")
    nuevaId: int = registrarUsuario(
        conexion, correoElectronicoNuevo, claveAccesoNueva, nombreUsuarioNuevo
    )
    return jsonify({"key": "", "idUsuario": nuevaId})
