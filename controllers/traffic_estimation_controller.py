#  Copyright (c) 2020.
import datetime


from csv import writer

from api_connectors import firebase_connector
from models.traffic_estimation_model import Estimacion
from serializators.traffic_estimation_serializator import TrafficEstimation


def export_traffic_estimation(ts: TrafficEstimation):
    update_str = ts.estimaciones.fecha_actualizacion.campo.valor
    update = to_datetime(update_str)
    estimaciones = ts.estimaciones.estimacion
    estimation_array = []

    for estimacion in estimaciones:
        entrada = estimacion.campo[0].valor
        salida = estimacion.campo[1].valor
        distancia_str = estimacion.campo[2].valor
        distancia = distance_str_to_float(distancia_str)
        duracion = to_datetime1(estimacion.campo[3].valor)
        duracion_historica = to_datetime1(estimacion.campo[4].valor)
        duracion15 = to_datetime1(estimacion.campo[5].valor)
        duracion30 = to_datetime1(estimacion.campo[6].valor)
        duracion45 = to_datetime1(estimacion.campo[7].valor)
        duracion60 = to_datetime1(estimacion.campo[8].valor)
        estimacion_obj = Estimacion(entrada, salida, update, distancia, duracion, duracion_historica, duracion15,
                                    duracion30, duracion45, duracion60)
        estimation_array.append(estimacion_obj)

    export_csv('estimacion_trafico.csv', estimation_array)

def export_traffic_estimation_firebase(ts:TrafficEstimation):
    update_str = ts.estimaciones.fecha_actualizacion.campo.valor
    update = to_datetime(update_str).strftime("%Y/%m/%d/%H/%M")

    estimaciones = ts.estimaciones.estimacion
    estimation_array = []

    for estimacion in estimaciones:
        entrada = estimacion.campo[0].valor
        salida = estimacion.campo[1].valor
        distancia_str = estimacion.campo[2].valor
        distancia = distance_str_to_float(distancia_str)
        # duracion = to_datetime1(estimacion.campo[3].valor)
        # duracion_historica = to_datetime1(estimacion.campo[4].valor)
        # duracion15 = to_datetime1(estimacion.campo[5].valor)
        # duracion30 = to_datetime1(estimacion.campo[6].valor)
        # duracion45 = to_datetime1(estimacion.campo[7].valor)
        # duracion60 = to_datetime1(estimacion.campo[8].valor)
        duracion = to_datetime1(estimacion.campo[3].valor).strftime("%H:%M:%S")
        duracion_historica = to_datetime1(estimacion.campo[4].valor).strftime("%H:%M:%S")
        duracion15 = to_datetime1(estimacion.campo[5].valor).strftime("%H:%M:%S")
        duracion30 = to_datetime1(estimacion.campo[6].valor).strftime("%H:%M:%S")
        duracion45 = to_datetime1(estimacion.campo[7].valor).strftime("%H:%M:%S")
        duracion60 = to_datetime1(estimacion.campo[8].valor).strftime("%H:%M:%S")

        estimacion_obj = Estimacion(entrada, salida, update, distancia, duracion, duracion_historica, duracion15,
                                    duracion30, duracion45, duracion60)
        estimation_array.append(estimacion_obj)
    firebase_connector.post_estimacion_trafico(estimation_array,update)


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
