## Tráfico. Datos del tráfico en tiempo real
#  Copyright (c) 2020.
import datetime

# import pandas as pd
from csv import writer

from api_connectors import firebase_connector
from models.datos_trafico_model import DatoTMadModel


def export_datos_trafico_mad(datos_trafico: DatoTMadModel):
    datos_trafico_array = []
    list_pms = datos_trafico.pms.pm
    update = datos_trafico.pms.fecha_hora

    for pm in list_pms:
        idelem = pm.idelem
        descripcion = pm.descripcion
        intensidad = pm.intensidad
        ocupacion = pm.ocupacion
        carga = pm.carga
        velocidad = pm.velocidad
        nivel_servicio = pm.nivel_servicio
        intensidad_sat = pm.intensidad_sat
        x = pm.st_x
        y = pm.st_y

        dato_trafico_obj = DatoTMadModel(idelem, descripcion, intensidad, ocupacion, carga, velocidad, nivel_servicio,
                                         intensidad_sat, x, y)

        datos_trafico_array.append(dato_trafico_obj)

    firebase_connector.post_datos_trafico(datos_trafico_array, update)


# export_csv('contaminacion.csv', contaminacion_obj)


def export_csv(file_name, list_of_elem):
    # Open file in append mode
    with open('estimacion_trafico.csv', 'a+', newline='') as csvfile:
        csv_writer = writer(csvfile)
        # if isempty:
        #     csv_writer.writerow(['Entrada', 'salida', 'update', 'duracion', 'duracion_historica', 'duracion15',
        #                      'duracion30', 'duracion45', 'duracion60'])
        for estimacion in list_of_elem:
            csv_writer.writerow(
                [estimacion.entrada, estimacion.salida, estimacion.update, estimacion.distance, estimacion.duracion,
                 estimacion.duracion_historica, estimacion.duracion15, estimacion.duracion30,
                 estimacion.duracion45, estimacion.duracion60])


# Parse str "XX.XX KM" to float XX.XX
def distance_str_to_float(distance_str) -> float:
    distance_array = distance_str.split()
    return distance_array[0]


# Format date str to datetime object
def to_datetime(str_time: str) -> datetime:
    date_time_obj = datetime.datetime.strptime(str_time, '%d/%m/%Y %H:%M:%S')
    return date_time_obj


# Parse min seconds time to date time object
def to_datetime1(str_time: str) -> datetime:
    try:
        date_time_obj = datetime.datetime.strptime(str_time, "%M ' %S ''")
    except:
        date_time_obj = datetime.datetime(2010, 4, 27)
    return date_time_obj
