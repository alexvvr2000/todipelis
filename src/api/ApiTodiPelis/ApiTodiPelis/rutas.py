from flask import Blueprint, abort, jsonify, request
from ApiTodiPelis.operaciones.select import obtenerPelicula, obtenerPeliculaTitulo
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.types import Pelicula
from mariadb import Connection
from dataclasses import asdict

rutas: Blueprint = Blueprint("rutas", __name__)


@rutas.route("/pelicula/<string:idPelicula>", methods=["GET"])
def obtenerPeliculaIdBase(idPelicula: str):
    conexion: Connection = obtenerConexion()
    peliculaBase: Pelicula | None = obtenerPelicula(conexion, idPelicula)
    if peliculaBase is None:
        abort(404, description="Pelicula no existe en base")
    return asdict(peliculaBase)


@rutas.route("/pelicula", methods=["GET"])
def obtenerPeliculaTituloBase():
    conexion: Connection = obtenerConexion()
    tituloBuscado: str = request.args.get("titulo")
    peliculaBase: Pelicula | None = obtenerPeliculaTitulo(conexion, tituloBuscado)
    if peliculaBase is None:
        abort(404, description="Pelicula no existe en base")
    return asdict(peliculaBase)


@rutas.errorhandler(404)
def peliculaNoEncontrada(error):
    return jsonify(error=str(error)), 404
