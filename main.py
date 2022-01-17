import asyncio
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import python_weather
from PyQt5.QtCore import (Qt, QSize)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyWeather import Ui_MainWindow
from Weather import getWeather
from select_city_dialog import Ui_Dialog

path = "resources/config/weather.json"


def update_username_json(json_field, value, filename=path):
    with open(filename, 'w') as file:
        json.dump({json_field: value}, file)


class SelectCityDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_ok.clicked.connect(self.setCity)
        self.ui.button_closedialog.clicked.connect(self.close)

        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_top_btns.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def setCity(self):
        update_username_json("city_name", self.ui.lineEdit_passLength.text())
        self.close()


def weatherCondition(skyText):
    iconPath = None
    if "sunny" in skyText:
        iconPath = "icons/WeatherIcons/icon_clear_day.png"

    if "rain" in skyText:
        iconPath = "icons/WeatherIcons/icon_rain.png"

    if "cloudy" in skyText:
        if "mostly" in skyText or "partly" in skyText:
            iconPath = "icons/WeatherIcons/icon_partial_cloudy_day.png"
        if skyText == "cloudy":
            iconPath = "icons/WeatherIcons/icon_cloudy.png"

    if skyText == "snow":
        iconPath = "icons/WeatherIcons/icon_snow.png"

    if "fog" in skyText or "smoke" in skyText:
        iconPath = "icons/WeatherIcons/icon_fog.png"

    return iconPath


def changeIcon(skyText, button: QPushButton, iconPosition):
    iconPath = weatherCondition(str(skyText).lower())
    icon = QIcon()
    icon.addPixmap(QPixmap(str(iconPath)), QIcon.Normal, QIcon.Off)
    button.setIcon(icon)
    if iconPosition == "left":
        button.setIconSize(QSize(64, 64))
    else:
        button.setIconSize(QSize(48, 48))


def readJson():
    with open("{}".format(os.path.join(os.getcwd(), "Resources/config/weather.json")), "r") as f:
        json_ = json.load(f)
    return json_["city_name"]


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.dialog = SelectCityDialog()
        self.ui.setupUi(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropshadowFrameLeft.setGraphicsEffect(self.shadow)
        self.ui.dropshadowFrame_Right.setGraphicsEffect(self.shadow)
        self.progress(False)
        self.json_config = None
        self.initViews(readJson())

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.dropshadowFrame_Right.mouseMoveEvent = moveWindow
        self.ui.window_close_button.clicked.connect(self.close)
        self.ui.pushButton_getweather.clicked.connect(self.buttonHandler)
        self.ui.button_change_city.clicked.connect(lambda: self.dialog.show())

    def executor_with_gui(self, obj, *argv):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(obj, *argv)
            while future.running():
                time.sleep(0.05)
                QApplication.processEvents()
            return_value = future.result()
            return return_value

    def initViews(self, city_name):
        self.progress(True)
        loop = asyncio.get_event_loop()
        QApplication.processEvents()
        currentWeather, weatherObject = self.executor_with_gui(loop.run_until_complete,
                                                               getWeather(city_name, python_weather.METRIC))

        self.ui.label_day.setText(currentWeather["day"])
        self.ui.label_date.setText(currentWeather["date"])
        self.ui.label_temperature.setText(currentWeather["temperature"] + "° C")
        self.ui.label_location.setText(currentWeather["location"])
        self.ui.label_sky_text.setText(currentWeather["sky_text"])
        self.ui.label_temp_low_high.setText(
            f"{currentWeather['temp_high']}° / {currentWeather['temp_low']}° Feels like {currentWeather['feels_like']}°")
        self.ui.label_uc.setText(currentWeather["precip"] + " %")
        self.ui.label_uc_4.setText(currentWeather["wind_speed"] + " km/h")
        self.ui.label_uc_8.setText(currentWeather["humidity"] + " %")
        self.ui.icon_location.setVisible(True)
        self.ui.icon_current_weather.setVisible(True)

        changeIcon(currentWeather["sky_text"], self.ui.icon_current_weather, "left")

        for forecast in range(len(weatherObject)):
            if forecast == 0:
                changeIcon(weatherObject[forecast][4], self.ui.weather_icon_1, "right")
                self.ui.weather_icon_1.setVisible(True)
                self.ui.day_1.setText(weatherObject[forecast][0])
                self.ui.weather_5.setText(f"{weatherObject[forecast][2]}° / {weatherObject[forecast][3]}°")
                self.ui.weather_1.setText(weatherObject[forecast][1] + "° C")
            if forecast == 1:
                changeIcon(weatherObject[forecast][4], self.ui.weather_icon_2, "right")
                self.ui.weather_icon_2.setVisible(True)
                self.ui.day_2.setText(weatherObject[forecast][0])
                self.ui.weather_6.setText(f"{weatherObject[forecast][2]}° / {weatherObject[forecast][3]}°")
                self.ui.weather_2.setText(weatherObject[forecast][1] + "° C")
            if forecast == 2:
                changeIcon(weatherObject[forecast][4], self.ui.weather_icon_3, "right")
                self.ui.weather_icon_3.setVisible(True)
                self.ui.day_3.setText(weatherObject[forecast][0])
                self.ui.weather_7.setText(f"{weatherObject[forecast][2]}° / {weatherObject[forecast][3]}°")
                self.ui.weather_3.setText(weatherObject[forecast][1] + "° C")
            if forecast == 3:
                changeIcon(weatherObject[forecast][4], self.ui.weather_icon_4, "right")
                self.ui.weather_icon_4.setVisible(True)
                self.ui.day_4.setText(weatherObject[forecast][0])
                self.ui.weather_8.setText(f"{weatherObject[forecast][2]}° / {weatherObject[forecast][3]}°")
                self.ui.weather_4.setText(weatherObject[forecast][1] + "° C")
        self.progress(False)

    def getLastData(self):
        with open("{}".format(os.path.join(os.getcwd(), "resources/config/weather.json")), "r") as f:
            self.json_config = json.load(f)
        self.initViews(self.json_config["city_name"])

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def progress(self, on=True):
        if on:
            self.ui.progressBar.show()
        else:
            self.ui.progressBar.hide()

    def buttonHandler(self):
        city_name = readJson()
        self.initViews(city_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
