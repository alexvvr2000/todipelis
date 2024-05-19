from flask import Blueprint, jsonify
from mariadb import Connection
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Criticas import obtenerCriticasBase
from ApiTodiPelis.types import ListaCriticas
from typing import List

rutasCriticasBlueprint: Blueprint = Blueprint("rutasCritcas", __name__)


@rutasCriticasBlueprint.route("/1/criticas/", methods=["GET"])
def obtenerCriticas():
    conexion: Connection = obtenerConexion()
    criticasBase: List[ListaCriticas] = obtenerCriticasBase(conexion)
    return jsonify(
        {"cantidadCriticas": len(criticasBase), "criticasUsuario": criticasBase}
    )
