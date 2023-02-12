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
HeatMap(cords, radius=50).add_to(map)


map.save('map.html')
webbrowser.open('map.html')