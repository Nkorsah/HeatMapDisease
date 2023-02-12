# CMD promp as administrator -> pip install Seaborn
# https://youtu.be/d07MOXnNlyI heatmap vid

# import seaborn
# import numpy
# import matplotlib.pylab
import folium
import webbrowser
from folium.plugins import HeatMap
from folium.features import GeoJsonTooltip
import geopandas as gpd
import pandas as pd

map = folium.Map(location=[39.95700996945959, -75.15569443929508], zoom_start = 9.5)

complete = open('complete.csv','r')
dadata = pd.read_csv('complete.csv')
data = complete.readlines()
latlong = []
cords = []
for line in data:
    datalist = line.split(",")
    if datalist[0] == 'fibs code':
        pass
    else:
        latlong = [float(datalist[3]), float(datalist[2]), float(datalist[4])]
        cords.append(latlong)

for item in cords:
    pass
folium.Choropleth(
    geo_data="https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json",
    name="choropleth",
    data=dadata,
    columns=["county", "long", "risk_level"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="risk_level",
).add_to(map)

folium.LayerControl().add_to(map)

# HeatMap(cords, radius=50).add_to(map)


map.save('map.html')
webbrowser.open('map.html')