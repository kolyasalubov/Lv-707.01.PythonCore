from pyowm import OWM
from configuration import API_KEY


owm = OWM(API_KEY)  

# Search for current weather in London (Great Britain)
manager_of_weather = owm.weather_manager()
observation = manager_of_weather.weather_at_place('Lviv,Ukraine')
location_of_weather = observation.weather

print(f"Detailed status is: {location_of_weather.detailed_status}")
print(f"Wind is: {location_of_weather.wind()}")
print(f"Humidity is: {location_of_weather.humidity}")
print(f"Temperature is: {location_of_weather.temperature('celsius')}")
print(f"Rain is: {location_of_weather.rain}")
print(f"Heat index is: {location_of_weather.heat_index}")
print(f"Clouds are: {location_of_weather.clouds}") 