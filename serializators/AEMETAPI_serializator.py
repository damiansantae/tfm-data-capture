# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from typing import Any, Union, Optional, List, TypeVar, Type, Callable, cast
from enum import Enum
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()




class EstadoCielo:
    value: str
    periodo: str
    descripcion: str

    def __init__(self, value: str, periodo: str, descripcion: str) -> None:
        self.value = value
        self.periodo = periodo
        self.descripcion = descripcion

    @staticmethod
    def from_dict(obj: Any) -> 'EstadoCielo':
        assert isinstance(obj, dict)
        value = from_str(obj.get("value"))
        periodo = from_str(obj.get("periodo"))
        descripcion = from_str(obj.get("descripcion"))
        return EstadoCielo(value, periodo, descripcion)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_str(self.value)
        result["periodo"] = from_str(self.periodo)
        result["descripcion"] = from_str(self.descripcion)
        return result


class FluffyValue(Enum):
    EMPTY = ""
    IP = "Ip"


class HumedadRelativa:
    value: Union[FluffyValue, int]
    periodo: str

    def __init__(self, value: Union[FluffyValue, int], periodo: str) -> None:
        self.value = value
        self.periodo = periodo

    @staticmethod
    def from_dict(obj: Any) -> 'HumedadRelativa':
        assert isinstance(obj, dict)
        value = from_str(obj.get("value"))
        periodo = from_str(obj.get("periodo"))
        return HumedadRelativa(value, periodo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_str(self.value)
        result["periodo"] = from_str(self.periodo)
        return result


class VientoAndRachaMax:
    direccion: Optional[List[str]]
    velocidad: Optional[List[int]]
    periodo: str
    value: Optional[int]

    def __init__(self, direccion: Optional[List[str]], velocidad: Optional[List[int]], periodo: str, value: Optional[int]) -> None:
        self.direccion = direccion
        self.velocidad = velocidad
        self.periodo = periodo
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'VientoAndRachaMax':
        assert isinstance(obj, dict)
        direccion = from_union([lambda x: from_list(from_str, x), from_none], obj.get("direccion"))
        velocidad = from_union([lambda x: from_list(lambda x: int(from_str(x)), x), from_none], obj.get("velocidad"))
        periodo = from_str(obj.get("periodo"))
        value = from_union([from_none, lambda x: int(from_str(x))], obj.get("value"))
        return VientoAndRachaMax(direccion, velocidad, periodo, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["direccion"] = from_union([lambda x: from_list(from_str, x), from_none], self.direccion)
        result["velocidad"] = from_union([lambda x: from_list(lambda x: from_str((lambda x: str(x))(x)), x), from_none], self.velocidad)
        result["periodo"] = from_str(self.periodo)
        result["value"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.value)
        return result


class Dia:
    estado_cielo: List[EstadoCielo]
    precipitacion: List[HumedadRelativa]
    nieve: List[HumedadRelativa]
    temperatura: List[HumedadRelativa]
    humedad_relativa: List[HumedadRelativa]
    viento_and_racha_max: List[VientoAndRachaMax]
    fecha: datetime
    orto: str
    ocaso: str

    def __init__(self, estado_cielo: List[EstadoCielo], precipitacion: List[HumedadRelativa],  nieve: List[HumedadRelativa],  temperatura: List[HumedadRelativa], humedad_relativa: List[HumedadRelativa], viento_and_racha_max: List[VientoAndRachaMax], fecha: datetime, orto: str, ocaso: str) -> None:
        self.estado_cielo = estado_cielo
        self.precipitacion = precipitacion
        self.nieve = nieve
        self.temperatura = temperatura
        self.humedad_relativa = humedad_relativa
        self.viento_and_racha_max = viento_and_racha_max
        self.fecha = fecha
        self.orto = orto
        self.ocaso = ocaso

    @staticmethod
    def from_dict(obj: Any) -> 'Dia':
        assert isinstance(obj, dict)
        estado_cielo = from_list(EstadoCielo.from_dict, obj.get("estadoCielo"))
        precipitacion = from_list(HumedadRelativa.from_dict, obj.get("precipitacion"))
        nieve = from_list(HumedadRelativa.from_dict, obj.get("nieve"))
        temperatura = from_list(HumedadRelativa.from_dict, obj.get("temperatura"))
        humedad_relativa = from_list(HumedadRelativa.from_dict, obj.get("humedadRelativa"))
        viento_and_racha_max = from_list(VientoAndRachaMax.from_dict, obj.get("vientoAndRachaMax"))
        fecha = from_datetime(obj.get("fecha"))
        orto = from_str(obj.get("orto"))
        ocaso = from_str(obj.get("ocaso"))
        return Dia(estado_cielo, precipitacion, nieve, temperatura,  humedad_relativa, viento_and_racha_max, fecha, orto, ocaso)

    def to_dict(self) -> dict:
        result: dict = {}
        result["estadoCielo"] = from_list(lambda x: to_class(EstadoCielo, x), self.estado_cielo)
        result["precipitacion"] = from_list(lambda x: to_class(HumedadRelativa, x), self.precipitacion)
        result["nieve"] = from_list(lambda x: to_class(HumedadRelativa, x), self.nieve)
        result["temperatura"] = from_list(lambda x: to_class(HumedadRelativa, x), self.temperatura)
        result["humedadRelativa"] = from_list(lambda x: to_class(HumedadRelativa, x), self.humedad_relativa)
        result["vientoAndRachaMax"] = from_list(lambda x: to_class(VientoAndRachaMax, x), self.viento_and_racha_max)
        result["fecha"] = self.fecha.isoformat()
        result["orto"] = from_str(self.orto)
        result["ocaso"] = from_str(self.ocaso)
        return result


class Prediccion:
    dia: List[Dia]

    def __init__(self, dia: List[Dia]) -> None:
        self.dia = dia

    @staticmethod
    def from_dict(obj: Any) -> 'Prediccion':
        assert isinstance(obj, dict)
        dia = from_list(Dia.from_dict, obj.get("dia"))
        return Prediccion(dia)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dia"] = from_list(lambda x: to_class(Dia, x), self.dia)
        return result


class WelcomeElement:
    elaborado: datetime
    prediccion: Prediccion
    id: int
    version: str

    def __init__(self, elaborado: datetime, prediccion: Prediccion, id: int, version: str) -> None:
        self.elaborado = elaborado
        self.prediccion = prediccion
        self.id = id
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeElement':
        assert isinstance(obj, dict)
        elaborado = from_datetime(obj.get("elaborado"))
        prediccion = Prediccion.from_dict(obj.get("prediccion"))
        id = int(from_str(obj.get("id")))
        version = from_str(obj.get("version"))
        return WelcomeElement(elaborado, prediccion, id, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["elaborado"] = self.elaborado.isoformat()
        result["prediccion"] = to_class(Prediccion, self.prediccion)
        result["id"] = from_str(str(self.id))
        result["version"] = from_str(self.version)
        return result


def welcome_from_dict(s: Any) -> List[WelcomeElement]:
    return from_list(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
    return from_list(lambda x: to_class(WelcomeElement, x), x)
