import pytest
import json
from apis.whether import Weather



@pytest.mark.usefixtures("setup")
class Test_02_API:
    def test_api(self):
        weather_obj = Weather(self.util_obj)
        response = weather_obj.execute_weather_api("Toronto")
        data=json.loads(response.text)
        temp=self.util_obj.convert_temp_from_k_to_c(data["main"]["temp"])
        print("API response code: %s"%(response.status_code))
        print("Toroto temperature now: %s"%(temp))
        assert response.status_code==200
    