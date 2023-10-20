import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtCore import Qt


class CountryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Country App')
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()

        self.combo_country = QComboBox(self)
        self.combo_country.currentIndexChanged.connect(self.country_selection_change)
        self.layout.addWidget(self.combo_country)

        self.combo_city = QComboBox(self)
        self.layout.addWidget(self.combo_city)

        self.show_button = QPushButton('Show Weather', self)
        self.show_button.clicked.connect(self.show_weather)
        self.layout.addWidget(self.show_button)

        self.data = None
        self.selected_city = None
        self.make_request()

        self.fetch_data()
        self.setLayout(self.layout)

    def make_request(self):
        url = 'https://countriesnow.space/api/v0.1/countries'
        response = requests.get(url)
        self.data = response.json()

    def fetch_data(self):
        for country in self.data['data']:
            self.combo_country.addItem(country['country'])

    def country_selection_change(self, index):
        self.combo_city.clear()
        country_index = self.combo_country.currentIndex()
        for city in self.data['data'][country_index]['cities']:
            self.combo_city.addItem(city)

    def show_weather(self):
        self.selected_city = self.combo_city.currentText()
        self.close()

    def get_city(self):
        return self.selected_city
