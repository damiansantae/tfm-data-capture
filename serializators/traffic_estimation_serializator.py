# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = traffic_estimation_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class CampoElement:
    variable: str
    valor: str

    @staticmethod
    def from_dict(obj: Any) -> 'CampoElement':
        assert isinstance(obj, dict)
        variable = from_str(obj.get("variable"))
        valor = from_str(obj.get("valor"))
        return CampoElement(variable, valor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["variable"] = from_str(self.variable)
        result["valor"] = from_str(self.valor)
        return result


@dataclass
class Estimacion:
    campo: List[CampoElement]

    @staticmethod
    def from_dict(obj: Any) -> 'Estimacion':
        assert isinstance(obj, dict)
        campo = from_list(CampoElement.from_dict, obj.get("campo"))
        return Estimacion(campo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["campo"] = from_list(lambda x: to_class(CampoElement, x), self.campo)
        return result


@dataclass
class FechaActualizacionCampo:
    nombre: str
    valor: str

    @staticmethod
    def from_dict(obj: Any) -> 'FechaActualizacionCampo':
        assert isinstance(obj, dict)
        nombre = from_str(obj.get("nombre"))
        valor = from_str(obj.get("valor"))
        return FechaActualizacionCampo(nombre, valor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nombre"] = from_str(self.nombre)
        result["valor"] = from_str(self.valor)
        return result


@dataclass
class FechaActualizacion:
    campo: FechaActualizacionCampo

    @staticmethod
    def from_dict(obj: Any) -> 'FechaActualizacion':
        assert isinstance(obj, dict)
        campo = FechaActualizacionCampo.from_dict(obj.get("campo"))
        return FechaActualizacion(campo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["campo"] = to_class(FechaActualizacionCampo, self.campo)
        return result


@dataclass
class Estimaciones:
    fecha_actualizacion: FechaActualizacion
    estimacion: List[Estimacion]

    @staticmethod
    def from_dict(obj: Any) -> 'Estimaciones':
        assert isinstance(obj, dict)
        fecha_actualizacion = FechaActualizacion.from_dict(obj.get("FechaActualizacion"))
        estimacion = from_list(Estimacion.from_dict, obj.get("Estimacion"))
        return Estimaciones(fecha_actualizacion, estimacion)

    def to_dict(self) -> dict:
        result: dict = {}
        result["FechaActualizacion"] = to_class(FechaActualizacion, self.fecha_actualizacion)
        result["Estimacion"] = from_list(lambda x: to_class(Estimacion, x), self.estimacion)
        return result


@dataclass
class TrafficEstimation:
    estimaciones: Estimaciones

    @staticmethod
    def from_dict(obj: Any) -> 'TrafficEstimation':
        assert isinstance(obj, dict)
        estimaciones = Estimaciones.from_dict(obj.get("Estimaciones"))
        return TrafficEstimation(estimaciones)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Estimaciones"] = to_class(Estimaciones, self.estimaciones)
        return result


def traffic_estimation_from_dict(s: Any) -> TrafficEstimation:
    return TrafficEstimation.from_dict(s)


def traffic_estimation_to_dict(x: TrafficEstimation) -> Any:
    return to_class(TrafficEstimation, x)
