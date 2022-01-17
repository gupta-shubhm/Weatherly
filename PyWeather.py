from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.dropshadowFrameLeft = QtWidgets.QFrame(self.centralwidget)
        self.dropshadowFrameLeft.setGeometry(QtCore.QRect(10, 35, 321, 401))
        self.dropshadowFrameLeft.setStyleSheet("QFrame{\n"
                                               "border-radius: 20px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.517, stop:0 rgba(11, 119, 148, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                               "\n"
                                               "}\n"
                                               "\n"
                                               "")
        self.dropshadowFrameLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropshadowFrameLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropshadowFrameLeft.setLineWidth(1)
        self.dropshadowFrameLeft.setObjectName("dropshadowFrameLeft")
        self.label_day = QtWidgets.QLabel(self.dropshadowFrameLeft)
        self.label_day.setGeometry(QtCore.QRect(20, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_day.setFont(font)
        self.label_day.setStyleSheet("QLabel{\n"
                                     "color:white;\n"
                                     "background-color:transparent}")
        self.label_day.setWordWrap(True)
        self.label_day.setObjectName("label_day")
        self.label_date = QtWidgets.QLabel(self.dropshadowFrameLeft)
        self.label_date.setGeometry(QtCore.QRect(20, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_date.setFont(font)
        self.label_date.setStyleSheet("QLabel{\n"
                                      "color:white;\n"
                                      "background-color:transparent}")
        self.label_date.setWordWrap(True)
        self.label_date.setObjectName("label_date")
        self.icon_location = QtWidgets.QPushButton(self.dropshadowFrameLeft)
        self.icon_location.setGeometry(QtCore.QRect(10, 280, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_location.sizePolicy().hasHeightForWidth())
        self.icon_location.setSizePolicy(sizePolicy)
        self.icon_location.setVisible(False)
        self.icon_location.setMaximumSize(QtCore.QSize(30, 30))
        self.icon_location.setStyleSheet("QPushButton {\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: transparent;\n"
                                         "}")
        self.icon_location.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-location-pin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_location.setIcon(icon)
        self.icon_location.setIconSize(QtCore.QSize(16, 16))
        self.icon_location.setObjectName("icon_location")
        self.label_location = QtWidgets.QLabel(self.dropshadowFrameLeft)
        self.label_location.setGeometry(QtCore.QRect(40, 277, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_location.setFont(font)
        self.label_location.setStyleSheet("QLabel{\n"
                                          "color:white;\n"
                                          "background-color:transparent}")
        self.label_location.setWordWrap(True)
        self.label_location.setObjectName("label_location")
        self.icon_current_weather = QtWidgets.QPushButton(self.dropshadowFrameLeft)
        self.icon_current_weather.setGeometry(QtCore.QRect(10, 90, 121, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_current_weather.sizePolicy().hasHeightForWidth())
        self.icon_current_weather.setSizePolicy(sizePolicy)
        self.icon_current_weather.setVisible(False)
        self.icon_current_weather.setMaximumSize(QtCore.QSize(300, 300))
        self.icon_current_weather.setStyleSheet("QPushButton {\n"
                                                "    border-radius: 5px;    \n"
                                                "    background-color: transparent;\n"
                                                "}")
        self.icon_current_weather.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/WeatherIcons/icon_partial_cloudy_day.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.icon_current_weather.setIcon(icon1)
        self.icon_current_weather.setIconSize(QtCore.QSize(64, 64))
        self.icon_current_weather.setObjectName("icon_current_weather")
        self.label_temperature = QtWidgets.QLabel(self.dropshadowFrameLeft)
        self.label_temperature.setGeometry(QtCore.QRect(10, 190, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_temperature.setFont(font)
        self.label_temperature.setStyleSheet("QLabel{\n"
                                             "color:white;\n"
                                             "background-color:transparent}")
        self.label_temperature.setWordWrap(True)
        self.label_temperature.setObjectName("label_temperature")
        self.label_sky_text = QtWidgets.QLabel(self.dropshadowFrameLeft)
        self.label_sky_text.setGeometry(QtCore.QRect(20, 330, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_sky_text.setFont(font)
        self.label_sky_text.setStyleSheet("QLabel{\n"
                                          "color:white;\n"
                                          "background-color:transparent}")
        self.label_sky_text.setWordWrap(True)
        self.label_sky_text.setObjectName("label_sky_text")
        self.label_temp_low_high = QtWidgets.QLabel(self.dropshadowFrameLeft)
        self.label_temp_low_high.setGeometry(QtCore.QRect(20, 350, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp_low_high.setFont(font)
        self.label_temp_low_high.setStyleSheet("QLabel{\n"
                                               "color:white;\n"
                                               "background-color:transparent}")
        self.label_temp_low_high.setWordWrap(True)
        self.label_temp_low_high.setObjectName("label_temp_low_high")
        self.dropshadowFrame_Right = QtWidgets.QFrame(self.centralwidget)
        self.dropshadowFrame_Right.setGeometry(QtCore.QRect(290, 10, 351, 455))
        self.dropshadowFrame_Right.setStyleSheet("background-color: rgb(32,39,49);\n"
                                                 "border-radius: 10px;")
        self.dropshadowFrame_Right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropshadowFrame_Right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropshadowFrame_Right.setObjectName("dropshadowFrame_Right")
        self.pushButton_getweather = QtWidgets.QPushButton(self.dropshadowFrame_Right)
        self.pushButton_getweather.setGeometry(QtCore.QRect(20, 388, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_getweather.sizePolicy().hasHeightForWidth())
        self.pushButton_getweather.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_getweather.setFont(font)
        self.pushButton_getweather.setStyleSheet("QPushButton {\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0.00497512, y1:0.517, x2:1, y2:0.528, stop:0 rgba(18, 95, 136, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                 "    color:black;\n"
                                                 "    border-radius: 5px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "background-color: qlineargradient(spread:pad, x1:0.00497512, y1:0.517, x2:1, y2:0.528, stop:0 rgba(18, 95, 136, 255), stop:1 rgba(255, 255, 255, 255));    border: 2px solid rgb(17, 94, 134);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {    \n"
                                                 "    background-color: rgba(0, 170, 255, 100);\n"
                                                 "    border: 2px solid rgb(17, 94, 134);\n"
                                                 "color:white\n"
                                                 "}")
        self.pushButton_getweather.setObjectName("pushButton_getweather")
        self.frame_params = QtWidgets.QFrame(self.dropshadowFrame_Right)
        self.frame_params.setGeometry(QtCore.QRect(10, 200, 331, 161))
        self.frame_params.setStyleSheet("border-radius: 5px;\n"
                                        "background-color: rgb(31, 31, 31);\n"
                                        "background-color: rgb(26,32,38);")
        self.frame_params.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_params.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_params.setLineWidth(5)
        self.frame_params.setObjectName("frame_params")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_params)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.weatherframe_1 = QtWidgets.QFrame(self.frame_params)
        self.weatherframe_1.setStyleSheet("QFrame{\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(58, 58, 58);\n"
                                          "border-radius: 5px;\n"
                                          "border: 2px solid rgb(245, 245 ,245);\n"
                                          "}")
        self.weatherframe_1.setObjectName("weatherframe_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.weatherframe_1)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.weather_icon_1 = QtWidgets.QPushButton(self.weatherframe_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_icon_1.sizePolicy().hasHeightForWidth())
        self.weather_icon_1.setSizePolicy(sizePolicy)
        self.weather_icon_1.setVisible(False)
        self.weather_icon_1.setMaximumSize(QtCore.QSize(100, 60))
        self.weather_icon_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.weather_icon_1.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 5px;    \n"
                                          "    background-color: transparent;\n"
                                          "}")
        self.weather_icon_1.setText("")
        self.weather_icon_1.setIcon(icon1)
        self.weather_icon_1.setIconSize(QtCore.QSize(48, 48))
        self.weather_icon_1.setObjectName("weather_icon_1")
        self.verticalLayout.addWidget(self.weather_icon_1)
        self.day_1 = QtWidgets.QLabel(self.weatherframe_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.day_1.setFont(font)
        self.day_1.setStyleSheet("QLabel{\n"
                                 "color: rgb(58, 58, 58);\n"
                                 "border-radius:1px;\n"
                                 "border: 1px transoarent;\n"
                                 "}")
        self.day_1.setAlignment(QtCore.Qt.AlignCenter)
        self.day_1.setWordWrap(True)
        self.day_1.setObjectName("day_1")
        self.verticalLayout.addWidget(self.day_1)
        self.weather_5 = QtWidgets.QLabel(self.weatherframe_1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.weather_5.setFont(font)
        self.weather_5.setStyleSheet("QLabel{\n"
                                     "color: rgb(58, 58, 58);\n"
                                     "border-radius:10px;\n"
                                     "border: 1px transoarent;\n"
                                     "}")
        self.weather_5.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_5.setWordWrap(True)
        self.weather_5.setObjectName("weather_5")
        self.verticalLayout.addWidget(self.weather_5)
        self.weather_1 = QtWidgets.QLabel(self.weatherframe_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weather_1.setFont(font)
        self.weather_1.setStyleSheet("QLabel{\n"
                                     "color: rgb(58, 58, 58);\n"
                                     "border-radius:10px;\n"
                                     "border: 1px transoarent;\n"
                                     "}")
        self.weather_1.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_1.setWordWrap(True)
        self.weather_1.setObjectName("weather_1")
        self.verticalLayout.addWidget(self.weather_1)
        self.horizontalLayout.addWidget(self.weatherframe_1)
        self.weatherframe_2 = QtWidgets.QFrame(self.frame_params)
        self.weatherframe_2.setStyleSheet("QFrame{\n"
                                          "background-color: transparent;\n"
                                          "color: white;\n"
                                          "}\n"
                                          "QLabel{\n"
                                          "background-color:transparent;\n"
                                          "color:white;\n"
                                          "}")
        self.weatherframe_2.setObjectName("weatherframe_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.weatherframe_2)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.weather_icon_2 = QtWidgets.QPushButton(self.weatherframe_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_icon_2.sizePolicy().hasHeightForWidth())
        self.weather_icon_2.setSizePolicy(sizePolicy)
        self.weather_icon_2.setVisible(False)
        self.weather_icon_2.setMaximumSize(QtCore.QSize(100, 60))
        self.weather_icon_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.weather_icon_2.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 5px;    \n"
                                          "    background-color: transparent;\n"
                                          "}")
        self.weather_icon_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/WeatherIcons/icon_rain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weather_icon_2.setIcon(icon2)
        self.weather_icon_2.setIconSize(QtCore.QSize(48, 48))
        self.weather_icon_2.setObjectName("weather_icon_2")
        self.verticalLayout_2.addWidget(self.weather_icon_2)
        self.day_2 = QtWidgets.QLabel(self.weatherframe_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.day_2.setFont(font)
        self.day_2.setStyleSheet("")
        self.day_2.setAlignment(QtCore.Qt.AlignCenter)
        self.day_2.setWordWrap(True)
        self.day_2.setObjectName("day_2")
        self.verticalLayout_2.addWidget(self.day_2)
        self.weather_6 = QtWidgets.QLabel(self.weatherframe_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.weather_6.setFont(font)
        self.weather_6.setStyleSheet("")
        self.weather_6.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_6.setWordWrap(True)
        self.weather_6.setObjectName("weather_6")
        self.verticalLayout_2.addWidget(self.weather_6)
        self.weather_2 = QtWidgets.QLabel(self.weatherframe_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weather_2.setFont(font)
        self.weather_2.setStyleSheet("")
        self.weather_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_2.setWordWrap(True)
        self.weather_2.setObjectName("weather_2")
        self.verticalLayout_2.addWidget(self.weather_2)
        self.horizontalLayout.addWidget(self.weatherframe_2)
        self.weatherframe_3 = QtWidgets.QFrame(self.frame_params)
        self.weatherframe_3.setStyleSheet("QFrame{\n"
                                          "background-color: transparent;\n"
                                          "color: white;\n"
                                          "}")
        self.weatherframe_3.setObjectName("weatherframe_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.weatherframe_3)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.weather_icon_3 = QtWidgets.QPushButton(self.weatherframe_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_icon_3.sizePolicy().hasHeightForWidth())
        self.weather_icon_3.setSizePolicy(sizePolicy)
        self.weather_icon_3.setVisible(False)
        self.weather_icon_3.setMaximumSize(QtCore.QSize(100, 60))
        self.weather_icon_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.weather_icon_3.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 5px;    \n"
                                          "    background-color: transparent;\n"
                                          "}")
        self.weather_icon_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/WeatherIcons/icon_thunderstorm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weather_icon_3.setIcon(icon3)
        self.weather_icon_3.setIconSize(QtCore.QSize(48, 48))
        self.weather_icon_3.setObjectName("weather_icon_3")
        self.verticalLayout_5.addWidget(self.weather_icon_3)
        self.day_3 = QtWidgets.QLabel(self.weatherframe_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.day_3.setFont(font)
        self.day_3.setStyleSheet("QLabel{\n"
                                 "background-color:transparent;\n"
                                 "color:white;\n"
                                 "}")
        self.day_3.setAlignment(QtCore.Qt.AlignCenter)
        self.day_3.setWordWrap(True)
        self.day_3.setObjectName("day_3")
        self.verticalLayout_5.addWidget(self.day_3)
        self.weather_7 = QtWidgets.QLabel(self.weatherframe_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.weather_7.setFont(font)
        self.weather_7.setStyleSheet("")
        self.weather_7.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_7.setWordWrap(True)
        self.weather_7.setObjectName("weather_7")
        self.verticalLayout_5.addWidget(self.weather_7)
        self.weather_3 = QtWidgets.QLabel(self.weatherframe_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weather_3.setFont(font)
        self.weather_3.setStyleSheet("QLabel{\n"
                                     "background-color:transparent;\n"
                                     "color:white;\n"
                                     "}")
        self.weather_3.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_3.setWordWrap(True)
        self.weather_3.setObjectName("weather_3")
        self.verticalLayout_5.addWidget(self.weather_3)
        self.horizontalLayout.addWidget(self.weatherframe_3)
        self.weatherframe_4 = QtWidgets.QFrame(self.frame_params)
        self.weatherframe_4.setStyleSheet("QFrame{\n"
                                          "background-color: transparent;\n"
                                          "color: white;\n"
                                          "}\n"
                                          "QLabel{\n"
                                          "background-color:transparent;\n"
                                          "color:white;\n"
                                          "}")
        self.weatherframe_4.setObjectName("weatherframe_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.weatherframe_4)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.weather_icon_4 = QtWidgets.QPushButton(self.weatherframe_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_icon_4.sizePolicy().hasHeightForWidth())
        self.weather_icon_4.setSizePolicy(sizePolicy)
        self.weather_icon_4.setVisible(False)
        self.weather_icon_4.setMaximumSize(QtCore.QSize(100, 60))
        self.weather_icon_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.weather_icon_4.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 5px;    \n"
                                          "    background-color: transparent;\n"
                                          "}")
        self.weather_icon_4.setText("")
        self.weather_icon_4.setIcon(icon1)
        self.weather_icon_4.setIconSize(QtCore.QSize(48, 48))
        self.weather_icon_4.setObjectName("weather_icon_4")
        self.verticalLayout_4.addWidget(self.weather_icon_4)
        self.day_4 = QtWidgets.QLabel(self.weatherframe_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.day_4.setFont(font)
        self.day_4.setStyleSheet("")
        self.day_4.setAlignment(QtCore.Qt.AlignCenter)
        self.day_4.setWordWrap(True)
        self.day_4.setObjectName("day_4")
        self.verticalLayout_4.addWidget(self.day_4)
        self.weather_8 = QtWidgets.QLabel(self.weatherframe_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.weather_8.setFont(font)
        self.weather_8.setStyleSheet("")
        self.weather_8.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_8.setWordWrap(True)
        self.weather_8.setObjectName("weather_8")
        self.verticalLayout_4.addWidget(self.weather_8)
        self.weather_4 = QtWidgets.QLabel(self.weatherframe_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weather_4.setFont(font)
        self.weather_4.setStyleSheet("")
        self.weather_4.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_4.setWordWrap(True)
        self.weather_4.setObjectName("weather_4")
        self.verticalLayout_4.addWidget(self.weather_4)
        self.horizontalLayout.addWidget(self.weatherframe_4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.dropshadowFrame_Right)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(25, 438, 300, 1))
        self.progressBar.setMinimumSize(QtCore.QSize(4, 1))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 1))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(1)
        font.setItalic(True)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    min-height: 1px;\n"
                                       "    max-height: 1px;\n"
                                       "    border-radius: 54px;    \n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: rgb(210, 210, 210);\n"
                                       "    border-radius: 2px;\n"
                                       "}")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.window_close_button = QtWidgets.QPushButton(self.dropshadowFrame_Right)
        self.window_close_button.setGeometry(QtCore.QRect(310, 10, 31, 28))
        self.window_close_button.setStyleSheet("QPushButton {\n"
                                               "    background-color: transparent;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "    \n"
                                               "background-color: transparent;\n"
                                               "}\n"
                                               "QPushButton:pressed {    \n"
                                               "background-color: rgb(65, 65, 65);\n"
                                               "}")
        self.window_close_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/24x24/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window_close_button.setIcon(icon4)
        self.window_close_button.setIconSize(QtCore.QSize(16, 16))
        self.window_close_button.setObjectName("window_close_button")
        self.button_change_city = QtWidgets.QPushButton(self.dropshadowFrame_Right)
        self.button_change_city.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.button_change_city.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_change_city.setFont(font)
        self.button_change_city.setStyleSheet("QPushButton {\n"
                                              "    border-radius: 5px;\n"
                                              "    background-color: rgb(26,32,38);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(35, 42, 55);\n"
                                              "}\n"
                                              "QPushButton:pressed {    \n"
                                              "    background-color: rgb(30, 35, 42);\n"
                                              "}\n"
                                              "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/24x24/cil-location-pin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_change_city.setIcon(icon5)
        self.button_change_city.setIconSize(QtCore.QSize(16, 16))
        self.button_change_city.setObjectName("button_change_city")
        self.widget = QtWidgets.QWidget(self.dropshadowFrame_Right)
        self.widget.setGeometry(QtCore.QRect(10, 50, 331, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, -1)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.icon_location_4 = QtWidgets.QPushButton(self.widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_location_4.sizePolicy().hasHeightForWidth())
        self.icon_location_4.setSizePolicy(sizePolicy)
        self.icon_location_4.setMaximumSize(QtCore.QSize(30, 30))
        self.icon_location_4.setStyleSheet("QPushButton {\n"
                                           "    border-radius: 5px;    \n"
                                           "    background-color: transparent;\n"
                                           "}")
        self.icon_location_4.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/24x24/icon_rain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_location_4.setIcon(icon6)
        self.icon_location_4.setIconSize(QtCore.QSize(24, 24))
        self.icon_location_4.setObjectName("icon_location_4")
        self.horizontalLayout_3.addWidget(self.icon_location_4)
        self.label_uc_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uc_2.setFont(font)
        self.label_uc_2.setStyleSheet("background-color:transparent")
        self.label_uc_2.setObjectName("label_uc_2")
        self.horizontalLayout_3.addWidget(self.label_uc_2)
        self.label_uc = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uc.setFont(font)
        self.label_uc.setStyleSheet("background-color:transparent")
        self.label_uc.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_uc.setObjectName("label_uc")
        self.horizontalLayout_3.addWidget(self.label_uc)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, -1)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icon_location_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_location_3.sizePolicy().hasHeightForWidth())
        self.icon_location_3.setSizePolicy(sizePolicy)
        self.icon_location_3.setMaximumSize(QtCore.QSize(30, 30))
        self.icon_location_3.setStyleSheet("QPushButton {\n"
                                           "    border-radius: 5px;    \n"
                                           "    background-color: transparent;\n"
                                           "}")
        self.icon_location_3.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/24x24/icon_wind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_location_3.setIcon(icon7)
        self.icon_location_3.setIconSize(QtCore.QSize(24, 24))
        self.icon_location_3.setObjectName("icon_location_3")
        self.horizontalLayout_4.addWidget(self.icon_location_3)
        self.label_uc_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uc_3.setFont(font)
        self.label_uc_3.setStyleSheet("background-color:transparent")
        self.label_uc_3.setObjectName("label_uc_3")
        self.horizontalLayout_4.addWidget(self.label_uc_3)
        self.label_uc_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uc_4.setFont(font)
        self.label_uc_4.setStyleSheet("background-color:transparent")
        self.label_uc_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_uc_4.setObjectName("label_uc_4")
        self.horizontalLayout_4.addWidget(self.label_uc_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, -1)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.icon_location_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_location_2.sizePolicy().hasHeightForWidth())
        self.icon_location_2.setSizePolicy(sizePolicy)
        self.icon_location_2.setMaximumSize(QtCore.QSize(30, 30))
        self.icon_location_2.setStyleSheet("QPushButton {\n"
                                           "    border-radius: 5px;    \n"
                                           "    background-color: transparent;\n"
                                           "}")
        self.icon_location_2.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/24x24/humidity.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_location_2.setIcon(icon8)
        self.icon_location_2.setIconSize(QtCore.QSize(24, 24))
        self.icon_location_2.setObjectName("icon_location_2")
        self.horizontalLayout_6.addWidget(self.icon_location_2)
        self.label_uc_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uc_7.setFont(font)
        self.label_uc_7.setStyleSheet("background-color:transparent")
        self.label_uc_7.setObjectName("label_uc_7")
        self.horizontalLayout_6.addWidget(self.label_uc_7)
        self.label_uc_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uc_8.setFont(font)
        self.label_uc_8.setStyleSheet("background-color:transparent")
        self.label_uc_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_uc_8.setObjectName("label_uc_8")
        self.horizontalLayout_6.addWidget(self.label_uc_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_day.setText(_translate("MainWindow", ""))
        self.label_date.setText(_translate("MainWindow", ""))
        self.label_location.setText(_translate("MainWindow", ""))
        self.label_temperature.setText(_translate("MainWindow", ""))
        self.label_sky_text.setText(_translate("MainWindow", ""))
        self.label_temp_low_high.setText(_translate("MainWindow", ""))
        self.pushButton_getweather.setText(_translate("MainWindow", "Get Weather Info"))
        self.day_1.setText(_translate("MainWindow", ""))
        self.weather_5.setText(_translate("MainWindow", ""))
        self.weather_1.setText(_translate("MainWindow", ""))
        self.day_2.setText(_translate("MainWindow", ""))
        self.weather_6.setText(_translate("MainWindow", ""))
        self.weather_2.setText(_translate("MainWindow", ""))
        self.day_3.setText(_translate("MainWindow", ""))
        self.weather_7.setText(_translate("MainWindow", ""))
        self.weather_3.setText(_translate("MainWindow", ""))
        self.day_4.setText(_translate("MainWindow", ""))
        self.weather_8.setText(_translate("MainWindow", ""))
        self.weather_4.setText(_translate("MainWindow", ""))
        self.button_change_city.setText(_translate("MainWindow", " Change City"))
        self.label_uc_2.setText(_translate("MainWindow", "Precipitation"))
        self.label_uc.setText(_translate("MainWindow", "-"))
        self.label_uc_3.setText(_translate("MainWindow", "Wind Speed"))
        self.label_uc_4.setText(_translate("MainWindow", "-"))
        self.label_uc_7.setText(_translate("MainWindow", "Humidity"))
        self.label_uc_8.setText(_translate("MainWindow", "-"))


import files_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
