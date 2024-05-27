from flask import Blueprint, abort, jsonify, request
from ApiTodiPelis.operaciones.Pelicula import obtenerPelicula, obtenerPeliculaTitulo
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.types import Pelicula
from mariadb import Connection

rutasPeliculaBlueprint: Blueprint = Blueprint("rutasPelicula", __name__)


@rutasPeliculaBlueprint.route("/pelicula/<string:idPelicula>", methods=["GET"])
def obtenerPeliculaIdBase(idPelicula: str):
    conexion: Connection = obtenerConexion()
    peliculaBase: Pelicula = obtenerPelicula(conexion, idPelicula)
    return jsonify(peliculaBase)


@rutasPeliculaBlueprint.route("/pelicula", methods=["GET"])
def obtenerPeliculaTituloBase():
    conexion: Connection = obtenerConexion()
    tituloBuscado: str = request.args.get("titulo")
    paginaBusqueda: int = request.args.get("paginaBusqueda", default=-1, type=int)
    if paginaBusqueda <= 0:
        raise Exception("La pagina debe estar ser mayor o igual a 1")
    peliculaBase: Pelicula = obtenerPeliculaTitulo(
        conexion, tituloBuscado, paginaBusqueda
    )
    return jsonify(peliculaBase)


@rutasPeliculaBlueprint.errorhandler(404)
def peliculaNoEncontrada(error):
    return jsonify(error=str(error)), 404
