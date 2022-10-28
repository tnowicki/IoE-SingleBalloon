import requests, json
from BalloonData import *

API_KEY = '316899cae2024ff475d3460be04b8c1c'

def fromOpenWeather(balloonData):    
    lat = balloonData[LATITUDE]
    lon = balloonData[LONGITUDE]
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    balloonData[TEMPERATURE] = data['main']['temp'] - 273.15
    balloonData[HUMIDITY] = data['main']['humidity']
    balloonData[WIND_SPEED] = data['wind']['speed']
    balloonData[WIND_DIRECTION] = data['wind']['deg']
    return balloonData