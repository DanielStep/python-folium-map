import folium
import pandas


def get_volcanoes():
    data = pandas.read_csv("volcanoes.txt")
    volcanoes = []
    for lt, ln, el in zip(list(data["LAT"]), list(data["LON"]), list(data["ELEV"])):
        volcanoes.append({
            "Lat": lt,
            "Lon": ln,
            "Elev": el,
            "Colour": colour_producer(el)
        })
    return volcanoes


def colour_producer(el):
    if el < 1000:
        return "green"
    elif 1000 <= el < 3000:
        return "orange"
    else:
        return "red"


fg = folium.FeatureGroup(name="My Map")

for v in get_volcanoes():
    fg.add_child(folium.CircleMarker(location=[v["Lat"], v["Lon"]], radius=6,
                                     popup=str(v["Elev"]), icon=folium.Icon(color=v["Colour"])))

map = folium.Map(location=[-37.819783, 144.957530], zoom_start=6,
                 tiles="Mapbox Bright")

map.add_child(fg)
map.save("Map1.html")
