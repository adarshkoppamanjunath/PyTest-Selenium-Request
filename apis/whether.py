import requests

class Weather:
    base_url="http://api.openweathermap.org/data/2.5/weather"
    weather_filter= "?q=<city>&appid=8c2ee1d545d44be778ba214fb008c22c"
    def __init__(self,util_obj):
        self.util_obj=util_obj
    def execute_weather_api(self,city):
        weather_filter=self.weather_filter.replace("<city>",city)
        weather_filter=self.base_url+weather_filter
        print(weather_filter)
        response = requests.request("GET", url=weather_filter)
        return response