from pickle import TRUE
from turtle import color
import folium
import pandas
def color_producer(elevation):
        if elevation<1000:
                return "black"
        elif 1000<=elevation <3000:
                return "purple"
        else :
                return "green"

map=folium.Map(location=[34.9312, 72.4171],zoom_start=10)
fgv=folium.FeatureGroup(name="Volcanoes")
fgp=folium.FeatureGroup(name="population")
fgve=folium.FeatureGroup(name="Village")
fgt=folium.FeatureGroup(name="Toursit spots")


fgve.add_child(folium.Marker(location=[35.00025814827912, 72.45042793207188],popup="Bara Drushkhela",
icon=folium.Icon(color="red")))
for coordinates in [[35.17, 72.36],[35.492, 72.57780]] :
        fgt.add_child(folium.Marker(location=coordinates,popup="Tourist spot",icon=folium.Icon(color="blue")))
data1=pandas.read_csv("web_Mapping/Volcanoes.txt")
lat=list(data1["LAT"])
lon=list(data1["LON"])
el=list(data1["ELEV"])
for lt,ln,ele in zip(lat,lon,el):
        fgv.add_child(folium.Marker(location=(lt,ln),popup=str(ele)+" m"+"Volcano",
        icon=folium.Icon(color=color_producer(ele))))
fgp.add_child(folium.GeoJson(data=open("web_Mapping/world.json",'r',encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor":"green"if x['properties']['POP2005']<10000000 else "yellow" 
 if  10000000<= x['properties']['POP2005']
<20000000 else "red" }))



map.add_child(fgv)
map.add_child(fgve)
map.add_child(fgp)
map.add_child(fgt)
map.add_child(folium.LayerControl())
map.save("Map2.html")

        
        