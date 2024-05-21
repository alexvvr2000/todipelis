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


def existeCorreoRegistradoBase(conexion: Connection, correoElectronico: str) -> bool:
    cursor: Cursor = conexion.cursor()
    cursor.execute("select funcionCorreoExiste(?) as existe", (correoElectronico,))
    filaRetornada = cursor.fetchone()
    cursor.close()
    peliculaExiste: bool = filaRetornada[0] == 1
    return peliculaExiste


def registrarUsuario(
    conexion: Connection, correoElectronico: str, claveNueva: str, nombreUsuario: str
) -> Usuario:
    if correoElectronico == "":
        raise Exception("Correo no puede estar vacio")
    if existeCorreoRegistradoBase(conexion, correoElectronico):
        raise Exception("Correo ya existe en base")
    if claveNueva == "":
        raise Exception("Clave de acceso no puede estar vacia")
    if nombreUsuario == "":
        raise Exception("Nombre de usuario no puede estar vacio")
    cursor: Cursor = conexion.cursor()
    # TODO: encriptar conexion mariadb -> python y viceversa
    cursor.callproc(
        "procedureRegistrarUsuario", [correoElectronico, claveNueva, nombreUsuario]
    )
    nuevoIdUsuario = cursor.fetchone()
    cursor.close()
    conexion.commit()
    return int(nuevoIdUsuario[0])
