from flask import Flask
from ApiTodiPelis.operaciones.select import obtenerPelicula
from ApiTodiPelis.operaciones.conexion import obtenerConexion
from mariadb import Connection
from dataclasses import asdict

app: Flask = Flask(__name__)


@app.route("/<string:idPelicula>", methods=["GET"])
def ruta(idPelicula: str):
    conexion: Connection = obtenerConexion()
    peliculaBase = obtenerPelicula(conexion, idPelicula)
    return asdict(peliculaBase)
