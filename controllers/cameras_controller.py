from serializators.cameras_serializator import Cameras
import json
import datetime as dt

oobj = dt.datetime()

def export_cameras(cameras: Cameras):
    geojson = {
        "type": "FeatureCollection"
    }
    features_list = []
    cameras_list = cameras.camaras.camara
    for c in cameras_list:
        lat = c.posicion.latitud
        lon = c.posicion.longitud
        url = c.url
        description = c.fichero
        id = c.nombre
        feature = {
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(lon),
                    float(lat)
                ]
            },
            "type": "Feature",
            "properties": {
                "description": description,
                "marker-symbol": "cinema",
                "title": id,
                "url": url
            }
        }
        features_list.append(feature)
    geojson.update({"features": features_list})
    result = json.dumps(geojson)
    f = open("cameras.geojson", "w")
    f.write(result)
    f.close()
    print(geojson)
