# -*- coding: utf-8 -*-
"""210818.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16T8jZbuHPbXSP1afnCQFPVNmWuwyPsI2
"""

import folium

msp_osm=folium.Map(location=[45.5236, -122.6750])
msp_osm

stamen=folium.Map(location=[35.5394827878 , 129.3114679191],zoom_start=180)
stamen

stamen = folium.Map (location=[35.5394827878 , 129.3114679191],tiles='Stamen Toner',zoom_start=13)
stamen

stamen = folium.Map (location=[35.5394827878 , 129.3114679191],tiles='Stamen Terrain',zoom_start=13)
stamen

map_1 = folium.Map (location=[45.372 , -121.6972] , zoom_start=12 ,tiles='Stamen Terrain')
folium.Marker ([45.3288 , -121.6625] , popup = 'Mt. Hood Meadows' , icon=folium.Icon(icon='cloud')).add_to(map_1)
folium.Marker ([45.3311 , -121.7113] , popup='Timberline lodge' , icon=folium.Icon(icon='cloud')).add_to(map_1)
map_1

map_1 = folium.Map (location=[45.372 , -121.6972] , zoom_start=12 ,tiles='Stamen Terrain')
folium.Marker ([45.3288 , -121.6625] , popup = 'Mt. Hood Meadows' , icon=folium.Icon(icon='cloud')).add_to(map_1)
folium.Marker ([45.3311 , -121.7113] , popup='Timberline lodge' , icon=folium.Icon(color='green')).add_to(map_1)
folium.Marker ([45.3300 , -121.6823] , popup='Some Other Location' , icon=folium.Icon(color='red' , icon='info-sign')).add_to(map_1)
map_1

map_2 = folium.Map(location=[45.5236 , -122.6750] , tiles='Stamen Toner' , zoom_start=12)
folium.Marker([45.5244 , -122.6699] , popup='The Water front').add_to(map_2)
folium.CircleMarker([45.5215 , -122.6261] ,radius = 50 , popup = 'Laurelhrst park' , color='#3486cc' , fill_color = '#3186cc').add_to(map_2)
map_2

map_5 = folium.Map(location=[45.5236 , -122.6750] , zoom_start=13)
folium.RegularPolygonMarker([45.5012 , -122.6655] , popup='Ross Island Bridge' , fill_color='#132b5e' ,
                            number_of_sides=3 , radius=20).add_to(map_5)
folium.RegularPolygonMarker([45.5132 , -122.6078] , popup='Hawthorne Bridge' , fill_color='#132b5e' ,
                            number_of_sides=4 , radius=20).add_to(map_5)
folium.RegularPolygonMarker([45.5275 , -122.6692] , popup='Steel Bridge' , fill_color='#132b5e' ,
                            number_of_sides=5 , radius=20).add_to(map_5)
folium.RegularPolygonMarker([45.5318 , -122.6745] , popup='Broad Way Bridge' , fill_color='#132b5e' ,
                            number_of_sides=6 , radius=20).add_to(map_5)
map_5

"""# ??? ??????"""

