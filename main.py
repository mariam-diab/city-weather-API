import sys
import requests
from PyQt5.QtWidgets import QApplication
from country_app import CountryApp
from weather_app import WeatherApp


API_ACCESS_KEY = "821bf71e70a00ce93f16c6f885919f4e"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    country_window = CountryApp()
    country_window.show()
    app.exec_()
    city = country_window.get_city()
    if city:
        url = f"http://api.weatherstack.com/current?access_key={API_ACCESS_KEY}&query={city}"
        response = requests.get(url)
        weather_data = response.json()
        weather_window = WeatherApp(weather_data)
        weather_window.show()
        sys.exit(app.exec_())
