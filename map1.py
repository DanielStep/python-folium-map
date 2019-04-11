import folium
import pandas


def get_countries():
    return open('world.json', 'r', encoding='utf-8-sig').read()


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


fgv = folium.FeatureGroup(name="Volcanoes")
for v in get_volcanoes():
    fgv.add_child(folium.CircleMarker(location=[v["Lat"], v["Lon"]],
                                      radius=6,
                                      popup=str(v["Elev"])+"m",
                                      fill_color=v["Colour"],
                                      color="grey",
                                      fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=get_countries(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                             else 'red'}))

map = folium.Map(location=[-37.819783, 144.957530], zoom_start=6,
                 tiles="Mapbox Bright")

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save("Map1.html")
