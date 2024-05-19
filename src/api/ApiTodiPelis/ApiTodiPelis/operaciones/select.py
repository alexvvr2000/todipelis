from typing import Dict
from flask import g
from requests import get, Response
from get_docker_secret import get_docker_secret
from mariadb import Connection, Cursor
from ApiTodiPelis.operaciones.insert import agregarPeliculaBase
from ApiTodiPelis.conexion import existePeliculaBase
from ApiTodiPelis.types import (
    Pelicula,
    ListaCriticas,
    ListaFavoritos,
    Usuario,
)


def obtenerPeliculaIdApi(idPelicula: str) -> Pelicula | None:
    urlBase: str = "http://www.omdbapi.com/"
    parametros: Dict[str, str] = {
        "apikey": get_docker_secret("api-key"),
        "i": idPelicula,
    }
    respuesta: Response = get(urlBase, params=parametros)
    if respuesta.status_code != 200:
        return None
    datosPeliculas = respuesta.json()
    if datosPeliculas.get("Response") == "False":
        return None
    peliculaBase = Pelicula(
        idPelicula=idPelicula,
        titulo=datosPeliculas.get("Title"),
        genero=datosPeliculas.get("Genre"),
        urlPoster=datosPeliculas.get("Poster"),
        rating=datosPeliculas.get("imdbRating"),
        sinopsis=datosPeliculas.get("Plot"),
    )
    return peliculaBase


def obtenerPelicula(conexion: Connection, idPelicula: str) -> Pelicula | None:
    peliculaBase: Pelicula | None
    if existePeliculaBase(conexion, idPelicula):
        cursor: Cursor = conexion.cursor()
        cursor.callproc("procedureObtenerPelicula", (idPelicula,))
        filaRetornada = cursor.fetchone()
        cursor.close()
        peliculaBase: Pelicula = Pelicula(
            idPelicula=idPelicula,
            titulo=filaRetornada[0],
            genero=filaRetornada[1],
            urlPoster=filaRetornada[2],
            rating=filaRetornada[3],
            sinopsis=filaRetornada[4],
        )
        return peliculaBase
    else:
        peliculaBase: Pelicula | None = obtenerPeliculaIdApi(idPelicula)
        if peliculaBase is None:
            return None
        agregarPeliculaBase(conexion, peliculaBase)
    return peliculaBase
