from datetime import date
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from my_config import API_KEY

# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
city=input("Enter your city here:")
observation = mgr.weather_at_place(city)
w = observation.weather

print("w.detailed_status=",w.detailed_status)        # 'clouds'
speed_wind=w.wind() 
print(f"Wind speed in {city}=",speed_wind['speed'])                 # {'speed': 4.6, 'deg': 330}
print(f"Humidity in {city}=",w.humidity )               # 87
print(f"Current temperature in {city}:{w.temperature('celsius')['temp']}")
print(f"Max temperature in {city}:{w.temperature('celsius')['temp_max']}")
print(f"Min temperature in {city}:{w.temperature('celsius')['temp_min']}")
print(f"Feels like temperature in {city}:{w.temperature('celsius')['feels_like']}")
print(f"Rain in {city}=", w.rain)                 # {}
print(f"Heat index in {city}=", w.heat_index)         # None
print(f"Clouds in {city}=", w.clouds)           # 75



