from flask import Blueprint, jsonify
from ApiTodiPelis.conexion import obtenerConexion
from ApiTodiPelis.operaciones.Favoritos import obtenerFavoritos
from ApiTodiPelis.types import ListaFavoritos
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
