from flask import Flask, g
from flask.json.provider import DefaultJSONProvider
from dataclasses import asdict, is_dataclass
from json import JSONEncoder
from ApiTodiPelis.rutas import rutas


class DataclassProveedor(DefaultJSONProvider):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj)


app: Flask = Flask(__name__)
app.json = DataclassProveedor(app)
app.register_blueprint(rutas)


@app.teardown_appcontext
def cerrarBase(e=None):
    conexion = g.pop("conexion", None)
    if conexion is not None:
        conexion.close()
