# CMD promp as administrator -> pip install Seaborn
# https://youtu.be/d07MOXnNlyI heatmap vid

# import seaborn
# import numpy
# import matplotlib.pylab
import folium
import webbrowser
from folium.plugins import HeatMap



map = folium.Map(location=[39.95700996945959, -75.15569443929508], zoom_start = 9.5)

complete = open('complete.csv','r')
data = complete.readlines()
latlong = []
for line in data:
    datalist = line.split(",")
    if datalist[0] == 'fibs code':
        pass
    else:
        latlong = [float(datalist[2]), float(datalist[3])]
        print(latlong)
        HeatMap(latlong).add_to(map)

# lats_longs = [ [39.95700996945959,-75.15569443929508] ]
map.save('map.html')
# webbrowser.open('map.html')