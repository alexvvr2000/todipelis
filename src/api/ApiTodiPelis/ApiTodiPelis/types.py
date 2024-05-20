from dataclasses import dataclass
from decimal import Decimal, getcontext
from datetime import date, datetime

getcontext().prec = 2


@dataclass(frozen=True)
class IdUsuarioPelicula:
    idUsuario: int
    idPelicula: str


@dataclass(frozen=True)
class Usuario:
    idUsuario: int
    nombreUsuario: str
    urlFotoPerfil: str | None


@dataclass(frozen=True)
class Pelicula:
    idPelicula: str
    titulo: str
    genero: str
    urlPoster: str
    rating: Decimal
    sinopsis: str


@dataclass(frozen=True)
class ListaCriticas:
    idCritica: IdUsuarioPelicula
    descripcion: str | None
    estrellas: Decimal
    fechaAgregado: date
    fechaModificado: datetime | None


@dataclass(frozen=True)
class ListaFavoritos:
    idFavorito: IdUsuarioPelicula
