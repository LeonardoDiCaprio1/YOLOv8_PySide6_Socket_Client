# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QVBoxLayout,
    QWidget)
import util.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1220, 725)
        font = QFont()
        font.setFamilies([u"aakar"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.Main_QW = QWidget(MainWindow)
        self.Main_QW.setObjectName(u"Main_QW")
        self.verticalLayout = QVBoxLayout(self.Main_QW)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_QF = QFrame(self.Main_QW)
        self.Main_QF.setObjectName(u"Main_QF")
        self.Main_QF.setStyleSheet(u"QFrame#Main_QF{\n"
"	background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(0, 205, 102), stop:1 rgb(180, 140, 255));\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.main_qframe = QHBoxLayout(self.Main_QF)
        self.main_qframe.setSpacing(0)
        self.main_qframe.setObjectName(u"main_qframe")
        self.main_qframe.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuBg = QFrame(self.Main_QF)
        self.LeftMenuBg.setObjectName(u"LeftMenuBg")
        self.LeftMenuBg.setMinimumSize(QSize(68, 0))
        self.LeftMenuBg.setMaximumSize(QSize(68, 16777215))
        self.LeftMenuBg.setStyleSheet(u"QFrame#LeftMenuBg{\n"
"	background-color: rgba(255, 255, 255,0);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.LeftMenuBg.setFrameShape(QFrame.NoFrame)
        self.LeftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.TopLogoInfo = QFrame(self.LeftMenuBg)
        self.TopLogoInfo.setObjectName(u"TopLogoInfo")
        self.TopLogoInfo.setEnabled(True)
        self.TopLogoInfo.setMinimumSize(QSize(0, 70))
        self.TopLogoInfo.setMaximumSize(QSize(16777215, 70))
        self.TopLogoInfo.setFrameShape(QFrame.StyledPanel)
        self.TopLogoInfo.setFrameShadow(QFrame.Raised)
        self.logo = QWidget(self.TopLogoInfo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 10, 50, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(50, 50))
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setStyleSheet(u"image: url(:/all/img/logo.png);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:10px")
        self.Author = QLabel(self.TopLogoInfo)
        self.Author.setObjectName(u"Author")
        self.Author.setGeometry(QRect(90, 30, 60, 30))
        sizePolicy.setHeightForWidth(self.Author.sizePolicy().hasHeightForWidth())
        self.Author.setSizePolicy(sizePolicy)
        self.Author.setMinimumSize(QSize(60, 30))
        self.Author.setMaximumSize(QSize(60, 30))
        self.Author.setStyleSheet(u"font: italic 11pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 255);")
        self.Author.setAlignment(Qt.AlignCenter)
        self.Title = QLabel(self.TopLogoInfo)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(60, 10, 121, 20))
        self.Title.setMaximumSize(QSize(16777215, 30))
        self.Title.setStyleSheet(u"font: 600 13pt \"Segoe UI Semibold\";\n"
"color: rgba(255, 255, 255, 255);")
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.TopLogoInfo)

        self.ToggleBox = QFrame(self.LeftMenuBg)
        self.ToggleBox.setObjectName(u"ToggleBox")
        self.ToggleBox.setMinimumSize(QSize(200, 80))
        self.ToggleBox.setMaximumSize(QSize(200, 80))
        self.ToggleBox.setFrameShape(QFrame.NoFrame)
        self.ToggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ToggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ToggleBotton = QPushButton(self.ToggleBox)
        self.ToggleBotton.setObjectName(u"ToggleBotton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToggleBotton.sizePolicy().hasHeightForWidth())
        self.ToggleBotton.setSizePolicy(sizePolicy1)
        self.ToggleBotton.setMinimumSize(QSize(0, 45))
        self.ToggleBotton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.ToggleBotton.setFont(font1)
        self.ToggleBotton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ToggleBotton.setMouseTracking(True)
        self.ToggleBotton.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton.setAutoFillBackground(False)
        self.ToggleBotton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        icon = QIcon()
        iconThemeName = u"zoom-out"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.ToggleBotton.setIcon(icon)
        self.ToggleBotton.setAutoDefault(False)
        self.ToggleBotton.setFlat(False)

        self.verticalLayout_4.addWidget(self.ToggleBotton)


        self.verticalLayout_2.addWidget(self.ToggleBox)

        self.MenuBox = QFrame(self.LeftMenuBg)
        self.MenuBox.setObjectName(u"MenuBox")
        self.MenuBox.setMinimumSize(QSize(200, 0))
        self.MenuBox.setMaximumSize(QSize(200, 16777215))
        self.MenuBox.setFrameShape(QFrame.NoFrame)
        self.MenuBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.MenuBox)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.src_file_button = QPushButton(self.MenuBox)
        self.src_file_button.setObjectName(u"src_file_button")
        self.src_file_button.setMinimumSize(QSize(0, 45))
        self.src_file_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_file_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/file.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.verticalLayout_5.addWidget(self.src_file_button)

        self.src_cam_button = QPushButton(self.MenuBox)
        self.src_cam_button.setObjectName(u"src_cam_button")
        self.src_cam_button.setMinimumSize(QSize(0, 45))
        self.src_cam_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_cam_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/cam.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.verticalLayout_5.addWidget(self.src_cam_button)

        self.src_rtsp_button = QPushButton(self.MenuBox)
        self.src_rtsp_button.setObjectName(u"src_rtsp_button")
        self.src_rtsp_button.setMinimumSize(QSize(0, 45))
        self.src_rtsp_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_rtsp_button.setAutoFillBackground(False)
        self.src_rtsp_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/RTSP.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.verticalLayout_5.addWidget(self.src_rtsp_button)

        self.src_goal_button = QPushButton(self.MenuBox)
        self.src_goal_button.setObjectName(u"src_goal_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.src_goal_button.sizePolicy().hasHeightForWidth())
        self.src_goal_button.setSizePolicy(sizePolicy2)
        self.src_goal_button.setMinimumSize(QSize(0, 45))
        self.src_goal_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_goal_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/goal.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.verticalLayout_5.addWidget(self.src_goal_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_5.setStretch(0, 1)

        self.verticalLayout_2.addWidget(self.MenuBox)

        self.VersionInfo = QFrame(self.LeftMenuBg)
        self.VersionInfo.setObjectName(u"VersionInfo")
        self.VersionInfo.setMinimumSize(QSize(200, 10))
        self.VersionInfo.setMaximumSize(QSize(200, 15))
        self.VersionInfo.setFrameShape(QFrame.StyledPanel)
        self.VersionInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.VersionInfo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(18, 0, -1, 0)
        self.VersionLabel = QLabel(self.VersionInfo)
        self.VersionLabel.setObjectName(u"VersionLabel")
        self.VersionLabel.setStyleSheet(u"font: 900 italic 10pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 199);")
        self.VersionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.VersionLabel)


        self.verticalLayout_2.addWidget(self.VersionInfo)


        self.main_qframe.addWidget(self.LeftMenuBg)

        self.ContentBox = QFrame(self.Main_QF)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setStyleSheet(u"QFrame#ContentBox{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.ContentBox.setFrameShape(QFrame.StyledPanel)
        self.ContentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.ContentBox)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 30))
        self.top.setMaximumSize(QSize(16777215, 30))
        self.top.setStyleSheet(u"QFrame#top{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, -1, 0)
        self.explain_title = QLabel(self.top)
        self.explain_title.setObjectName(u"explain_title")
        self.explain_title.setMinimumSize(QSize(0, 30))
        self.explain_title.setMaximumSize(QSize(16777215, 30))
        self.explain_title.setStyleSheet(u"font: 700 italic 11pt \"Segoe UI\";")
        self.explain_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.explain_title)

        self.buttons_sf = QFrame(self.top)
        self.buttons_sf.setObjectName(u"buttons_sf")
        self.buttons_sf.setMinimumSize(QSize(85, 30))
        self.buttons_sf.setMaximumSize(QSize(85, 30))
        self.buttons_sf.setFrameShape(QFrame.StyledPanel)
        self.buttons_sf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_sf)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.min_sf = QPushButton(self.buttons_sf)
        self.min_sf.setObjectName(u"min_sf")
        self.min_sf.setMinimumSize(QSize(14, 14))
        self.min_sf.setMaximumSize(QSize(14, 14))
        self.min_sf.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(4, 180, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.min_sf)

        self.max_sf = QPushButton(self.buttons_sf)
        self.max_sf.setObjectName(u"max_sf")
        self.max_sf.setMinimumSize(QSize(14, 14))
        self.max_sf.setMaximumSize(QSize(14, 14))
        self.max_sf.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(227, 199, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.max_sf)

        self.close_button = QPushButton(self.buttons_sf)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(14, 14))
        self.close_button.setMaximumSize(QSize(14, 14))
        self.close_button.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(240, 108, 96);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.buttons_sf)


        self.verticalLayout_6.addWidget(self.top)

        self.content = QFrame(self.ContentBox)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.main_content = QVBoxLayout()
        self.main_content.setSpacing(5)
        self.main_content.setObjectName(u"main_content")
        self.char_label = QLabel(self.content)
        self.char_label.setObjectName(u"char_label")
        self.char_label.setMinimumSize(QSize(0, 20))
        self.char_label.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.char_label.setFont(font2)
        self.char_label.setStyleSheet(u"padding-left:12px;")

        self.main_content.addWidget(self.char_label)

        self.QF_Group = QFrame(self.content)
        self.QF_Group.setObjectName(u"QF_Group")
        self.QF_Group.setMinimumSize(QSize(0, 100))
        self.QF_Group.setMaximumSize(QSize(16777215, 100))
        self.QF_Group.setStyleSheet(u"QFrame#QF_Group{\n"
"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.QF_Group.setFrameShape(QFrame.StyledPanel)
        self.QF_Group.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.QF_Group)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 15)
        self.Class_QF = QFrame(self.QF_Group)
        self.Class_QF.setObjectName(u"Class_QF")
        self.Class_QF.setMinimumSize(QSize(170, 80))
        self.Class_QF.setMaximumSize(QSize(170, 80))
        self.Class_QF.setToolTipDuration(0)
        self.Class_QF.setStyleSheet(u"QFrame#Class_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);\n"
"}\n"
"")
        self.Class_QF.setFrameShape(QFrame.StyledPanel)
        self.Class_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Class_QF)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Class_top = QFrame(self.Class_QF)
        self.Class_top.setObjectName(u"Class_top")
        self.Class_top.setStyleSheet(u"border:none")
        self.Class_top.setFrameShape(QFrame.StyledPanel)
        self.Class_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Class_top)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 3, 0, 3)
        self.label_5 = QLabel(self.Class_top)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setIndent(0)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_7.addWidget(self.Class_top)

        self.line_2 = QFrame(self.Class_QF)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.Class_bottom = QFrame(self.Class_QF)
        self.Class_bottom.setObjectName(u"Class_bottom")
        self.Class_bottom.setStyleSheet(u"border:none")
        self.Class_bottom.setFrameShape(QFrame.StyledPanel)
        self.Class_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Class_bottom)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 6, 0, 6)
        self.Class_num = QLabel(self.Class_bottom)
        self.Class_num.setObjectName(u"Class_num")
        self.Class_num.setMinimumSize(QSize(0, 30))
        self.Class_num.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI"])
        font4.setPointSize(17)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.Class_num.setFont(font4)
        self.Class_num.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.Class_num.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.Class_num, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.Class_bottom)

        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 1)

        self.horizontalLayout_3.addWidget(self.Class_QF)

        self.Target_QF = QFrame(self.QF_Group)
        self.Target_QF.setObjectName(u"Target_QF")
        self.Target_QF.setMinimumSize(QSize(170, 80))
        self.Target_QF.setMaximumSize(QSize(170, 80))
        self.Target_QF.setToolTipDuration(0)
        self.Target_QF.setStyleSheet(u"QFrame#Target_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(253, 139, 133),  stop:1 rgb(248, 194, 152));\n"
"border: 1px outset rgb(252, 194, 149)\n"
"}\n"
"")
        self.Target_QF.setFrameShape(QFrame.StyledPanel)
        self.Target_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Target_QF)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Target_top = QFrame(self.Target_QF)
        self.Target_top.setObjectName(u"Target_top")
        self.Target_top.setStyleSheet(u"border:none")
        self.Target_top.setFrameShape(QFrame.StyledPanel)
        self.Target_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Target_top)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 3, 0, 3)
        self.label_6 = QLabel(self.Target_top)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setIndent(0)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.verticalLayout_9.addWidget(self.Target_top)

        self.line_3 = QFrame(self.Target_QF)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)

        self.Target_bottom = QFrame(self.Target_QF)
        self.Target_bottom.setObjectName(u"Target_bottom")
        self.Target_bottom.setStyleSheet(u"border:none")
        self.Target_bottom.setFrameShape(QFrame.StyledPanel)
        self.Target_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Target_bottom)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 6, 0, 6)
        self.Target_num = QLabel(self.Target_bottom)
        self.Target_num.setObjectName(u"Target_num")
        self.Target_num.setMinimumSize(QSize(0, 30))
        self.Target_num.setMaximumSize(QSize(16777215, 30))
        self.Target_num.setFont(font4)
        self.Target_num.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.Target_num.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.Target_num, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.Target_bottom)

        self.verticalLayout_9.setStretch(1, 2)
        self.verticalLayout_9.setStretch(2, 1)

        self.horizontalLayout_3.addWidget(self.Target_QF)

        self.Fps_QF = QFrame(self.QF_Group)
        self.Fps_QF.setObjectName(u"Fps_QF")
        self.Fps_QF.setMinimumSize(QSize(170, 80))
        self.Fps_QF.setMaximumSize(QSize(170, 80))
        self.Fps_QF.setToolTipDuration(0)
        self.Fps_QF.setStyleSheet(u"QFrame#Fps_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219)\n"
"}\n"
"")
        self.Fps_QF.setFrameShape(QFrame.StyledPanel)
        self.Fps_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Fps_QF)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Fps_top = QFrame(self.Fps_QF)
        self.Fps_top.setObjectName(u"Fps_top")
        self.Fps_top.setStyleSheet(u"border:none")
        self.Fps_top.setFrameShape(QFrame.StyledPanel)
        self.Fps_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Fps_top)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 3, 7, 3)
        self.label_7 = QLabel(self.Fps_top)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_7.setMidLineWidth(-1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setIndent(0)

        self.horizontalLayout_8.addWidget(self.label_7)


        self.verticalLayout_11.addWidget(self.Fps_top)

        self.line_4 = QFrame(self.Fps_QF)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 1))
        self.line_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_4)

        self.Fps_bottom = QFrame(self.Fps_QF)
        self.Fps_bottom.setObjectName(u"Fps_bottom")
        self.Fps_bottom.setStyleSheet(u"border:none")
        self.Fps_bottom.setFrameShape(QFrame.StyledPanel)
        self.Fps_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Fps_bottom)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 6, 0, 6)
        self.fps_label = QLabel(self.Fps_bottom)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setMinimumSize(QSize(0, 30))
        self.fps_label.setMaximumSize(QSize(16777215, 30))
        self.fps_label.setFont(font4)
        self.fps_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.fps_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.fps_label, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.Fps_bottom)

        self.verticalLayout_11.setStretch(1, 2)
        self.verticalLayout_11.setStretch(2, 1)

        self.horizontalLayout_3.addWidget(self.Fps_QF)

        self.Model_QF = QFrame(self.QF_Group)
        self.Model_QF.setObjectName(u"Model_QF")
        self.Model_QF.setMinimumSize(QSize(170, 80))
        self.Model_QF.setMaximumSize(QSize(170, 80))
        self.Model_QF.setToolTipDuration(0)
        self.Model_QF.setStyleSheet(u"QFrame#Model_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(66, 226, 192),  stop:1 rgb(62, 154, 193));\n"
"border: 1px outset rgb(72, 158, 204)\n"
"}\n"
"")
        self.Model_QF.setFrameShape(QFrame.StyledPanel)
        self.Model_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.Model_QF)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Model_top = QFrame(self.Model_QF)
        self.Model_top.setObjectName(u"Model_top")
        self.Model_top.setStyleSheet(u"border:none")
        self.Model_top.setFrameShape(QFrame.StyledPanel)
        self.Model_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Model_top)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 3, 7, 3)
        self.label_8 = QLabel(self.Model_top)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_8.setMidLineWidth(-1)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setIndent(0)

        self.horizontalLayout_9.addWidget(self.label_8)


        self.verticalLayout_13.addWidget(self.Model_top)

        self.line_5 = QFrame(self.Model_QF)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(16777215, 1))
        self.line_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_5)

        self.Model_bottom = QFrame(self.Model_QF)
        self.Model_bottom.setObjectName(u"Model_bottom")
        self.Model_bottom.setStyleSheet(u"border:none")
        self.Model_bottom.setFrameShape(QFrame.StyledPanel)
        self.Model_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.Model_bottom)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 6, 0, 6)
        self.Model_name = QLabel(self.Model_bottom)
        self.Model_name.setObjectName(u"Model_name")
        self.Model_name.setMinimumSize(QSize(0, 30))
        self.Model_name.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        self.Model_name.setFont(font5)
        self.Model_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 15pt \"Microsoft YaHei UI\";\n"
