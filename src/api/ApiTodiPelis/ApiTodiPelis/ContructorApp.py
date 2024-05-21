from flask import Flask
from flask.json.provider import DefaultJSONProvider
from dataclasses import asdict, is_dataclass
from ApiTodiPelis.rutas.RutasPelicula import rutasPeliculaBlueprint
from ApiTodiPelis.rutas.RutasFavoritos import rutasFavoritosBlueprint
from ApiTodiPelis.rutas.RutasCriticas import rutasCriticasBlueprint
from ApiTodiPelis.rutas.RutasUsuario import rutasUsuarioBlueprint
from ApiTodiPelis.operaciones.Usuario import obtenerDatosUsuarioBase
from ApiTodiPelis.types import Usuario
from ApiTodiPelis.conexion import obtenerConexion
from mariadb import Connection
from get_docker_secret import get_docker_secret
from flask_jwt_extended import JWTManager
from datetime import timedelta


jwtAplicacion: JWTManager = JWTManager()


@jwtAplicacion.user_identity_loader
def idConInstancia(usuarioActual: Usuario):
    return usuarioActual.idUsuario


@jwtAplicacion.user_lookup_loader
def buscarUsuarioPorMedioId(_jwt_header, jwt_data):
    idUsuario: int = jwt_data["sub"]
    conexionBase: Connection = obtenerConexion()
    return obtenerDatosUsuarioBase(conexionBase, idUsuario)


class DataclassProveedor(DefaultJSONProvider):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj)


def crearApp() -> Flask:
    app: Flask = Flask(__name__)

    app.json = DataclassProveedor(app)

    app.register_blueprint(rutasPeliculaBlueprint)
    app.register_blueprint(rutasFavoritosBlueprint)
    app.register_blueprint(rutasCriticasBlueprint)
    app.register_blueprint(rutasUsuarioBlueprint)

    app.config["JWT_SECRET_KEY"] = get_docker_secret("jwt-key")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    jwtAplicacion.init_app(app)

    return app
