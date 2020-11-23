from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from ui_file import Ui_MainWindow
import sys
from random import randint


class MainWidget(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.clicked = False
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.clicked = True
        self.repaint()

    def paintEvent(self, event):
        if self.clicked:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.clicked = False

    def draw(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(0, min(self.width(), self.height()))
        x, y = randint(0, self.width() - r), randint(0, self.height() - r)
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MainWidget()
    wid.show()
    sys.exit(app.exec())
