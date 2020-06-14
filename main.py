import json

# from flask import Flask

from serializators.contaminacion_serializator import contaminacion_from_dict
from serializators.trafficAPI_serializator import empty_from_dict
from serializators.trabajos_planificados_serializator import trabajos_planificados_from_dict
from serializators.traffic_estimation_serializator import traffic_estimation_from_dict
from serializators.AEMETAPI_serializator import welcome_from_dict
from serializators.cameras_serializator import cameras_from_dict
from api_connectors.apiconnection_service import APIConnection, AEMETAPI_Connection
from apscheduler.schedulers.blocking import BlockingScheduler
from controllers.contaminacion_controller import export_contaminacion
from controllers.datos_trafico_madrid import export_datos_trafico_mad
from controllers.weather_controller import export_dayly_weather_firebase
from controllers.cameras_controller import export_cameras
from controllers.traffic_estimation_controller import export_traffic_estimation_firebase
from controllers.trabajos_planificados_controller import export_trabajos_planificados_firebase

# app = Flask(__name__)
# PORT = 5000
# DEBUG = True

sched = BlockingScheduler()
traffic_api = APIConnection()
aemet_api = AEMETAPI_Connection()

# @app.errorhandler(404)
# def not_found(error):
#     return "Not found"
#
#
# @app.route('/', methods=['GET'])
# def index():
#     result = get_contaminacion()
#     hola = result
#     return hola


# if __name__ == '__main__':
#     app.run(port=PORT, debug=DEBUG)

traffic_api = APIConnection()
aemet_api = AEMETAPI_Connection()


def get_contaminacion() -> str:
    get_contaminacion = traffic_api.get_contamination
    data = get_contaminacion()
    contaminacion_madrid = contaminacion_from_dict(json.loads(data))
    return contaminacion_madrid


def get_datos_trafico_madrid() -> str:
    get_datos_trafico_madrid = traffic_api.get_traffic_data_urls
    data = get_datos_trafico_madrid()
    datos_traffico_madrid = empty_from_dict(json.loads(data))
    return datos_traffico_madrid


def get_estimacion_trafico() -> str:
    get_estimation = traffic_api.get_traffic_estimation
    data = get_estimation()
    traffic_estimation = traffic_estimation_from_dict(json.loads(data))
    return traffic_estimation


def get_trabajos_planificados() -> str:
    get_trabajos_planificados = traffic_api.get_trabajos_planificados
    data = get_trabajos_planificados()
    json_data = json.loads(data)
    trabajos_planificados = trabajos_planificados_from_dict(json_data)
    return trabajos_planificados




def get_daily_weather() -> str:
    get_daily_weather = aemet_api.get_daily_weather
    data = get_daily_weather()
    dayly_weather = welcome_from_dict(json.loads(data))
    return dayly_weather


@sched.scheduled_job('interval', minutes=60)
def timed_job():
    result = get_contaminacion()
    export_contaminacion(result)


@sched.scheduled_job('interval', minutes=5)
def timed_job():
    result = get_datos_trafico_madrid()
    export_datos_trafico_mad(result)


@sched.scheduled_job('interval', minutes=5)
def timed_job():
    result = get_estimacion_trafico()
    export_traffic_estimation_firebase(result)


@sched.scheduled_job('interval', minutes=120)
def timed_job():
    result = get_trabajos_planificados()
    export_trabajos_planificados_firebase(result)


@sched.scheduled_job('interval', minutes=60)
def timed_job():
    result = get_daily_weather()
    export_dayly_weather_firebase(result)


sched.start()


# def main():
#     result = get_datos_trafico_madrid()
#     export_datos_trafico_mad(result)
#
#
# if __name__ == "__main__":
#     main()
