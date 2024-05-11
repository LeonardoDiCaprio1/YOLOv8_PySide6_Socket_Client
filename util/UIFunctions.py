# -*- coding: utf-8 -*-🚀
import time
from sockets_client import *
from util.custom_grips import CustomGrip
from util.Ui_MainWindow import Ui_MainWindow
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QEvent, QTimer
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

GLOBAL_STATE = False  
GLOBAL_TITLE_BAR = True


class UIFuncitons(Ui_MainWindow):
    def __init__(self):
        super(UIFuncitons, self).__init__()
        self.dragPos = QPoint()  
        
    def toggleMenu(self, enable):
        if enable:
            standard = 68
            maxExtend = 180
            width = self.LeftMenuBg.width()

            if width == 68:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            
            self.animation = QPropertyAnimation(self.LeftMenuBg, b"minimumWidth")
            self.animation.setDuration(500) # ms
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuint)
            self.animation.start()

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False: 
            GLOBAL_STATE = True
            self.showMaximized()   
            self.max_sf.setToolTip("Restore")
            self.frame_size_grip.hide()   
            self.left_grip.hide()             
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()       
            self.resize(self.width()+1, self.height()+1)
            self.max_sf.setToolTip("Maximize")
            self.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
    
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFuncitons.maximize_restore(self))
        self.top.mouseDoubleClickEvent = dobleClickMaximizeRestore
        
        def moveWindow(event):
            if GLOBAL_STATE:                        
                UIFuncitons.maximize_restore(self)
            if event.buttons() == Qt.LeftButton: 
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
        self.top.mouseMoveEvent = moveWindow
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        self.min_sf.clicked.connect(lambda: self.showMinimized())
        self.max_sf.clicked.connect(lambda: UIFuncitons.maximize_restore(self))
        self.close_button.clicked.connect(self.close)

    def resize_grips(self):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def shadow_style(self, widget, Color):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(8, 8)  
        shadow.setBlurRadius(38)    
        shadow.setColor(Color)  
        widget.setGraphicsEffect(shadow) 
