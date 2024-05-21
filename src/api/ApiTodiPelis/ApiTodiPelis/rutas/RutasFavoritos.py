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
from flask_jwt_extended import current_user, jwt_required

rutasFavoritosBlueprint: Blueprint = Blueprint("rutasFavoritos", __name__)


@rutasFavoritosBlueprint.route("/favoritos/", methods=["GET"])
@jwt_required()
def obtenerFavoritosUsuario():
    conexion: Connection = obtenerConexion()
    favoritosUsuario: List[ListaFavoritos] = obtenerFavoritos(conexion)
    return jsonify(
        {
            "cantidadFavoritos": len(favoritosUsuario),
            "favoritosUsuario": favoritosUsuario,
        }
    )


@rutasFavoritosBlueprint.route("/favoritos", methods=["POST"])
@jwt_required()
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


@rutasFavoritosBlueprint.route("/favoritos", methods=["DELETE"])
@jwt_required()
def borrarFavoritoUsuario():
    conexion: Connection = obtenerConexion()
    idPeliculaBorrada: str = request.args.get("idPelicula", "", type=str)
    if idPeliculaBorrada == "":
        abort(404)
    idUsuarioActual: int = current_user.idUsuario
    criticaBorrada: IdUsuarioPelicula = borrarFavoritoBase(
        conexion, IdUsuarioPelicula(idUsuarioActual, idPeliculaBorrada)
    )
    return jsonify(criticaBorrada)
