#  Copyright (c) 2020.


class TrabajoPlanificado:
    fecha_inicio: str
    fecha_fin: str
    horario: str
    descripcion: str
    puntos: []

    def __init__(self, fecha_inicio, fecha_fin, horario, tipo_corte,
                 descripcion, puntos) -> None:
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.horario = horario
        self.fecha_inicio = fecha_inicio
        self.tipo_corte = tipo_corte
        self.descripcion = descripcion
        self.puntos = puntos
