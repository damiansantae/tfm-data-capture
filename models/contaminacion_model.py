#  Copyright (c) 2020.


class ContaminacionModel:
    datetime: str
    estacion: int
    magnitud: int
    valor: float

    def __init__(self, datetime: str, estacion: int, magnitud: int, valor: float) -> None:
        self.datetime = datetime
        self.estacion = estacion
        self.magnitud = magnitud
        self.valor = valor

    def get_datetime(self):
        return self.datetime

    def get_estacion(self):
        return self.estacion

    def get_magnitud(self):
        return self.magnitud

    def get_valor(self):
        return self.valor
