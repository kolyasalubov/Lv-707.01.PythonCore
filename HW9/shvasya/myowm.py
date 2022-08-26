from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('01db8804fa037ca575861deedde54b50')
mgr = owm.weather_manager()

input_city = input("What city are you in? ")

observation = mgr.weather_at_place(input_city)
w = observation.weather

status_clouds = w.detailed_status         # 'clouds'
speed_wind = w.wind()['speed']                  # {'speed': 4.6, 'deg': 330}
humidity = w.humidity                # 87
temperature_max = w.temperature('celsius')['temp_max']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
temperature = w.temperature('celsius')['temp'] 
temperature_min = w.temperature('celsius')['temp_min']

print(f"in the city of {input_city} the average temperature is {temperature} ")
print(f"in the city of {input_city} the max temperature is {temperature_max} ")
print(f"in the city of {input_city} the min temperature is {temperature_min} ")
print(f"in the city of {input_city} the condition with clouds are {status_clouds}")
print(f"in the city of {input_city} the wind speed is {speed_wind}")
print(f"in the city of {input_city} the level of humidity is {humidity}")