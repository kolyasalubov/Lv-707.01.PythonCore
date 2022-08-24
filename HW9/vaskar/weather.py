import pyowm

initer = pyowm.OWM('0dca045abeda9b280cab1140df689bd7')
loc = initer.weather_manager()

def weather(location):
    weather = loc.weather_at_place(location).weather[1]
    return location, weather

print(weather('Paris, FR'))