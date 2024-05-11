# -*- coding: utf-8 -*-🚀
import sys
from PySide6.QtWidgets import QApplication, QWidget
from util.Ui_rtsp_dialog import Ui_Form


class RTSP_Window(QWidget, Ui_Form):
    def __init__(self):
        super(RTSP_Window, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RTSP_Window()
    window.show()
    sys.exit(app.exec())
