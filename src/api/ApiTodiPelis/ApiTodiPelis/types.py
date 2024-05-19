from dataclasses import dataclass
from decimal import Decimal, getcontext

getcontext().prec = 2


@dataclass(frozen=True)
class Usuario:
    idUsuario: int
    nombreUsuario: str
    urlFotoPerfil: str


@dataclass(frozen=True)
class Pelicula:
    idPelicula: int
    titulo: str
    genero: str
    urlPoster: str
    rating: Decimal
    sinopsis: str
