from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Literal
import httpx
from datetime import datetime
import pytz

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить всем источникам доступ
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

OPENWEATHER_API_KEY = "daca8a4bf4432150158b5c32e6668342"  # Замените на ваш API ключ
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/"

@app.get("/weather/{city}")
async def get_weather(city: str, units: Literal['metric', 'imperial']):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f'{OPENWEATHER_BASE_URL}forecast', 
                                        params={
                                            'appid': OPENWEATHER_API_KEY,
                                            'q': city,
                                            'units': units
                                        })
            if response.status_code == 200:
                data = response.json()
                
                # Получаем временную зону города
                timezone_offset = data['city']['timezone']
                city_tz = pytz.FixedOffset(timezone_offset / 60)  # В OpenWeatherMap временная зона указана в секундах от UTC, преобразуем в минуты

                # Преобразуем текущее время в локальное время города
                now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
                now_city = now_utc.astimezone(city_tz)
                today_date = now_city.strftime('%Y-%m-%d')

                degree_symbol = '°C' if units == 'metric' else '°F'

                todays_forecast = [
                    {
                        'time': entry['dt_txt'].split(' ')[1][:5],  # Форматирование времени в 'HH:MM'
                        'temperature': entry['main']['temp'],
                        'pic_url': '/icons/weather.png'
                    }
                    for entry in data['list']
                    if entry['dt_txt'].startswith(today_date) and int(entry['dt_txt'].split(' ')[1].split(':')[0]) % 3 == 0
                ]

                # Отфильтровываем записи на текущий день
                today_entries = [entry for entry in data['list'] if entry['dt_txt'].startswith(today_date)]
                
                # Получаем максимальные и минимальные температуры с проверкой на пустоту
                temperature_max = max((entry['main']['temp_max'] for entry in today_entries), default=404)
                temperature_min = min((entry['main']['temp_min'] for entry in today_entries), default=404)

                weatherData = {
                    'degree_symbol': degree_symbol,
                    'now': 
                    {
                        'city': data['city']['name'],
                        'temperature_max': temperature_max,
                        'temperature_min': temperature_min
                    },
                    'now_details':
                    {
                        'temp': ['Temperature', data['list'][0]['main']['temp']],
                        'feels_like': ['Feels Like', data['list'][0]['main']['feels_like']],
                        'temp_min': ['Minimum Temperature', temperature_min],
                        'temp_max': ['Maximum Temperature', temperature_max],
                        'pressure': ['Pressure', data['list'][0]['main']['pressure']],
                        'humidity': ['Humidity', data['list'][0]['main']['humidity']],
                        'sea_level': ['Sea Level Pressure', data['list'][0]['main'].get('sea_level')],
                        'grnd_level': ['Ground Level Pressure', data['list'][0]['main'].get('grnd_level')],
                    },
                    'todays_forecast': todays_forecast
                }
                return weatherData
            else:
                raise HTTPException(status_code=response.status_code, detail=response.json())
        
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/weather/5days/{city}")
async def get_5dayweather(city: str, units: Literal['metric', 'imperial']):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f'{OPENWEATHER_BASE_URL}forecast', 
                                        params={
                                            'appid': OPENWEATHER_API_KEY,
                                            'q': city,
                                            'units': units
                                        })
            if response.status_code == 200:
                data = response.json()
                forecast_list = data.get('list', [])  # Используем .get() для списка прогнозов

                get5DayForecast = []

                # Добавляем информацию о городе вне цикла
                city_data = {
                    'name': data['city']['name'],
                    'coord': {
                        'lat': data['city']['coord']['lat'],
                        'lon': data['city']['coord']['lon']
                    },
                    'population': data['city'].get('population', None),  # Используем .get()
                }

                # Преобразуем время восхода и заката из Unix времени
                sunrise_unix = data['city']['sunrise']
                sunset_unix = data['city']['sunset']
                sunrise_time = datetime.fromtimestamp(sunrise_unix).strftime('%H:%M')
                sunset_time = datetime.fromtimestamp(sunset_unix).strftime('%H:%M')

                sun_data = {
                    'sunrise': sunrise_time,
                    'sunset': sunset_time
                }

                for forecast in forecast_list:
                    # Парсим дату и время из данных
                    dt = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
                    date_str = dt.date().isoformat()
                    time_str = dt.time().strftime('%H:%M')

                    # Ищем или создаем запись для текущей даты
                    day_forecast = next((item for item in get5DayForecast if item['date'] == date_str), None)
                    if not day_forecast:
                        day_forecast = {'date': date_str, 'hours': []}
                        get5DayForecast.append(day_forecast)

                    # Добавляем данные за конкретное время
                    hour_data = {
                        'time': time_str,
                        'main': {
                            'temp': forecast['main']['temp'],
                            'feels_like': forecast['main']['feels_like'],
                            'temp_min': forecast['main']['temp_min'],
                            'temp_max': forecast['main']['temp_max'],
                            'pressure': forecast['main']['pressure'],
                            'sea_level': forecast['main'].get('sea_level', None),
                            'grnd_level': forecast['main'].get('grnd_level', None),
                            'humidity': forecast['main']['humidity'],
                            'temp_kf': forecast['main'].get('temp_kf', None),
                        },
                        'weather': {
                            'clouds': {
                                'value': forecast['clouds']['all'],
                                'condition': forecast['weather'][0]['main'],
                                'description': forecast['weather'][0]['description'],
                            },
                            'wind': {
                                'speed': forecast['wind']['speed'],
                                'deg': forecast['wind']['deg'],
                                'gust': forecast['wind'].get('gust', None),
                            },
                            'rain': forecast.get('rain', {}).get('3h', None)  # Уточнение rain
                        }
                    }

                    day_forecast['hours'].append(hour_data)

                return {
                    "city": city_data,
                    "sun": sun_data,
                    "forecast": get5DayForecast
                }
            
            else:
                raise HTTPException(status_code=response.status_code, detail=response.json())
            
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=str(e))