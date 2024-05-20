from ApiTodiPelis.ContructorApp import crearApp
from flask import g

aplicacion = crearApp()


@aplicacion.teardown_appcontext
def cerrarBase(e=None):
    conexion = g.pop("conexion", None)
    if conexion is not None:
        conexion.close()


if __name__ == "__main__":
    aplicacion.run()