"")
        self.Model_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.Model_name, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.Model_bottom)

        self.verticalLayout_13.setStretch(1, 2)
        self.verticalLayout_13.setStretch(2, 1)

        self.horizontalLayout_3.addWidget(self.Model_QF)


        self.main_content.addWidget(self.QF_Group)

        self.Result_QF = QFrame(self.content)
        self.Result_QF.setObjectName(u"Result_QF")
        self.Result_QF.setStyleSheet(u"")
        self.Result_QF.setFrameShape(QFrame.StyledPanel)
        self.Result_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Result_QF)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.Result_QF)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(2)
        self.line_chart = QLabel(self.splitter)
        self.line_chart.setObjectName(u"line_chart")
        self.line_chart.setMinimumSize(QSize(200, 100))
        self.line_chart.setStyleSheet(u"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.line_chart.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.line_chart)
        self.res_video = QLabel(self.splitter)
        self.res_video.setObjectName(u"res_video")
        self.res_video.setMinimumSize(QSize(200, 100))
        self.res_video.setStyleSheet(u"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.res_video.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.res_video)

        self.verticalLayout_16.addWidget(self.splitter)


        self.main_content.addWidget(self.Result_QF)

        self.Pause_QF = QFrame(self.content)
        self.Pause_QF.setObjectName(u"Pause_QF")
        self.Pause_QF.setMinimumSize(QSize(0, 30))
        self.Pause_QF.setMaximumSize(QSize(16777215, 30))
        self.Pause_QF.setFrameShape(QFrame.StyledPanel)
        self.Pause_QF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Pause_QF)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 3, 0)
        self.progress_bar = QProgressBar(self.Pause_QF)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMinimumSize(QSize(0, 20))
        self.progress_bar.setMaximumSize(QSize(16777215, 20))
        self.progress_bar.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(253, 143, 134); \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(119, 111, 252, 200);\n"
