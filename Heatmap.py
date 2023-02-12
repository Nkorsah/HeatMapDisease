# CMD promp as administrator -> pip install Seaborn
# https://youtu.be/d07MOXnNlyI heatmap vid

# import seaborn
# import numpy
# import matplotlib.pylab
import folium
import webbrowser
from folium.plugins import HeatMap




map = folium.Map(location=[39.95700996945959, -75.15569443929508], zoom_start = 9.5)



lats_longs = [ [39.95700996945959,-75.15569443929508] ]

HeatMap(lats_longs).add_to(map)
map.save('map.html')
webbrowser.open('map.html')