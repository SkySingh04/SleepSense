import geocoder
from geopy.geocoders import Nominatim

g = geocoder.ip('me')
geolocator = Nominatim(user_agent='MyApp')
coordinates = g.latlng
location = geolocator.reverse(coordinates)
a = location.raw['address']
loc = a['amenity']+", "+a['road']+", "+a['suburb']+", "+a['city_district']+", "+a['city']
f = open('location.txt','w')
f.write(loc)