"border-radius: 7px;\n"
"}")
        self.progress_bar.setMaximum(1000)
        self.progress_bar.setValue(0)

        self.horizontalLayout_4.addWidget(self.progress_bar)

        self.stop_button = QPushButton(self.Pause_QF)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 30))
        self.stop_button.setMaximumSize(QSize(16777215, 30))
        self.stop_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/stop.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.stop_button)


        self.main_content.addWidget(self.Pause_QF)


        self.horizontalLayout_5.addLayout(self.main_content)


        self.verticalLayout_6.addWidget(self.content)

        self.below = QFrame(self.ContentBox)
        self.below.setObjectName(u"below")
        self.below.setMinimumSize(QSize(0, 30))
        self.below.setMaximumSize(QSize(16777215, 30))
        self.below.setFrameShape(QFrame.StyledPanel)
        self.below.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.below)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 2, 0, 4)
        self.status_bar = QLabel(self.below)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setMinimumSize(QSize(600, 0))
        self.status_bar.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"color: rgba(0, 0, 0, 140);")

        self.horizontalLayout_13.addWidget(self.status_bar)

        self.frame_size_grip = QFrame(self.below)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"border-radius:30px;")
        self.frame_size_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.below)


        self.main_qframe.addWidget(self.ContentBox)


        self.verticalLayout.addWidget(self.Main_QF)

        MainWindow.setCentralWidget(self.Main_QW)

        self.retranslateUi(MainWindow)

        self.ToggleBotton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Author.setText(QCoreApplication.translate("MainWindow", u"shiwen", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"YOLO APP", None))
        self.ToggleBotton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.src_file_button.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.src_cam_button.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.src_rtsp_button.setText(QCoreApplication.translate("MainWindow", u"RTSP", None))
        self.src_goal_button.setText(QCoreApplication.translate("MainWindow", u"Goal", None))
        self.VersionLabel.setText("")
        self.explain_title.setText(QCoreApplication.translate("MainWindow", u"YOLO App  \u2013  Pedestrian flow monitoring system For YOLOv8", None))
        self.min_sf.setText("")
        self.max_sf.setText("")
        self.close_button.setText("")
        self.char_label.setText(QCoreApplication.translate("MainWindow", u"Detection", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Classes", None))
        self.Class_num.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Targets", None))
        self.Target_num.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fps", None))
        self.fps_label.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Use Model", None))
        self.Model_name.setText("")
        self.line_chart.setText("")
        self.res_video.setText("")
        self.stop_button.setText("")
        self.status_bar.setText(QCoreApplication.translate("MainWindow", u"欢迎使用人流量监测系统!                                                                        ", None))
    # retranslateUi

