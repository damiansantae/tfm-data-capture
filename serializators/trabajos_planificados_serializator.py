# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = trabajos_planificados_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, Union, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class CampoCampo:
    variable: str
    nombre: str
    posicion: int
    prioridad: int

    @staticmethod
    def from_dict(obj: Any) -> 'CampoCampo':
        assert isinstance(obj, dict)
        variable = from_str(obj.get("variable"))
        nombre = from_str(obj.get("nombre"))
        posicion = int(from_str(obj.get("posicion")))
        prioridad = int(from_str(obj.get("prioridad")))
        return CampoCampo(variable, nombre, posicion, prioridad)

    def to_dict(self) -> dict:
        result: dict = {}
        result["variable"] = from_str(self.variable)
        result["nombre"] = from_str(self.nombre)
        result["posicion"] = from_str(str(self.posicion))
        result["prioridad"] = from_str(str(self.prioridad))
        return result


@dataclass
class Cabecera:
    campo: List[Union[CampoCampo, str]]

    @staticmethod
    def from_dict(obj: Any) -> 'Cabecera':
        assert isinstance(obj, dict)
        campo = from_list(lambda x: from_union([CampoCampo.from_dict, from_str], x), obj.get("campo"))
        return Cabecera(campo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["campo"] = from_list(lambda x: from_union([lambda x: to_class(CampoCampo, x), from_str], x), self.campo)
        return result


@dataclass
class ColorZoomCampo:
    nombre: str
    valor: str

    @staticmethod
    def from_dict(obj: Any) -> 'ColorZoomCampo':
        assert isinstance(obj, dict)
        nombre = from_str(obj.get("nombre"))
        valor = from_str(obj.get("valor"))
        return ColorZoomCampo(nombre, valor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nombre"] = from_str(self.nombre)
        result["valor"] = from_str(self.valor)
        return result


@dataclass
class ColorZoom:
    campo: ColorZoomCampo

    @staticmethod
    def from_dict(obj: Any) -> 'ColorZoom':
        assert isinstance(obj, dict)
        campo = ColorZoomCampo.from_dict(obj.get("campo"))
        return ColorZoom(campo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["campo"] = to_class(ColorZoomCampo, self.campo)
        return result


@dataclass
class TrabajoPlanificadoCampo:
    variable: str
    valor: str

    @staticmethod
    def from_dict(obj: Any) -> 'TrabajoPlanificadoCampo':
        assert isinstance(obj, dict)
        variable = from_str(obj.get("variable"))
        valor = from_str(obj.get("valor"))
        return TrabajoPlanificadoCampo(variable, valor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["variable"] = from_str(self.variable)
        result["valor"] = from_str(self.valor)
        return result


@dataclass
class Punto:
    latitud: str
    longitud: str

    @staticmethod
    def from_dict(obj: Any) -> 'Punto':
        assert isinstance(obj, dict)
        latitud = from_str(obj.get("Latitud"))
        longitud = from_str(obj.get("Longitud"))
        return Punto(latitud, longitud)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Latitud"] = from_str(self.latitud)
        result["Longitud"] = from_str(self.longitud)
        return result


@dataclass
class Puntos:
    punto: List[Punto]

    @staticmethod
    def from_dict(obj: Any) -> 'Puntos':
        assert isinstance(obj, dict)
        punto = from_list(Punto.from_dict, obj.get("Punto"))
        return Puntos(punto)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Punto"] = from_list(lambda x: to_class(Punto, x), self.punto)
        return result


@dataclass
class TrabajosARealizar:
    trabajo: Union[List[str], str]

    @staticmethod
    def from_dict(obj: Any) -> 'TrabajosARealizar':
        assert isinstance(obj, dict)
        trabajo = from_union([lambda x: from_list(from_str, x), from_str], obj.get("Trabajo"))
        return TrabajosARealizar(trabajo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Trabajo"] = from_union([lambda x: from_list(from_str, x), from_str], self.trabajo)
        return result


@dataclass
class TrabajosARealizarIngles:
    trabajo_ingles: Union[List[str], str]

    @staticmethod
    def from_dict(obj: Any) -> 'TrabajosARealizarIngles':
        assert isinstance(obj, dict)
        trabajo_ingles = from_union([lambda x: from_list(from_str, x), from_str], obj.get("TrabajoIngles"))
        return TrabajosARealizarIngles(trabajo_ingles)

    def to_dict(self) -> dict:
        result: dict = {}
        result["TrabajoIngles"] = from_union([lambda x: from_list(from_str, x), from_str], self.trabajo_ingles)
        return result


@dataclass
class TrabajoPlanificado:
    campo: List[TrabajoPlanificadoCampo]
    trabajos_a_realizar: TrabajosARealizar
    trabajos_a_realizar_ingles: TrabajosARealizarIngles
    puntos: Puntos
    zoom: Puntos
    color: str
    tipo_corte: str
    tipo_corte_ingles: str
    estado_corte: str
    estado_corte_ingles: str
    fecha_inicio: str
    fecha_fin: str
    expediente: int
    horario: str

    @staticmethod
    def from_dict(obj: Any) -> 'TrabajoPlanificado':
        assert isinstance(obj, dict)
        campo = from_list(TrabajoPlanificadoCampo.from_dict, obj.get("campo"))
        trabajos_a_realizar = TrabajosARealizar.from_dict(obj.get("TrabajosARealizar"))
        trabajos_a_realizar_ingles = TrabajosARealizarIngles.from_dict(obj.get("TrabajosARealizarIngles"))
        puntos = Puntos.from_dict(obj.get("Puntos"))
        zoom = Puntos.from_dict(obj.get("Zoom"))
        color = from_str(obj.get("Color"))
        tipo_corte = from_str(obj.get("TipoCorte"))
        tipo_corte_ingles = from_str(obj.get("TipoCorteIngles"))
        estado_corte = from_str(obj.get("EstadoCorte"))
        estado_corte_ingles = from_str(obj.get("EstadoCorteIngles"))
        fecha_inicio = from_str(obj.get("FechaInicio"))
        fecha_fin = from_str(obj.get("FechaFin"))
        expediente = int(from_str(obj.get("Expediente")))
        horario = from_str(obj.get("Horario"))
        return TrabajoPlanificado(campo, trabajos_a_realizar, trabajos_a_realizar_ingles, puntos, zoom, color,
                                  tipo_corte, tipo_corte_ingles, estado_corte, estado_corte_ingles, fecha_inicio,
                                  fecha_fin, expediente, horario)

    def to_dict(self) -> dict:
        result: dict = {}
        result["campo"] = from_list(lambda x: to_class(TrabajoPlanificadoCampo, x), self.campo)
        result["TrabajosARealizar"] = to_class(TrabajosARealizar, self.trabajos_a_realizar)
        result["TrabajosARealizarIngles"] = to_class(TrabajosARealizarIngles, self.trabajos_a_realizar_ingles)
        result["Puntos"] = to_class(Puntos, self.puntos)
        result["Zoom"] = to_class(Puntos, self.zoom)
        result["Color"] = from_str(self.color)
        result["TipoCorte"] = from_str(self.tipo_corte)
        result["TipoCorteIngles"] = from_str(self.tipo_corte_ingles)
        result["EstadoCorte"] = from_str(self.estado_corte)
        result["EstadoCorteIngles"] = from_str(self.estado_corte_ingles)
        result["FechaInicio"] = from_str(self.fecha_inicio)
        result["FechaFin"] = from_str(self.fecha_fin)
        result["Expediente"] = from_str(str(self.expediente))
        result["Horario"] = from_str(self.horario)
        return result


@dataclass
class TrabajosPlanificadosClass:
    fecha_actualizacion: ColorZoom
    color_zoom: ColorZoom
    cabecera: Cabecera
    trabajo_planificado: List[TrabajoPlanificado]

    @staticmethod
    def from_dict(obj: Any) -> 'TrabajosPlanificadosClass':
        assert isinstance(obj, dict)
        fecha_actualizacion = ColorZoom.from_dict(obj.get("FechaActualizacion"))
        color_zoom = ColorZoom.from_dict(obj.get("ColorZoom"))
        cabecera = Cabecera.from_dict(obj.get("Cabecera"))
        trabajo_planificado = from_list(TrabajoPlanificado.from_dict, obj.get("TrabajoPlanificado"))
        return TrabajosPlanificadosClass(fecha_actualizacion, color_zoom, cabecera, trabajo_planificado)

    def to_dict(self) -> dict:
        result: dict = {}
        result["FechaActualizacion"] = to_class(ColorZoom, self.fecha_actualizacion)
        result["ColorZoom"] = to_class(ColorZoom, self.color_zoom)
        result["Cabecera"] = to_class(Cabecera, self.cabecera)
        result["TrabajoPlanificado"] = from_list(lambda x: to_class(TrabajoPlanificado, x), self.trabajo_planificado)
        return result


@dataclass
class TrabajosPlanificados:
    trabajos_planificados: TrabajosPlanificadosClass

    @staticmethod
    def from_dict(obj: Any) -> 'TrabajosPlanificados':
        assert isinstance(obj, dict)
        trabajos_planificados = TrabajosPlanificadosClass.from_dict(obj.get("TrabajosPlanificados"))
        return TrabajosPlanificados(trabajos_planificados)

    def to_dict(self) -> dict:
        result: dict = {}
        result["TrabajosPlanificados"] = to_class(TrabajosPlanificadosClass, self.trabajos_planificados)
        return result


def trabajos_planificados_from_dict(s: Any) -> TrabajosPlanificados:
    return TrabajosPlanificados.from_dict(s)


def trabajos_planificados_to_dict(x: TrabajosPlanificados) -> Any:
    return to_class(TrabajosPlanificados, x)
