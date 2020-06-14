#  Copyright (c) 2020.
import datetime


#import pandas as pd
from csv import writer

from api_connectors import firebase_connector
from models.contaminacion_model import ContaminacionModel


def export_contaminacion(contaminacion: ContaminacionModel):

    contaminacion_array = []
    list_contaminacion = contaminacion.datos.dato_horario

    for contaminacion in list_contaminacion:
        month = contaminacion.get('mes')
        year = contaminacion.get('ano')
        day = contaminacion.get('dia')
        estacion = contaminacion.get('estacion')
        magnitud = contaminacion.get('magnitud')
        for i in range(1, 25):
            if i - 10 < 0:
                hora = i
                valor = contaminacion.get('H0' + str(i))
                time = datetime.datetime(int(year), int(month), int(day), hora).strftime("%H")
                contaminacion_obj = ContaminacionModel(time, estacion, magnitud, float(valor))
            else:
                hora = i
                valor = contaminacion.get('H' + str(i))
                contaminacion_obj = ContaminacionModel(str(i), estacion, magnitud, float(valor))

            contaminacion_array.append(contaminacion_obj)
    firebase_connector.post_contaminacion(contaminacion_array)

    #export_csv('contaminacion.csv', contaminacion_obj)


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
