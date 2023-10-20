from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests


class WeatherApp(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Weather Forecast")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.central_widget.setStyleSheet("background-color: lightblue;")

        self.display_weather(data)

    def display_weather(self, data):
        location = data['location']
        current = data['current']

        location_label = QLabel(f"{location['name']}, {location['country']}")
        location_label.setAlignment(Qt.AlignCenter)
        location_label.setStyleSheet("font: bold; font-size: 20px;")
        self.layout.addWidget(location_label)

        localtime_label = QLabel(f"Local Time: {location['localtime']}")
        localtime_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(localtime_label)

        temperature_label = QLabel(f"Temperature: {current['temperature']}°C")
        temperature_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(temperature_label)

        weather_description_label = QLabel(f"Weather: {current['weather_descriptions'][0]}")
        weather_description_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(weather_description_label)

        wind_label = QLabel(f"Wind: {current['wind_speed']} km/h, {current['wind_dir']}")
        wind_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(wind_label)

        humidity_label = QLabel(f"Humidity: {current['humidity']}%")
        humidity_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(humidity_label)

        uv_index_label = QLabel(f"UV Index: {current['uv_index']}")
        uv_index_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(uv_index_label)

        weather_icon_url = current['weather_icons'][0].replace("\\", "")
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(weather_icon_url).content)
        weather_icon_label = QLabel()
        weather_icon_label.setPixmap(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.layout.addWidget(weather_icon_label)
