from typing import Dict
from requests import get, Response
from get_docker_secret import get_docker_secret
from mariadb import Connection, Cursor
from ApiTodiPelis.types import Pelicula
from dataclasses import dataclass
from typing import List
from decimal import Decimal, getcontext, ROUND_CEILING

getcontext().prec = 2


@dataclass(frozen=True)
class PaginaBusquedaTitulo:
    resultadoBusqueda: List[Pelicula]
    cantidadPeliculasPaginaActual: int
    totalResultados: int
    totalPaginas: int
    paginaActual: int


def existePeliculaBase(conexion: Connection, idPelicula: str) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute("select funcionPeliculaExiste(?) as existe", (idPelicula,))
    filaRetornada = cursor.fetchone()
    cursor.close()
    peliculaExiste: bool = filaRetornada[0] == 1
    return peliculaExiste


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


def obtenerPeliculaIdApi(idPelicula: str) -> Pelicula:
    urlBase: str = "http://www.omdbapi.com/"
    parametros: Dict[str, str] = {
        "apikey": get_docker_secret("api-key"),
        "i": idPelicula,
        "type": "movie",
    }
    respuesta: Response = get(urlBase, params=parametros)
    if respuesta.status_code != 200:
        raise Exception("No se pudo hacer contacto con la base de datos de pelicula")
    datosPeliculas = respuesta.json()
    if datosPeliculas.get("Response") == "False":
        raise Exception("No se encontro pelicula por id en api")
    generoPelicula: str = datosPeliculas.get("Genre")
    urlPosterPelicula: str = datosPeliculas.get("Poster")
    ratingPelicula: str = datosPeliculas.get("imdbRating")
    sinopsisPelicula: str = datosPeliculas.get("Plot")
    peliculaBase = Pelicula(
        idPelicula=idPelicula,
        titulo=datosPeliculas.get("Title"),
        genero=None if generoPelicula == "N/A" else generoPelicula,
        urlPoster=None if urlPosterPelicula == "N/A" else urlPosterPelicula,
        rating=None if ratingPelicula == "N/A" else ratingPelicula,
        sinopsis=None if sinopsisPelicula == "N/A" else sinopsisPelicula,
    )
    return peliculaBase


def obtenerPeliculaTitulo(
    conexion: Connection, tituloPelicula: str, paginaBusqueda: int
) -> PaginaBusquedaTitulo:
    urlBase: str = "http://www.omdbapi.com/"
    parametros: Dict[str, str] = {
        "apikey": get_docker_secret("api-key"),
        "s": tituloPelicula,
        "type": "movie",
        "page": paginaBusqueda,
        "r": "json",
        "v": 1,
    }
    respuesta: Response = get(urlBase, params=parametros)
    if respuesta.status_code != 200:
        raise Exception("No se pudo hacer contacto con la base de datos de pelicula")
    datosPeliculas = respuesta.json()
    if datosPeliculas.get("Response") == "False":
        raise Exception("No se pudo encontrar peliculas con los parametros solicitados")
    listaPeliculas: List[Pelicula] = []
    totalResultados: int = int(datosPeliculas["totalResults"])
    totalPaginas: int = int(
        (Decimal(totalResultados) / Decimal("10")).to_integral_exact(
            rounding=ROUND_CEILING
        )
    )
    for peliculaActual in datosPeliculas.get("Search"):
        idPeliculaActual: str = peliculaActual.get("imdbID")
        datosPeliculaActual: Pelicula = obtenerPelicula(conexion, idPeliculaActual)
        peliculaBase = Pelicula(
            idPelicula=datosPeliculaActual.idPelicula,
            titulo=datosPeliculaActual.titulo,
            genero=datosPeliculaActual.genero,
            urlPoster=datosPeliculaActual.urlPoster,
            rating=datosPeliculaActual.rating,
            sinopsis=datosPeliculaActual.sinopsis,
        )
        listaPeliculas.append(peliculaBase)
    return PaginaBusquedaTitulo(
        listaPeliculas,
        len(listaPeliculas),
        totalResultados,
        totalPaginas,
        paginaBusqueda,
    )


def obtenerPelicula(conexion: Connection, idPelicula: str) -> Pelicula:
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
            rating=Decimal(filaRetornada[3]),
            sinopsis=filaRetornada[4],
        )
        return peliculaBase
    else:
        peliculaBase: Pelicula = obtenerPeliculaIdApi(idPelicula)
        agregarPeliculaBase(conexion, peliculaBase)
    return peliculaBase
