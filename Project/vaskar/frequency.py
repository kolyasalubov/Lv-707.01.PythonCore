from math import sin, cos, sqrt, atan2, radians
import geopy
from geopy import distance
geolocator = geopy.Nominatim(user_agent="tutorial")
loads = ['Memphis TN', 'Jacksonville FL', 'ALLENTOWN PA', 'DALLAS TX', 'BURLINGTON NJ', 'WAYNE NJ', \
'SOMERSET NJ', 'TOPEKA KS', 'KEARNS UT', 'HORN LAKE MS', 'DAYTON NJ', 'JONESBORO AR', 'FAYETTEVILLE TN', \
     'LACOMBE LA', 'PERRY FL', 'OCALA FL', 'JOLIET IL', 'PULASKI TN', 'KATHLEEN GA' ]
longitudes = [geolocator.geocode(a).longitude for a in loads]
latitudes = [geolocator.geocode(a).latitude for a in loads]
frequency = {}
for l, a, b in zip(loads, latitudes, longitudes):
    for g,f in zip(latitudes, longitudes):
        if distance.distance((a,b),(g,f)).miles <1000:
            if l in frequency:
                frequency[l] +=1
            else:
                frequency[l] = 1
        else:
            continue
print(frequency)
