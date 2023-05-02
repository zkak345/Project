from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
class Controller(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

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
            self.status_text.setText('On')
        else:
            self.status_text.setText('Off')
            self.volume_text.setText('')
            self.mute_text.setText('')
            self.channel_text.setText('')
    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.mute_text.setText('Muted')
                self.volume_text.setText('0')
            else:
                self.mute_text.setText('Not Muted')

    def channel_up(self):
        if self.__status:
            if self.__channel == Controller.MAX_CHANNEL:
                self.__channel = Controller.MIN_CHANNEL
            else:
                self.__channel += 1
                channel = str(self.__channel)
                self.channel_text.setText(channel)

    def channel_down(self):
        if self.__status:
            if self.__channel == Controller.MIN_CHANNEL:
                self.__channel = Controller.MAX_CHANNEL
            else:
                self.__channel -= 1
                channel = str(self.__channel)
                self.channel_text.setText(channel)

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
            if self.__volume < Controller.MAX_VOLUME:
                self.__volume += 1
                volume = str(self.__volume)
                self.volume_text.setText(volume)

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
            if self.__volume > Controller.MIN_VOLUME:
                self.__volume -= 1
                volume = str(self.__volume)
                self.volume_text.setText(volume)

    def output(self):
        if self.__status:
            self.status_text.setText('On')
            if self.__muted:
                self.mute_text.setText('Muted')
                self.volume_text.setText('0')
            else:
                self.volume_text.setText(self.__volume)
                self.mute_text.setText('Not Muted')
            self.channel_text.setText(self.__channel)
        else:
            self.status_text.setText('Off')
            self.volume_text.setText('')
            self.mute_text.setText('')
            self.channel_text.setText('')







