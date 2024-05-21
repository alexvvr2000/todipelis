from flask import Blueprint, jsonify
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.types import Usuario
from ApiTodiPelis.operaciones.Usuario import obtenerDatosUsuarioBase
from mariadb import Connection

rutasUsuarioBlueprint: Blueprint = Blueprint("rutasUsuario", __name__)


@rutasUsuarioBlueprint.route("/", methods=["GET"])
def obtenerDatosUsuario():
    return jsonify({"Conexion": "establecida"})
