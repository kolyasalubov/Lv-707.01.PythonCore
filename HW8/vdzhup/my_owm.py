from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import my_config

# ---------- FREE API KEY examples ---------------------

owm = OWM(my_config.KEY)
mgr = owm.weather_manager()

input_city = input("Enter your city (location): ")

observation = mgr.weather_at_place(input_city)
w = observation.weather

status_cloud = w.detailed_status
speed_wind = w.wind()["speed"]               
humidity = w.humidity
temperature = w.temperature("celsius")["temp"]
feels_temperature = w.temperature("celsius")["feels_like"]
max_temperature = w.temperature("celsius")["temp_max"]   
min_temperature = w.temperature("celsius")["temp_min"]

print(f"In city {input_city} the status cloud is: {status_cloud}")
print(f"In city {input_city} the wind speed is: {speed_wind}")
print(f"In city {input_city} the humidity of the air is: {humidity}")
print(f"In city {input_city} the temperature of the air is: {temperature}, feels like: {feels_temperature}")
print(f"In city {input_city} the maximum temperature of the air is: {max_temperature}")
print(f"In city {input_city} the minimum temperature of the air is: {min_temperature}")
