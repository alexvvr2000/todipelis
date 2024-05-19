from flask import Blueprint, abort, jsonify
from ApiTodiPelis.operaciones.select import obtenerPelicula
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.types import Pelicula
from mariadb import Connection
from dataclasses import asdict

rutas: Blueprint = Blueprint("rutas", __name__)


@rutas.route("/pelicula/<string:idPelicula>", methods=["GET"])
def ruta(idPelicula: str):
    conexion: Connection = obtenerConexion()
    peliculaBase: Pelicula | None = obtenerPelicula(conexion, idPelicula)
    if peliculaBase is None:
        abort(404, description="Pelicula no existe en base")
    return asdict(peliculaBase)


@rutas.errorhandler(404)
def peliculaNoEncontrada(error):
    return jsonify(error=str(error)), 404
