#  Copyright (c) 2020.


class WeatherModel:
    ocaso: str
    orto: str
    cielos: list
    nieve: list
    precipitacion: list
    temperatura: list
    humedad: list
    viento: list

    def __init__(self, orto: str, ocaso: str, cielos: list, humedad: list, nieve: list, temperatura: list,
                 viento: list,
                 precipitacion: list) -> None:
        self.ocaso = ocaso
        self.orto = orto
        self.cielos = cielos
        self.nieve = nieve
        self.precipitacion = precipitacion
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
