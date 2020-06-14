# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = contaminacion_from_dict(json.loads(json_string))

from typing import List, Dict, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Datos:
    dato_horario: List[Dict[str, str]]

    def __init__(self, dato_horario: List[Dict[str, str]]) -> None:
        self.dato_horario = dato_horario

    @staticmethod
    def from_dict(obj: Any) -> 'Datos':
        assert isinstance(obj, dict)
        dato_horario = from_list(lambda x: from_dict(from_str, x), obj.get("Dato_Horario"))
        return Datos(dato_horario)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Dato_Horario"] = from_list(lambda x: from_dict(from_str, x), self.dato_horario)
        return result


class Contaminacion:
    datos: Datos

    def __init__(self, datos: Datos) -> None:
        self.datos = datos

    @staticmethod
    def from_dict(obj: Any) -> 'Contaminacion':
        assert isinstance(obj, dict)
        datos = Datos.from_dict(obj.get("Datos"))
        return Contaminacion(datos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Datos"] = to_class(Datos, self.datos)
        return result


def contaminacion_from_dict(s: Any) -> Contaminacion:
    return Contaminacion.from_dict(s)


def contaminacion_to_dict(x: Contaminacion) -> Any:
    return to_class(Contaminacion, x)
