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
        
