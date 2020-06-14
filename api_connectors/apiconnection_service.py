#  Copyright (c) 2020.

from urllib.request import urlopen, Request

import ssl
import zlib
import xmltodict

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


class APIConnection:
    cameras_url: str = "https://www.mc30.es/components/com_hotspots/datos/camaras.xml"
    incicencias_url: str = "http://www.mc30.es/components/com_hotspots/datos/incidencias.xml"
    estimaciones_trafico: str = "http://www.mc30.es/images/xml/EstimacionesTrafico.xml"
    traffic_data_url: str = "http://informo.munimadrid.es/informo/tmadrid/pm.xml"
    # contamination_url :str = "https://datos.madrid.es/egob/catalogo/212531-10515086-calidad-aire-tiempo-real.csv"

    def __init__(self):
        super().__init__()

    def to_json(self, data):
        parse_data = xmltodict.parse(data)
        jsond = json.dumps(parse_data)
        return jsond

    def get_cameras(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
            'Accept-Encoding': 'gzip,deflate',
            'Host': 'www.mc30.es',
            'DNT': '1',
            'Connection': 'Keep-Alive',
        }
        # reg_url = "http://www.mc30.es/components/com_hotspots/datos/camaras.xml"
        # req = Request(url=reg_url, headers=headers)
        # contents = urlopen(req).read()

        conn = http.client.HTTPConnection("mc30.es")
        conn.request("GET",
                     "/components/com_hotspots/datos/camaras.xml",
                     headers=headers)
        res = conn.getresponse()

        encoding = self.get_encoding(res)
        if encoding == 'gzip':
            data = zlib.decompress(res.read(), 16 + zlib.MAX_WBITS).decode('utf-8')
        else:
            data = res.read().decode(encoding)

        jsond = self.to_json(data)
        return jsond

    def get_trabajos_planificados(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
            'Accept-Encoding': 'gzip,deflate',
            'Host': 'www.mc30.es',
            'DNT': '1',
            'Connection': 'Keep-Alive',
        }
        # reg_url = "http://www.mc30.es/components/com_hotspots/datos/camaras.xml"
        # req = Request(url=reg_url, headers=headers)
        # contents = urlopen(req).read()

        conn = http.client.HTTPConnection("mc30.es")
        conn.request("GET",
                     "/images/xml/TrabajosPlanificados.xml",
                     headers=headers)
        res = conn.getresponse()

        encoding = self.get_encoding(res)
        if encoding == 'gzip':
            data = zlib.decompress(res.read(), 16 + zlib.MAX_WBITS).decode('utf-8')
        else:
            data = res.read().decode(encoding)

        jsond = self.to_json(data)
        return jsond

    def get_traffic_estimation(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
            'Accept-Encoding': 'gzip,deflate',
            'Host': 'www.mc30.es',
            'DNT': '1',
            'Connection': 'Keep-Alive',
        }

        conn = http.client.HTTPConnection("mc30.es")
        conn.request("GET",
                     "/images/xml/EstimacionesTrafico.xml",
                     headers=headers)
        res = conn.getresponse()

        encoding = self.get_encoding(res)
        if encoding == 'gzip':
            data = zlib.decompress(res.read(), 16 + zlib.MAX_WBITS).decode('utf-8')
        else:
            data = res.read().decode(encoding)

        jsond = self.to_json(data)
        return jsond

    def get_encoding(self, res) -> str:
        headers = res.getheaders()
        enconding = headers[7][1]
        return enconding

    def get_traffic_data_urls(self):
        res = urlopen(self.traffic_data_url).read()
        data = res.decode("utf-8")
        jsond = self.to_json(data)
        return jsond

    def get_contamination(self):
        ##Configuracion de cabecera HTTP
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
            'Accept-Encoding': 'gzip,deflate',
            'Host': 'www.mambiente.madrid.es',
            'Connection': 'Keep-Alive',
        }
        ##Creacion de conexion HTTP el dominio
        conn = http.client.HTTPConnection("www.mambiente.madrid.es")
        ##Envio de peticion a la API
        conn.request("GET",
                     "/opendata/horario.xml",
                     headers=headers)
        ##Respuesta HTTP
        res = conn.getresponse()
        ##Decodificacion del contenido del mensaje
        data = res.read().decode('iso-8859-1')
        ##parse a objeto json
        jsond = self.to_json(data)
        return jsond




import http.client
import json


class AEMETAPI_Connection:
    apikey: str
    madrid_code = 28079
    api_url: str

    headers = {
        'cache-control': "no-cache"
    }
    api_url = ""
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkYW1pYW4uc2FudGFtYXJpYWVAYWx1bW5vcy51cG0uZXMiLCJqdGkiOiIxNjA3YTRmMS02NzJhLTQzNTQtYTJiOS05OWUxZjYwYWIyMDYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTU4MTcwNzQ3OSwidXNlcklkIjoiMTYwN2E0ZjEtNjcyYS00MzU0LWEyYjktOTllMWY2MGFiMjA2Iiwicm9sZSI6IiJ9.Oaa9P7N6PdJrC0hxlMAtKBHSsihfr3y0Y3EOaehx-f8"

    def __init__(self):
        super().__init__()

    def get_daily_weather(self):
        conn = http.client.HTTPSConnection("opendata.aemet.es")
        conn.request("GET",
                     "/opendata/api/prediccion/especifica/municipio/horaria/28079?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkYW1pYW4uc2FudGFtYXJpYWVAYWx1bW5vcy51cG0uZXMiLCJqdGkiOiIxNjA3YTRmMS02NzJhLTQzNTQtYTJiOS05OWUxZjYwYWIyMDYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTU4MTcwNzQ3OSwidXNlcklkIjoiMTYwN2E0ZjEtNjcyYS00MzU0LWEyYjktOTllMWY2MGFiMjA2Iiwicm9sZSI6IiJ9.Oaa9P7N6PdJrC0hxlMAtKBHSsihfr3y0Y3EOaehx-f8",
                     headers=self.headers)
        res = conn.getresponse()
        data = res.read().decode("iso8859-1")

        y = json.loads(data)
        datos = y["datos"]

        bytes = urlopen(datos).read()

        json_data1 = bytes.decode("iso8859-1")
        json_data = json_data1.encode("utf-8")

        return json_data
