from flask import Flask, g
from flask.json.provider import DefaultJSONProvider
from dataclasses import asdict, is_dataclass
from ApiTodiPelis.rutas.RutasPelicula import rutasPeliculaBlueprint
from ApiTodiPelis.rutas.RutasFavoritos import rutasFavoritosBlueprint
from ApiTodiPelis.rutas.RutasCriticas import rutasCriticasBlueprint
from ApiTodiPelis.rutas.RutasUsuario import rutasUsuarioBlueprint


class DataclassProveedor(DefaultJSONProvider):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj)


app: Flask = Flask(__name__)
app.json = DataclassProveedor(app)
app.register_blueprint(rutasPeliculaBlueprint)
app.register_blueprint(rutasFavoritosBlueprint)
app.register_blueprint(rutasCriticasBlueprint)
app.register_blueprint(rutasUsuarioBlueprint)


@app.teardown_appcontext
def cerrarBase(e=None):
    conexion = g.pop("conexion", None)
    if conexion is not None:
        conexion.close()
