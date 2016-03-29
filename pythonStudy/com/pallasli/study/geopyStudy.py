'''
Created on 2016年3月24日

@author: lyt
'''
# 地理编码

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address) 
print((location.latitude, location.longitude)) 
print(location.raw) 
# 反地理编码

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.reverse("52.509669, 13.376294")
print(location.address) 
print((location.latitude, location.longitude)) 
print(location.raw) 
# 计算距离

# geopy能使用经纬度距离公式（ Vincenty distance ） 或球面距离（ great-circle distance ）公式在两点间计算测地距离。在geopy中用的经纬度距离是默认的方式，类为geopy.distance.distance，计算距离为其属性（e.g.,  miles ,  meters , etc）。

# 给出计算经纬度距离的例子如下：

from geopy.distance import vincenty
 
newport_ri = (21.49008, -32.312796)
cleveland_oh = (11.499498, -43.695391) 
print(vincenty(newport_ri, cleveland_oh).miles) 
# 使用球面距离：

from geopy.distance import great_circle
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(great_circle(newport_ri, cleveland_oh).miles) 