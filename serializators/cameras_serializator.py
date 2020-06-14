# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = cameras_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Posicion:
    latitud: str
    longitud: str

    def __init__(self, latitud: str, longitud: str) -> None:
        self.latitud = latitud
        self.longitud = longitud

    @staticmethod
    def from_dict(obj: Any) -> 'Posicion':
        assert isinstance(obj, dict)
        latitud = from_str(obj.get("Latitud"))
        longitud = from_str(obj.get("Longitud"))
        return Posicion(latitud, longitud)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Latitud"] = from_str(self.latitud)
        result["Longitud"] = from_str(self.longitud)
        return result


class Camara:
    posicion: Posicion
    nombre: str
    fichero: str
    url: str

    def __init__(self, posicion: Posicion, nombre: str, fichero: str, url: str) -> None:
        self.posicion = posicion
        self.nombre = nombre
        self.fichero = fichero
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Camara':
        assert isinstance(obj, dict)
        posicion = Posicion.from_dict(obj.get("Posicion"))
        nombre = from_str(obj.get("Nombre"))
        fichero = from_str(obj.get("Fichero"))
        url = from_str(obj.get("URL"))
        return Camara(posicion, nombre, fichero, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Posicion"] = to_class(Posicion, self.posicion)
        result["Nombre"] = from_str(self.nombre)
        result["Fichero"] = from_str(self.fichero)
        result["URL"] = from_str(self.url)
        return result


class Camaras:
    camara: List[Camara]

    def __init__(self, camara: List[Camara]) -> None:
        self.camara = camara

    @staticmethod
    def from_dict(obj: Any) -> 'Camaras':
        assert isinstance(obj, dict)
        camara = from_list(Camara.from_dict, obj.get("Camara"))
        return Camaras(camara)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Camara"] = from_list(lambda x: to_class(Camara, x), self.camara)
        return result


class Cameras:
    camaras: Camaras

    def __init__(self, camaras: Camaras) -> None:
        self.camaras = camaras

    @staticmethod
    def from_dict(obj: Any) -> 'Cameras':
        assert isinstance(obj, dict)
        camaras = Camaras.from_dict(obj.get("Camaras"))
        return Cameras(camaras)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Camaras"] = to_class(Camaras, self.camaras)
        return result


def cameras_from_dict(s: Any) -> Cameras:
    return Cameras.from_dict(s)


def cameras_to_dict(x: Cameras) -> Any:
    return to_class(Cameras, x)
