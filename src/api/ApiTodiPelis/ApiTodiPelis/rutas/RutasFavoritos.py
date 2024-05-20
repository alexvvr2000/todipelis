from flask import Blueprint, jsonify, request, abort
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Favoritos import obtenerFavoritos, agregarFavoritoBase
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
