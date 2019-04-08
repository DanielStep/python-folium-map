import folium


def add_markers(coord):
    global fg
    fg.add_child(folium.Marker(location=coord["loc"], popup=coord["name"]
                               , icon=folium.Icon(color="green")))


map = folium.Map(location=[-37.819783, 144.957530], zoom_start=6,
                 tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

coords = [
    {
        "loc": [-37.815737, 144.957790],
        "name": "Work"
    },
    {
        "loc": [-37.886362, 145.083086],
        "name": "Home"
    }
]

for coord in coords:
    add_markers(coord)

map.add_child(fg)
map.save("Map1.html")
