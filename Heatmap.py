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
        latlong = [float(datalist[3]), float(datalist[2])]
        cords.append(latlong)

for item in cords:
    # print(item[1])
    pass

lats_longs = [
                [38.27312, -98.5821872], # Kansas
                [34.395342, -111.763275], # Arizona
                [37.5726028, -85.1551411], # Kentucky
                [32.3293809, -83.1137366], # Georgia
                [40.0796606, -89.4337288], # Illiniois
            ]

HeatMap(cords).add_to(map)


map.save('map.html')
webbrowser.open('map.html')