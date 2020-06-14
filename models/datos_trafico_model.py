#  Copyright (c) 2020.
from typing import Optional


class DatoTMadModel:
    idelem: str
    descripcion: str
    intensidad: int
    ocupacion: float
    carga: int
    velocidad: Optional[str]
    nivel_servicio: str
    intensidad_sat: int
    x: str
    y: str

    def __init__(self, idelem: str, descripcion: str, intensidad: int, ocupacion: float,
                 carga: int,
                 velocidad: Optional[str],
                 nivel_servicio: str,
                 intensidad_sat: int,
                 x: str,
                 y: str
                 ) -> None:
        self.idelem = idelem
        self.descripcion = descripcion
        self.intensidad = intensidad
        self.ocupacion = ocupacion
        self.carga = carga
        self.velocidad = velocidad
        self.nivel_servicio = nivel_servicio
        self.intensidad_sat = intensidad_sat
        self.x = x
        self.y = y

##TODO: configurar getters
