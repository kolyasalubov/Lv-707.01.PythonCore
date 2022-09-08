import pyowm
from key import key

print(key)
initer = pyowm.OWM(key)
loc = initer.weather_manager()

def weather(location):
    weather = loc.weather_at_place(location).weather
    return location, weather

print(weather('Paris, FR'))
