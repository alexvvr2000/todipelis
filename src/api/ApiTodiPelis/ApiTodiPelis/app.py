from flask import Flask, g
from ApiTodiPelis.rutas import rutas

app: Flask = Flask(__name__)
app.register_blueprint(rutas)


@app.teardown_appcontext
def cerrarBase(e=None):
    conexion = g.pop("conexion", None)
    if conexion is not None:
        conexion.close()
