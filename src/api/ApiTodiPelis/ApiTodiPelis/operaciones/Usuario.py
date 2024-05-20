from mariadb import Connection, Cursor
from ApiTodiPelis.types import Usuario


def obtenerDatosUsuarioBase(conexion: Connection) -> Usuario:
    cursor: Cursor = conexion.cursor()
    cursor.callproc("procedureUsuario", (1,))
    usuarioRetornado = cursor.fetchone()
    cursor.close()
    return Usuario(
        idUsuario=1,
        nombreUsuario=usuarioRetornado[0],
        urlFotoPerfil=usuarioRetornado[1] if usuarioRetornado[1] is not None else None,
    )
