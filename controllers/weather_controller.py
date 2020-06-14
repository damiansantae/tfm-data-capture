#  Copyright (c) 2020.
import datetime
from csv import writer
from api_connectors import firebase_connector
from serializators.AEMETAPI_serializator import WelcomeElement
from models.weather_model import WeatherModel


def export_dayly_weather_firebase(weather: WelcomeElement):
    update = weather[0].elaborado
    time = update.strftime("%Y/%m/%d/%H/%M")
    dias = weather[0].prediccion.dia
    prediction_list = []
    for dia in dias:
        ocaso = dia.ocaso
        orto = dia.orto
        cielos = dia.estado_cielo
        humedades = dia.humedad_relativa
        nieves = dia.nieve
        temperaturas = dia.temperatura
        vientos = dia.viento_and_racha_max
        precipitaciones = dia.precipitacion

        list_cielo = []
        list_humedad = []
        list_nieve = []
        list_precipitacion = []
        list_temperatura = []
        list_viento = []

        for estado_cielo in cielos:
            cielosdic = estado_cielo.__dict__
            list_cielo.append(cielosdic)
        for humedad in humedades:
            humedaddic = humedad.__dict__
            list_humedad.append(humedaddic)
        for nieve in nieves:
            nievedic = nieve.__dict__
            list_nieve.append(nievedic)
        for temperatura in temperaturas:
            temperaturadic = temperatura.__dict__
            list_temperatura.append(temperaturadic)
        for viento in vientos:
            vientodic = viento.__dict__
            list_viento.append(vientodic)
        for precipitacion in precipitaciones:
            precipitaciondic = precipitacion.__dict__
            list_precipitacion.append(precipitaciondic)

        dia_model = WeatherModel(orto, ocaso, list_cielo, list_humedad, list_nieve, list_temperatura, list_viento,
                                 list_precipitacion)
        prediction_list.append(dia_model)
    firebase_connector.post_weather(prediction_list, time)


def to_datetime(str_time: str) -> datetime:
    date_time_obj = datetime.datetime.strptime(str_time, '%d/%m/%Y %H:%M:%S')
    return date_time_obj
