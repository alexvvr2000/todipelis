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
from mariadb import Cursor
from get_docker_secret import get_docker_secret
from flask_jwt_extended import JWTManager
from datetime import timedelta


jwtAplicacion: JWTManager = JWTManager()


@jwtAplicacion.user_identity_loader
def idConInstancia(usuarioActual: Usuario):
    return usuarioActual.idUsuario


@jwtAplicacion.user_lookup_loader
def buscarUsuarioPorMedioId(_jwt_header, jwt_data):
    idUsuarioActual: int = jwt_data["sub"]
    cursor: Cursor = obtenerConexion().cursor()
    cursor.callproc("procedureUsuario", (idUsuarioActual,))
    usuarioRetornado = cursor.fetchone()
    cursor.close()
    return Usuario(
        idUsuario=idUsuarioActual,
        nombreUsuario=usuarioRetornado[0],
        urlFotoPerfil=usuarioRetornado[1] if usuarioRetornado[1] is not None else None,
        correoElectronico=usuarioRetornado[2],
    )


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
