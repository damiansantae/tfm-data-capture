import xmltodict
import json as js


##Recoger JSON
def to_json(data):
    parse_data = xmltodict.parse(data.text)
    json = js.dumps(parse_data)
    return json


# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = empty_from_dict(json.loads(json_string))

from enum import Enum
from typing import Optional, Any, List, TypeVar, Type, Callable, cast

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Pm:
    idelem: int
    descripcion: Optional[str]
    acceso_asociado: Optional[str]
    intensidad: int
    ocupacion: int
    carga: int
    nivel_servicio: str
    intensidad_sat: Optional[int]
    error: str
    subarea: Optional[str]
    st_x: str
    st_y: str
    velocidad: Optional[int]

    def __init__(self, idelem: int, descripcion: Optional[str], acceso_asociado: Optional[str], intensidad: int,
                 ocupacion: int, carga: int, nivel_servicio: str, intensidad_sat: Optional[int], error: str,
                 subarea: Optional[str], st_x: str, st_y: str, velocidad: Optional[int]) -> None:
        self.idelem = idelem
        self.descripcion = descripcion
        self.acceso_asociado = acceso_asociado
        self.intensidad = intensidad
        self.ocupacion = ocupacion
        self.carga = carga
        self.nivel_servicio = nivel_servicio
        self.intensidad_sat = intensidad_sat
        self.error = error
        self.subarea = subarea
        self.st_x = st_x
        self.st_y = st_y
        self.velocidad = velocidad

    @staticmethod
    def from_dict(obj: Any) -> 'Pm':
        assert isinstance(obj, dict)
        idelem = int(from_str(obj.get("idelem")))
        descripcion = from_union([from_str, from_none], obj.get("descripcion"))
        acceso_asociado = from_union([from_str, from_none], obj.get("accesoAsociado"))
        intensidad = int(from_str(obj.get("intensidad")))
        ocupacion = int(from_str(obj.get("ocupacion")))
        carga = int(from_str(obj.get("carga")))
        try:
            nivel_servicio = from_str(obj.get("nivelServicio"))
        except:
            nivel_servicio = '99'
        intensidad_sat = from_union([from_none, lambda x: int(from_str(x))], obj.get("intensidadSat"))
        try:
            error = from_str(obj.get("error"))
        except:
            error = 'S'
        subarea = from_union([from_str, from_none], obj.get("subarea"))
        st_x = from_str(obj.get("st_x"))
        st_y = from_str(obj.get("st_y"))
        velocidad = from_union([from_none, lambda x: int(from_str(x))], obj.get("velocidad"))
        return Pm(idelem, descripcion, acceso_asociado, intensidad, ocupacion, carga, nivel_servicio, intensidad_sat,
                  error, subarea, st_x, st_y, velocidad)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idelem"] = from_str(str(self.idelem))
        result["descripcion"] = from_union([from_str, from_none], self.descripcion)
        result["accesoAsociado"] = from_union([from_str, from_none], self.acceso_asociado)
        result["intensidad"] = from_str(str(self.intensidad))
        result["ocupacion"] = from_str(str(self.ocupacion))
        result["carga"] = from_str(str(self.carga))
        result["nivelServicio"] = from_str(self.nivel_servicio)
        result["intensidadSat"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                                              lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))],
                                             self.intensidad_sat)
        result["error"] = from_str(self.error)
        result["subarea"] = from_union([from_str, from_none], self.subarea)
        result["st_x"] = from_str(self.st_x)
        result["st_y"] = from_str(self.st_y)
        result["velocidad"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                                          lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))],
                                         self.velocidad)
        return result


class Pms:
    fecha_hora: str
    pm: List[Pm]

    def __init__(self, fecha_hora: str, pm: List[Pm]) -> None:
        self.fecha_hora = fecha_hora
        self.pm = pm

    @staticmethod
    def from_dict(obj: Any) -> 'Pms':
        assert isinstance(obj, dict)
        fecha_hora = from_str(obj.get("fecha_hora"))
        pm = from_list(Pm.from_dict, obj.get("pm"))
        return Pms(fecha_hora, pm)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fecha_hora"] = from_str(self.fecha_hora)
        result["pm"] = from_list(lambda x: to_class(Pm, x), self.pm)
        return result


class TrafficAPI:
    pms: Pms

    def __init__(self, pms: Pms) -> None:
        self.pms = pms

    @staticmethod
    def from_dict(obj: Any) -> 'TrafficAPI':
        assert isinstance(obj, dict)
        pms = Pms.from_dict(obj.get("pms"))
        return TrafficAPI(pms)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pms"] = to_class(Pms, self.pms)
        return result


def empty_from_dict(s: Any) -> TrafficAPI:
    return TrafficAPI.from_dict(s)


def empty_to_dict(x: TrafficAPI) -> Any:
    return to_class(TrafficAPI, x)
