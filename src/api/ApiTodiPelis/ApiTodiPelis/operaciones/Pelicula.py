from typing import Dict
from flask import g
from requests import get, Response
from get_docker_secret import get_docker_secret
from mariadb import Connection, Cursor
from ApiTodiPelis.types import Pelicula


def existePeliculaBase(conexion: Connection, idPelicula: str) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute("select funcionPeliculaExiste(?) as existe", (idPelicula,))
    filaRetornada = cursor.fetchone()
    cursor.close()
    peliculaExiste: bool = filaRetornada[0] == 1
    return peliculaExiste


def existePeliculaApi(idPelicula: str) -> bool:
    urlBase: str = "http://www.omdbapi.com/"
    parametros: Dict[str, str] = {
        "apikey": get_docker_secret("api-key"),
        "i": idPelicula,
    }
    respuesta: Response = get(urlBase, params=parametros)
    return respuesta.status_code == 200


def agregarPeliculaBase(conexion: Connection, pelicula: Pelicula) -> str:
    if existePeliculaBase(conexion, pelicula.idPelicula):
        raise Exception(f"Pelicula con id {pelicula.idPelicula} ya esta en base")
    cursor: Cursor = conexion.cursor()
    cursor.callproc(
        "procedureInsertPelicula",
        (
            pelicula.idPelicula,
            pelicula.titulo,
            pelicula.genero,
            pelicula.urlPoster,
            pelicula.rating,
            pelicula.sinopsis,
        ),
    )
    idInsertado = cursor.fetchone()
    cursor.close()
    conexion.commit()
    return idInsertado[0]


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


def obtenerPeliculaTitulo(conexion: Connection, tituloPelicula: str) -> Pelicula | None:
    urlBase: str = "http://www.omdbapi.com/"
    parametros: Dict[str, str] = {
        "apikey": get_docker_secret("api-key"),
        "t": tituloPelicula,
    }
    respuesta: Response = get(urlBase, params=parametros)
    if respuesta.status_code != 200:
        return None
    datosPeliculas = respuesta.json()
    if datosPeliculas.get("Response") == "False":
        return None
    peliculaBase = Pelicula(
        idPelicula=datosPeliculas.get("imdbID"),
        titulo=datosPeliculas.get("Title"),
        genero=datosPeliculas.get("Genre"),
        urlPoster=datosPeliculas.get("Poster"),
        rating=datosPeliculas.get("imdbRating"),
        sinopsis=datosPeliculas.get("Plot"),
    )
    if not existePeliculaBase(conexion, peliculaBase.idPelicula):
        agregarPeliculaBase(conexion, peliculaBase)
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
