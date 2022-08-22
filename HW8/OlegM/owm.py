from pyowm import OWM
import lib.config as config

# ---------- FREE API KEY examples ---------------------

owm = OWM(config.KEY)
owm.config['language'] = 'ua'
mgr = owm.weather_manager()

name_of_city = 'Kyiv'
observation = mgr.weather_at_place(name_of_city)

w = observation.weather
print(f"Погода в {name_of_city}")
print(f"Загальний прогноз: {w.status}")
print(f"Детально: {w.detailed_status}")

print(f"Сила вітру: {w.wind().get('speed', '-')} км/год")
print(f"Напрямок вітру: {w.wind().get('deg', '-')} грудусів")

print(f"Дощь: {'-'if w.rain == {} else w.rain.get('1h',0)} мм.")

print(f"Вологість: {w.humidity} %")                # 87
print(f"Тиск: {w.pressure.get('press', 0)} мм.")

print(f"Температура: {w.temperature('celsius').get('temp', '-')} градусів")
print(f"Температура, відчувається як : {w.temperature('celsius').get('feels_like', '-')} градусів")

print(f"Нижня висота хмар: {w.clouds} м.")                  # 75
print(f"мінімальна видимість: {w.visibility_distance} м.")

print(f"Схід сонця: {w.sunrise_time(timeformat='date')} за грінвічем")
print(f"Захід сонця: {w.sunset_time(timeformat='date')} за грінвічем")


