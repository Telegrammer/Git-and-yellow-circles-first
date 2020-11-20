import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.is_cursor = False
        self.setGeometry(0,
                         0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(lambda: self.update())

    def paintEvent(self, event):
        if self.is_cursor:
            painter = QPainter()
            painter.begin(self)
            radius = randrange(0, 300)
            painter.setPen(QColor(255, 255, 0))
            painter.drawEllipse(self.frameGeometry().width() // 2 - 100,
                                self.frameGeometry().height() // 2 - 100,
                                radius, radius)
            painter.end()
        self.is_cursor = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
