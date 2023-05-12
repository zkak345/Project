from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 0
    MAX_CHANNEL = 4
    Nonmuted = 0
    Channels = {0: 'National Geographic', 1: 'Cartoon Network', 2: 'HBO', 3: 'ESPN'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.power_button.clicked.connect(lambda: self.power())
        self.mute_button.clicked.connect(lambda: self.mute())
        self.channel_upbutton.clicked.connect(lambda: self.channel_up())
        self.channel_downbutton.clicked.connect(lambda: self.channel_down())
        self.vol_upbutton.clicked.connect(lambda: self.volume_up())
        self.vol_downbutton.clicked.connect(lambda: self.volume_down())
        self.__status = False
        self.__muted = False
        self.__volume = Controller.MIN_VOLUME
        self.__channel = Controller.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status
        if self.__status:
            channel = self.__channel
            self.textEdit.setText(Controller.Channels[channel])
        else:
            self.textEdit.setText('')
    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                Controller.Nonmuted = self.vol_amountbar.value()
                self.vol_amountbar.setValue(0)

    def channel_up(self):
        if self.__status:
            if self.__channel == 3:
                self.__channel = 0
                channel = self.__channel
                self.textEdit.setText(Controller.Channels[channel])
            else:
                self.__channel += 1
                channel = self.__channel
                self.textEdit.setText(Controller.Channels[channel])

    def channel_down(self):
        if self.__status:
            if self.__channel == Controller.MIN_CHANNEL:
                self.__channel = 3
                channel = self.__channel
                self.textEdit.setText(Controller.Channels[channel])
            else:
                self.__channel -= 1
                channel = self.__channel
                self.textEdit.setText(Controller.Channels[channel])

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
                self.vol_amountbar.setValue(Controller.Nonmuted)
            value = self.vol_amountbar.value()
            if value < Controller.MAX_VOLUME:
                self.vol_amountbar.setValue(value + 1)

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
                self.vol_amountbar.setValue(Controller.Nonmuted)
            value = self.vol_amountbar.value()
            if value > Controller.MIN_VOLUME:
                self.vol_amountbar.setValue(value - 1)









