from flask import Flask
from ApiTodiPelis.operaciones.select import obtenerPelicula
from dataclasses import asdict

app: Flask = Flask(__name__)


@app.route("/<string:idPelicula>", methods=["GET"])
def ruta(idPelicula: str):
    peliculaBase = obtenerPelicula(idPelicula)
    return asdict(peliculaBase)
