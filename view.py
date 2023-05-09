# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labal_TV_Remote = QtWidgets.QLabel(parent=self.centralwidget)
        self.labal_TV_Remote.setGeometry(QtCore.QRect(250, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labal_TV_Remote.setFont(font)
        self.labal_TV_Remote.setObjectName("labal_TV_Remote")
        self.power_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.power_button.setGeometry(QtCore.QRect(40, 20, 60, 60))
        self.power_button.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.power_button.setFont(font)
        self.power_button.setStyleSheet("")
        self.power_button.setObjectName("power_button")
        self.mute_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mute_button.setGeometry(QtCore.QRect(500, 20, 60, 60))
        self.mute_button.setMaximumSize(QtCore.QSize(60, 60))
        self.mute_button.setObjectName("mute_button")
        self.label_Channel = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_Channel.setGeometry(QtCore.QRect(30, 380, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_Channel.setFont(font)
        self.label_Channel.setObjectName("label_Channel")
        self.channel_upbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_upbutton.setGeometry(QtCore.QRect(150, 330, 31, 61))
        self.channel_upbutton.setMaximumSize(QtCore.QSize(31, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.channel_upbutton.setFont(font)
        self.channel_upbutton.setObjectName("channel_upbutton")
        self.channel_downbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_downbutton.setGeometry(QtCore.QRect(150, 420, 31, 61))
        self.channel_downbutton.setMaximumSize(QtCore.QSize(31, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.channel_downbutton.setFont(font)
        self.channel_downbutton.setObjectName("channel_downbutton")
        self.label_Volume = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_Volume.setGeometry(QtCore.QRect(320, 430, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_Volume.setFont(font)
        self.label_Volume.setObjectName("label_Volume")
        self.vol_upbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vol_upbutton.setGeometry(QtCore.QRect(490, 330, 31, 61))
        self.vol_upbutton.setMaximumSize(QtCore.QSize(31, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.vol_upbutton.setFont(font)
        self.vol_upbutton.setObjectName("vol_upbutton")
        self.vol_downbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vol_downbutton.setGeometry(QtCore.QRect(490, 410, 31, 61))
        self.vol_downbutton.setMaximumSize(QtCore.QSize(31, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.vol_downbutton.setFont(font)
        self.vol_downbutton.setObjectName("vol_downbutton")
        self.vol_amountbar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.vol_amountbar.setGeometry(QtCore.QRect(270, 390, 211, 21))
        self.vol_amountbar.setProperty("value", 24)
        self.vol_amountbar.setObjectName("vol_amountbar")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 90, 411, 211))
        self.textEdit.setObjectName("channel_view")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labal_TV_Remote.setText(_translate("MainWindow", "TV Remote"))
        self.power_button.setText(_translate("MainWindow", "Power"))
        self.mute_button.setText(_translate("MainWindow", "Mute"))
        self.label_Channel.setText(_translate("MainWindow", "Channel"))
        self.channel_upbutton.setText(_translate("MainWindow", "↑"))
        self.channel_downbutton.setText(_translate("MainWindow", "↓"))
        self.label_Volume.setText(_translate("MainWindow", "Volume"))
        self.vol_upbutton.setText(_translate("MainWindow", "↑"))
        self.vol_downbutton.setText(_translate("MainWindow", "↓"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
