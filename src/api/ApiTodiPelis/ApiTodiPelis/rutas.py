from flask import Blueprint
from ApiTodiPelis.operaciones.select import obtenerPelicula
from ApiTodiPelis.conexion import obtenerConexion
from mariadb import Connection
from dataclasses import asdict

rutas: Blueprint = Blueprint("rutas", __name__)


@rutas.route("/pelicula/<string:idPelicula>", methods=["GET"])
def ruta(idPelicula: str):
    conexion: Connection = obtenerConexion()
    peliculaBase = obtenerPelicula(conexion, idPelicula)
    return asdict(peliculaBase)
