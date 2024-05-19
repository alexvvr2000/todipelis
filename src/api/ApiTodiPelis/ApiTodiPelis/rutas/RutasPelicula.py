from flask import Blueprint, abort, jsonify, request
from ApiTodiPelis.operaciones.Pelicula import obtenerPelicula, obtenerPeliculaTitulo
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.types import Pelicula
from mariadb import Connection
from dataclasses import asdict

rutasPeliculaBlueprint: Blueprint = Blueprint("rutasPelicula", __name__)


@rutasPeliculaBlueprint.route("/pelicula/<string:idPelicula>", methods=["GET"])
def obtenerPeliculaIdBase(idPelicula: str):
    conexion: Connection = obtenerConexion()
    peliculaBase: Pelicula | None = obtenerPelicula(conexion, idPelicula)
    if peliculaBase is None:
        abort(404, description="Pelicula no existe en base")
    return jsonify(peliculaBase)


@rutasPeliculaBlueprint.route("/pelicula", methods=["GET"])
def obtenerPeliculaTituloBase():
    conexion: Connection = obtenerConexion()
    tituloBuscado: str = request.args.get("titulo")
    peliculaBase: Pelicula | None = obtenerPeliculaTitulo(conexion, tituloBuscado)
    if peliculaBase is None:
        abort(404, description="Pelicula no existe en base")
    return jsonify(peliculaBase)


@rutasPeliculaBlueprint.errorhandler(404)
def peliculaNoEncontrada(error):
    return jsonify(error=str(error)), 404
