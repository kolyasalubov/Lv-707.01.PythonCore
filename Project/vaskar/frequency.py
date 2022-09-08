import geopy
from geopy import distance
geolocator = geopy.Nominatim(user_agent="tutorial")
# pu = ['Memphis TN', 'Jacksonville FL', 'ALLENTOWN PA', 'DALLAS TX', 'BURLINGTON NJ', 'WAYNE NJ', \
# 'SOMERSET NJ', 'TOPEKA KS', 'KEARNS UT', 'HORN LAKE MS', 'DAYTON NJ', 'JONESBORO AR', 'FAYETTEVILLE TN', \
#      'LACOMBE LA', 'PERRY FL', 'OCALA FL', 'JOLIET IL', 'PULASKI TN', 'KATHLEEN GA' ]
# deliv = ['Fresno CA', 'Cincinnati OH', 'Laredo TX', 'Atlanta GA', 'Mira Loma CA', 'Houston TX', \
#     'Chattanooga TN', 'Chicago IL',  'York PA', 'Fairport NY', 'Fort Worth TX', 'Rosenberg TX', 'Princeton KY', \
#          'Orlando FL', 'Phoenix AZ', 'Charlotte NC',  'Binghamton NY', 'Portland OR' 'Modesto CA', 'West Columbia SC' ]
pu = ['Memphis TN', 'Jacksonville FL', 'ALLENTOWN PA', 'ALLENTOWN PA', 'Hellertown PA']
deliv = ['Fresno CA', 'Cincinnati OH', 'Laredo TX', 'Laredo TX', 'Rio Bravo TX' ]
lanes = [str(a + " " +b) for a,b in zip(pu, deliv)]
print(lanes)
pu_longitudes = [geolocator.geocode(a).longitude for a in pu]
pu_latitudes = [geolocator.geocode(a).latitude for a in pu]
del_longitudes = [geolocator.geocode(a).longitude for a in deliv]
del_latitudes = [geolocator.geocode(a).latitude for a in deliv]
lane_frequency = {}
accounted_lanes = []
for l, a, b, c, d in zip(lanes, pu_latitudes, pu_longitudes, del_latitudes, del_longitudes):
    if l in accounted_lanes:
        continue
    else:
        for s, g,f,r,p in zip(lanes, pu_latitudes, pu_longitudes, del_latitudes, del_longitudes):
            print(distance.distance((a,b),(g,f)).miles, distance.distance((c,d),(r,p)).miles, l, s)
            if distance.distance((a,b),(g,f)).miles <50 and distance.distance((c,d),(r,p)).miles < 50:
                if l in lane_frequency:
                    lane_frequency[l] +=1
                else:
                    lane_frequency[l] = 1
            else:
                continue
    accounted_lanes.append(l)
print(lane_frequency)
