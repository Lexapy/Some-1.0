# -*- coding: utf-8 -*-
import sys
from UI import Ui_Yellow_circles
from random import randint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Yellow_circles()
        self.ui.setupUi(self)
        self.do_paint = False
        self.ui.push.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, e):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        size = [self.width(), self.height()]
        for i in range(10):
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setBrush(color)
            qp.setPen(color)
            r = randint(1, min(size) - 1) // 4
            center = QPoint(randint(1 + r, size[0] - r),
                            randint(1 + r, size[1] - 100 - r))
            qp.drawEllipse(center, int(r), int(r))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Widget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())