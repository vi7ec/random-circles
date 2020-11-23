from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
import random


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.repaint())

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(0, 255, 255))
        x, y = random.randint(0, self.x()), random.randint(0, self.y())
        r = random.randint(0, self.x())
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MainWidget()
    wid.show()
    sys.exit(app.exec())
