from ApiTodiPelis.ContructorApp import crearApp
from werkzeug.exceptions import Unauthorized
from flask import g, jsonify

aplicacion = crearApp()


@aplicacion.teardown_appcontext
def cerrarBase(e=None):
    conexion = g.pop("conexion", None)
    if conexion is not None:
        conexion.close()


@aplicacion.errorhandler(Unauthorized)
def manejar_UsuarioSinAuth(e: Unauthorized):
    return (
        jsonify({"msg": str(e)}),
        401,
        {"WWW-Authenticate": 'Bearer realm="Login required"'},
    )


if __name__ == "__main__":
    aplicacion.run()
