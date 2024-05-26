from mariadb import Connection, Cursor
from ApiTodiPelis.types import Usuario
from flask_jwt_extended import jwt_required


def identificarUsuario(
    conexion: Connection, correoElectronico: str, claveAcceso: str
) -> int:
    cursor: Cursor = conexion.cursor()
    cursor.callproc("procedureLoginValido", [correoElectronico, claveAcceso])
    filaRetornada = cursor.fetchone()
    cursor.close()
    return int(filaRetornada[0])


def registrarUsuario(
    conexion: Connection, correoElectronico: str, claveNueva: str, nombreUsuario: str
) -> Usuario:
    if correoElectronico == "":
        raise Exception("Correo no puede estar vacio")
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
