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
    allow_origins=["*"],  # Здесь можно указать конкретные домены, если нужно
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

                todays_forecast = [
                    {
                        'time': entry['dt_txt'].split(' ')[1][:5],  # Форматирование времени в 'HH:MM'
                        'temperature': entry['main']['temp'],
                        'pic_url': '/icons/weather.png'
                    }
                    for entry in data['list']
                    if entry['dt_txt'].startswith(today_date) and int(entry['dt_txt'].split(' ')[1].split(':')[0]) % 3 == 0
                ]

                weatherData = {
                    'now': 
                    {
                        'city': data['city']['name'],
                        'temperature_max': max(entry['main']['temp_max'] for entry in data['list'] if entry['dt_txt'].startswith(today_date)),
                        'temperature_min': min(entry['main']['temp_min'] for entry in data['list'] if entry['dt_txt'].startswith(today_date))
                    },
                    'now_details':
                    {
                        'temp': ['Temperature', data['list'][0]['main']['temp']],
                        'feels_like': ['Feels Like', data['list'][0]['main']['feels_like']],
                        'temp_min': ['Minimum Temperature', min(entry['main']['temp_min'] for entry in data['list'] if entry['dt_txt'].startswith(today_date))],
                        'temp_max': ['Maximum Temperature', max(entry['main']['temp_max'] for entry in data['list'] if entry['dt_txt'].startswith(today_date))],
                        'pressure': ['Pressure', data['list'][0]['main']['pressure']],
                        'humidity': ['Humidity', data['list'][0]['main']['humidity']],
                        'sea_level': ['Sea Level Pressure', data['list'][0]['main'].get('sea_level')],
                        'grnd_level': ['Ground Level Pressure', data['list'][0]['main'].get('grnd_level')],
                    },
                    'todays_forecast': todays_forecast
                }
                return weatherData
            else:
                raise HTTPException(status_code=response.status_code,
                                    detail=f"{response.json()}")
        
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=str(e))



#   // weatherData.value = {
#   //   'now': {
#   //     'city': searchData.city,
#   //     'temperature_max': 12,
#   //     'temperature_min': -3
#   //   },
#   //   'now_details': {
#   //     'sunrise': ['Sunrise', '8:18'],
#   //     'sunset': ['Sunrset', '18:40'],
#   //     'chance_of_rain': ['Rain chance', 21],
#   //     'pressure': ['Rain chance', 21],
#   //     'detail5': ['Rain chance', 21],
#   //     'detail6': ['Rain chance', 21],
#   //     'detail7': ['Rain chance', 21],
#   //     'detail8': ['Rain chance', 21]
#   //   },
#   //   'todays_forecast': [
#   //     {
#   //       'time': '3:00',
#   //       'temperature': 3,
#   //       'pic_url': '/icons/weather.png'
#   //     },
#   //     {
#   //       'time': '6:00',
#   //       'temperature': 6,
#   //       'pic_url': '/icons/weather.png'
#   //     },
#   //     {
#   //       'time': '9:00',
#   //       'temperature': 9,
#   //       'pic_url': '/icons/weather.png'
#   //     },
#   //     {
#   //       'time': '12:00',
#   //       'temperature': 12,
#   //       'pic_url': '/icons/weather.png'
#   //     },
#   //     {
#   //       'time': '15:00',
#   //       'temperature': 15,
#   //       'pic_url': '/icons/weather.png'
#   //     },
#   //     {
#   //       'time': '18:00',
#   //       'temperature': 18,
#   //       'pic_url': '/icons/weather.png'
#   //     },
#   //     {
#   //       'time': '21:00',
#   //       'temperature': 21,
#   //       'pic_url': '/icons/weather.png'
#   //     },
#   //     {
#   //       'time': '24:00',
#   //       'temperature': 24,
#   //       'pic_url': '/icons/weather.png'
#   //     }
#   //   ]
#   // }