#  Copyright (c) 2020.


class Estimacion:
    entrada: str
    salida: str
    update: str
    distance: float
    duracion: str
    duracion_historica: str
    duracion15: str
    duracion30: str
    duracion45: str
    duracion60: str

    def __init__(self, entrada: str, salida: str, update: str, distance: float, duracion: str, duracion_historica: str,
                 duracion15: str, duracion30: str, duracion45: str, duracion60: str) -> None:
        self.entrada = entrada
        self.salida = salida
        self.update = update
        self.distance = distance
        self.duracion = duracion
        self.duracion_historica = duracion_historica
        self.duracion15 = duracion15
        self.duracion30 = duracion30
        self.duracion45 = duracion45
        self.duracion60 = duracion60

    def get_entrada(self):
        return self.entrada

    def get_salida(self):
        return self.salida

    def get_update(self):
        return self.update

    def get_distance(self):
        return self.distance

    def get_duracion(self):
        return self.duracion

    def get_duracion_historica(self):
        return self.duracion_historica

    def get_duracion15(self):
        return self.duracion15

    def get_duracion30(self):
        return self.duracion30

    def get_duracion45(self):
        return self.duracion45

    def get_duracion60(self):
        return self.duracion60
