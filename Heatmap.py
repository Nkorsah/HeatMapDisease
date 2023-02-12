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

map = folium.Map(location=[ 41.203323, -77.194527], zoom_start = 7.5)

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
    geo_data="https://gist.githubusercontent.com/wrobstory/5586482/raw/6031540596a4ff6cbfee13a5fc894588422fd3e6/us-counties.json",
    name="choropleth",
    data=dadata,
    columns=["fibs code", "risk_level"],
    key_on="feature.id",
    fill_color="YlOrRd",
    fill_opacity=0.35,
    line_opacity=0.5,
    legend_name="risk_level",
).add_to(map)

folium.LayerControl().add_to(map)

# HeatMap(cords, radius=50).add_to(map)


map.save('map.html')
webbrowser.open('map.html')