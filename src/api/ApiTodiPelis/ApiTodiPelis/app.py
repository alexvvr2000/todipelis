from flask import Flask, g
from flask.json.provider import DefaultJSONProvider
from dataclasses import asdict, is_dataclass
from ApiTodiPelis.rutas.RutasPelicula import rutasPeliculaBlueprint


class DataclassProveedor(DefaultJSONProvider):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj)


app: Flask = Flask(__name__)
app.json = DataclassProveedor(app)
app.register_blueprint(rutasPeliculaBlueprint)


@app.teardown_appcontext
def cerrarBase(e=None):
    conexion = g.pop("conexion", None)
    if conexion is not None:
        conexion.close()
