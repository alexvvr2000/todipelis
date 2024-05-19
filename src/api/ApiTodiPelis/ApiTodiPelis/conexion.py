from get_docker_secret import get_docker_secret
from mariadb import connect, Connection, Cursor
from flask import g


def existePeliculaBase(idPelicula: str) -> bool:
    cursor: Cursor = obtenerConexion().cursor()
    cursor.execute("select funcionPeliculaExiste(?) as existe", (idPelicula,))
    filaRetornada = cursor.fetchone()
    peliculaExiste: bool = filaRetornada[0] == 1
    cursor.close()
    return peliculaExiste


def obtenerConexion() -> Connection:
    if "conexion" not in g:
        g.conexion = connect(
            host="database",
            port=3306,
            user="api",
            password=get_docker_secret("api-password"),
            database="todipelis",
        )
    return g.conexion
