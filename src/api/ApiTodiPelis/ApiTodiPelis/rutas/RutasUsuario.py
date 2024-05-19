from flask import Blueprint, jsonify
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.types import Usuario
from ApiTodiPelis.operaciones.Usuario import obtenerDatosUsuarioBase
from mariadb import Connection

rutasUsuarioBlueprint: Blueprint = Blueprint("rutasUsuario", __name__)


@rutasUsuarioBlueprint.route("/1", methods=["GET"])
def obtenerDatosUsuario():
    conexion: Connection = obtenerConexion()
    usuarioBase: Usuario = obtenerDatosUsuarioBase(conexion)
    return jsonify(usuarioBase)
