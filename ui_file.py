from PyQt5.QtWidgets import QPushButton


class Ui_MainWindow(object):
    def setupUi(self):
        self.pushButton = QPushButton('Button', self)
        self.pushButton.setGeometry(100, 100, 120, 60)
