from flask import Blueprint, jsonify, request, abort
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Favoritos import (
    obtenerFavoritos,
    agregarFavoritoBase,
    borrarFavoritoBase,
)
from ApiTodiPelis.types import ListaFavoritos, IdUsuarioPelicula
from mariadb import Connection
from typing import List

rutasFavoritosBlueprint: Blueprint = Blueprint("rutasFavoritos", __name__)


@rutasFavoritosBlueprint.route("/1/favoritos/", methods=["GET"])
def obtenerFavoritosUsuario():
    conexion: Connection = obtenerConexion()
    favoritosUsuario: List[ListaFavoritos] = obtenerFavoritos(conexion)
    return jsonify(
        {
            "cantidadFavoritos": len(favoritosUsuario),
            "favoritosUsuario": favoritosUsuario,
        }
    )


@rutasFavoritosBlueprint.route("/1/favoritos", methods=["POST"])
def agregarFavoritoUsuario():
    conexion: Connection = obtenerConexion()
    idPeliculaAgregada: str = request.args.get("idPelicula", "", type=str)
    if idPeliculaAgregada == "":
        abort(404)
    nuevoFavorito: IdUsuarioPelicula = agregarFavoritoBase(conexion, idPeliculaAgregada)
    return jsonify(
        {
            "idFavorito": {
                "idPelicula": nuevoFavorito.idPelicula,
                "idUsuario": nuevoFavorito.idUsuario,
            }
        }
    )


@rutasFavoritosBlueprint.route("/1/favoritos", methods=["DELETE"])
def borrarFavoritoUsuario():
    conexion: Connection = obtenerConexion()
    idPeliculaBorrada: str = request.args.get("idPelicula", "", type=str)
    if idPeliculaBorrada == "":
        abort(404)
    criticaBorrada: IdUsuarioPelicula = borrarFavoritoBase(
        conexion, IdUsuarioPelicula(1, idPeliculaBorrada)
    )
    return jsonify(criticaBorrada)
