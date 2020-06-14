#  Copyright (c) 2020.

import firebase_admin
from firebase_admin import db
import datetime
import json

# firebase = firebase.FirebaseApplication("https://traffic-dt.firebaseio.com/",None)


cred = firebase_admin.credentials.Certificate("movies-d342f-e5d62f5dcb69.json")
firebase = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://movies-d342f.firebaseio.com/'
})


def post_contaminacion(data):
    time = datetime.datetime.now().strftime("%Y/%m/%d/%H/%M")
    list = []
    for dato in data:
        list.append(obj_dict(dato))
    ref = db.reference('/contaminacion/' + time)
    result = ref.set(list)
    ref2 = db.reference('/last_reg/contaminacion')
    result2 = ref2.set(list)
    print(result)


def post_estado_trafico(data, update):
    time = datetime.datetime.now()
    json_data = json.dumps(data)


def post_estimacion_trafico(data, update):
    list = []
    for dato in data:
        list.append(obj_dict(dato))
    ref = db.reference('/estimacion_trafico/' + update)
    result = ref.set(list)
    ref2 = db.reference('/last_reg/estimacion_trafico/')
    result2 = ref2.set(list)


def obj_dict(obj):
    return obj.__dict__


def post_datos_trafico(datos_trafico_array, update):
    update_datetime = to_datetime(update)
    time = update_datetime.strftime("%Y/%m/%d/%H/%M")
    list = []
    for dato in datos_trafico_array:
        list.append(obj_dict(dato))
    ref = db.reference('/datos_trafico_mad/' + time)
    result = ref.set(list)
    ref2 = db.reference('/last_reg/datos_trafico_mad')
    result2 = ref2.set(list)
    print(result)


def post_trabajos_planificados(trabajos, update):
    list = []
    for dato in trabajos:
        list.append(obj_dict(dato))
    ref = db.reference('/trabajos_planificados/' + update)
    result = ref.set(list)
    ref2 = db.reference('/last_reg/trabajos_planificados')
    result2 = ref2.set(list)
    print(result, result2)


def post_weather(weather, update):
    ref = db.reference('/tiempo/' + update)
    ref2 = db.reference('/last_reg/tiempo')
    list = []
    for dato in weather:
        list.append(obj_dict(dato))
    result = ref.set(list)
    result2 = ref2.set(list)
    print(result)


def to_datetime(str_time: str) -> datetime:
    date_time_obj = datetime.datetime.strptime(str_time, '%d/%m/%Y %H:%M:%S')
    return date_time_obj
