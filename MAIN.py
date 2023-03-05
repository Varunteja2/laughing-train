import requests
import json
from datetime import datetime, timedelta
from tkinter import Tk, Label, PhotoImage, messagebox

class WeatherApp:
    def _init_(self, api_key):
        self.api_key = api_key
        self.city name = None
        self.weather_description = None
        self.forecast_data = None

    
    def get_current_weather_data(self):
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self.api_key}"
        response = requests.get(weather_url)
        if response.status_code !=200:
            