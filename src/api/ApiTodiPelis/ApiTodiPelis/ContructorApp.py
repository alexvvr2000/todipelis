from flask import Flask, g
from flask.json.provider import DefaultJSONProvider
from dataclasses import asdict, is_dataclass
from ApiTodiPelis.rutas.RutasPelicula import rutasPeliculaBlueprint
from ApiTodiPelis.rutas.RutasFavoritos import rutasFavoritosBlueprint
from ApiTodiPelis.rutas.RutasCriticas import rutasCriticasBlueprint
from ApiTodiPelis.rutas.RutasUsuario import rutasUsuarioBlueprint
from get_docker_secret import get_docker_secret
from flask_jwt_extended import JWTManager


jwtAplicacion: JWTManager = JWTManager()


class DataclassProveedor(DefaultJSONProvider):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj)


def crearApp() -> Flask:
    app: Flask = Flask(__name__)

    app.json = DataclassProveedor(app)
    app.config["JWT_SECRET_KEY"] = get_docker_secret("jwt-key")

    app.register_blueprint(rutasPeliculaBlueprint)
    app.register_blueprint(rutasFavoritosBlueprint)
    app.register_blueprint(rutasCriticasBlueprint)
    app.register_blueprint(rutasUsuarioBlueprint)

    jwtAplicacion.init_app(app)

    return app
