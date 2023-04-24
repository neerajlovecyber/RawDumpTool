# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RDTNEW.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)
import nsp_rc

class Ui_RawDumpTool(object):
    def setupUi(self, RawDumpTool):
        if not RawDumpTool.objectName():
            RawDumpTool.setObjectName(u"RawDumpTool")
        RawDumpTool.setWindowModality(Qt.ApplicationModal)
        RawDumpTool.setEnabled(True)
        RawDumpTool.resize(1150, 625)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RawDumpTool.sizePolicy().hasHeightForWidth())
        RawDumpTool.setSizePolicy(sizePolicy)
        RawDumpTool.setMinimumSize(QSize(0, 0))
        RawDumpTool.setMaximumSize(QSize(1150, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(49, 49, 49, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        RawDumpTool.setPalette(palette)
        RawDumpTool.setCursor(QCursor(Qt.OpenHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/RDT.png", QSize(), QIcon.Normal, QIcon.Off)
        RawDumpTool.setWindowIcon(icon)
        RawDumpTool.setStyleSheet(u"QMainWindow{background-color: rgb(49, 49, 49);\n"
"border-radius:20px;}\n"
"\n"
"\n"
"QFrame{\n"
"background-color: rgb(49, 49, 49);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
" \n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: inset;\n"
"  \n"
"	background-color: rgb(170, 0, 255);\n"
"  \n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	border-color: rgb(170, 0, 255);\n"
"	background-color:rgb(170, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"   \n"
"	background-color: rgb(250, 82, 255);\n"
"    }\n"
"\n"
"")
        RawDumpTool.setAnimated(True)
        RawDumpTool.setDocumentMode(False)
        RawDumpTool.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(RawDumpTool)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(1150, 100000))
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush1)
        self.centralwidget.setPalette(palette1)
        font = QFont()
        font.setKerning(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QCursor(Qt.OpenHandCursor))
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"\n"
"QPushButton {\n"
" \n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"  \n"
"	background-color: rgb(170, 0, 255);\n"
"  \n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	border-color: rgb(170, 0, 255);\n"
"	background-color:rgb(170, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"   \n"
"	background-color: rgb(250, 82, 255);\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.side_menu_closed = QFrame(self.centralwidget)
        self.side_menu_closed.setObjectName(u"side_menu_closed")
        self.side_menu_closed.setMinimumSize(QSize(100, 0))
        self.side_menu_closed.setMaximumSize(QSize(150, 16777215))
        self.side_menu_closed.setStyleSheet(u"QPushButton:checked{\n"
"                    background-color: rgb(80, 80, 80);\n"
"                }")
        self.side_menu_closed.setFrameShape(QFrame.StyledPanel)
        self.side_menu_closed.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_closed)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.side_menu_closed)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.slide_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 10))
        self.label_2.setMaximumSize(QSize(100, 35))
        self.label_2.setStyleSheet(u"image: url(:/icons/coolicons PNG/White/Interface/Window_Terminal.png);")
        self.label_2.setPixmap(QPixmap(u"icons/RDT.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.home = QPushButton(self.frame_7)
        self.home.setObjectName(u"home")
        icon1 = QIcon()
        icon1.addFile(u"icons/home-3-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home.setIcon(icon1)
        self.home.setIconSize(QSize(25, 25))
        self.home.setCheckable(True)
        self.home.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.home)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.contact = QPushButton(self.frame_7)
        self.contact.setObjectName(u"contact")
        icon2 = QIcon()
        icon2.addFile(u"icons/message-2-xxl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.contact.setIcon(icon2)
        self.contact.setIconSize(QSize(25, 25))
        self.contact.setCheckable(True)
        self.contact.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.contact)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.checkmini_btn = QPushButton(self.frame_7)
        self.checkmini_btn.setObjectName(u"checkmini_btn")
        icon3 = QIcon()
        icon3.addFile(u"icons/lock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkmini_btn.setIcon(icon3)
        self.checkmini_btn.setIconSize(QSize(25, 25))
        self.checkmini_btn.setCheckable(True)
        self.checkmini_btn.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.checkmini_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.info = QPushButton(self.frame_7)
        self.info.setObjectName(u"info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u"icons/info-xxl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info.setIcon(icon4)
        self.info.setIconSize(QSize(25, 29))
        self.info.setCheckable(True)
        self.info.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.info)


        self.verticalLayout_8.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.side_menu_closed)

        self.side_menu_open = QFrame(self.centralwidget)
        self.side_menu_open.setObjectName(u"side_menu_open")
        self.side_menu_open.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.side_menu_open.sizePolicy().hasHeightForWidth())
        self.side_menu_open.setSizePolicy(sizePolicy2)
        self.side_menu_open.setMaximumSize(QSize(250, 16777215))
        self.side_menu_open.setBaseSize(QSize(2, 2))
        self.side_menu_open.setFrameShape(QFrame.StyledPanel)
        self.side_menu_open.setFrameShadow(QFrame.Raised)
        self.side_menu_open.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.side_menu_open)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.side_menu_open)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setFocusPolicy(Qt.NoFocus)
        self.frame_8.setAcceptDrops(False)
        self.frame_8.setStyleSheet(u".frame_8{border:5px solid;\n"
"border-color: rgb(225, 217, 255);}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);}\n"
"QPushButton:checked{\n"
"                    background-color: rgb(80, 80, 80);\n"
"                }")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(250, 100))
        self.label_3.setPixmap(QPixmap(u"icons/logo.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_3)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.home_btn = QPushButton(self.frame_8)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(34, 34))
        self.home_btn.setMaximumSize(QSize(16777215, 34))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.home_btn.setFont(font1)
        self.home_btn.setStyleSheet(u"")
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QSize(20, 20))
        self.home_btn.setCheckable(True)
        self.home_btn.setChecked(True)
        self.home_btn.setAutoExclusive(True)
        self.home_btn.setFlat(False)

        self.verticalLayout_6.addWidget(self.home_btn)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.check_btn = QPushButton(self.frame_8)
        self.check_btn.setObjectName(u"check_btn")
        self.check_btn.setEnabled(True)
        self.check_btn.setMinimumSize(QSize(0, 34))
        self.check_btn.setFont(font1)
        self.check_btn.setIcon(icon3)
        self.check_btn.setIconSize(QSize(17, 17))
        self.check_btn.setCheckable(True)
        self.check_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.check_btn)

        self.verticalSpacer_10 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.contact_btn = QPushButton(self.frame_8)
        self.contact_btn.setObjectName(u"contact_btn")
        self.contact_btn.setEnabled(True)
        self.contact_btn.setMinimumSize(QSize(0, 34))
        self.contact_btn.setFont(font1)
        self.contact_btn.setIcon(icon2)
        self.contact_btn.setIconSize(QSize(17, 17))
        self.contact_btn.setCheckable(True)
        self.contact_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.contact_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 337, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.infobtn = QPushButton(self.frame_8)
        self.infobtn.setObjectName(u"infobtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.infobtn.sizePolicy().hasHeightForWidth())
        self.infobtn.setSizePolicy(sizePolicy3)
        self.infobtn.setMinimumSize(QSize(0, 34))
        self.infobtn.setBaseSize(QSize(40, 100))
        self.infobtn.setFont(font1)
        self.infobtn.setIcon(icon4)
        self.infobtn.setIconSize(QSize(20, 20))
        self.infobtn.setCheckable(True)
        self.infobtn.setAutoExclusive(True)
        self.infobtn.setFlat(False)

        self.verticalLayout_6.addWidget(self.infobtn)


        self.verticalLayout_9.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.side_menu_open)

        self.Main_body = QFrame(self.centralwidget)
        self.Main_body.setObjectName(u"Main_body")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Main_body.sizePolicy().hasHeightForWidth())
        self.Main_body.setSizePolicy(sizePolicy4)
        self.Main_body.setMaximumSize(QSize(5000, 700))
        self.Main_body.setFrameShape(QFrame.StyledPanel)
        self.Main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.Main_body)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QSize(238, 0))
        self.header_frame.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(170, 0, 255);\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame)

        self.pushButton_6 = QPushButton(self.header_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(32, 32))
        self.pushButton_6.setToolTipDuration(0)
        icon5 = QIcon()
        icon5.addFile(u"icons/menu-4-xxl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(32, 32))
        self.pushButton_6.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minibtn_2 = QPushButton(self.header_frame)
        self.minibtn_2.setObjectName(u"minibtn_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.minibtn_2.sizePolicy().hasHeightForWidth())
        self.minibtn_2.setSizePolicy(sizePolicy5)
        font2 = QFont()
        font2.setFamilies([u"Script"])
        font2.setKerning(True)
        self.minibtn_2.setFont(font2)
        self.minibtn_2.setStyleSheet(u"QPushButton {\n"
" \n"
"    border: 0px solid #555;\n"
"    border-radius: 5px;\n"
"\n"
"\n"
"	background-color: rgb(52, 52, 52);\n"
"  \n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	border-color: rgb(170, 0, 255);\n"
"	background-color:rgb(240, 240, 240);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"   \n"
"	background-color: rgb(250, 82, 255);\n"
"    }")
        icon6 = QIcon()
        icon6.addFile(u"icons/icons8-do-not-disturb-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minibtn_2.setIcon(icon6)
        self.minibtn_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.minibtn_2)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.closebtn = QPushButton(self.frame_3)
        self.closebtn.setObjectName(u"closebtn")
        sizePolicy5.setHeightForWidth(self.closebtn.sizePolicy().hasHeightForWidth())
        self.closebtn.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Light"])
        self.closebtn.setFont(font3)
        self.closebtn.setStyleSheet(u"QPushButton {\n"
" \n"
"    border: 0px solid #555;\n"
"    border-radius: 5px;\n"
"\n"
"\n"
"	background-color: rgb(52, 52, 52);\n"
"  \n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	border-color: rgb(170, 0, 255);\n"
"	background-color:rgb(240, 240, 240);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"   \n"
"	background-color: rgb(250, 82, 255);\n"
"    }")
        icon7 = QIcon()
        icon7.addFile(u"icons/icons8-close-window-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closebtn.setIcon(icon7)
        self.closebtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.closebtn)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_content = QFrame(self.Main_body)
        self.main_body_content.setObjectName(u"main_body_content")
        sizePolicy.setHeightForWidth(self.main_body_content.sizePolicy().hasHeightForWidth())
        self.main_body_content.setSizePolicy(sizePolicy)
        self.main_body_content.setMaximumSize(QSize(16777215, 16777215))
        self.main_body_content.setBaseSize(QSize(700, 0))
        self.main_body_content.setStyleSheet(u"")
        self.main_body_content.setFrameShape(QFrame.WinPanel)
        self.main_body_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_body_content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy6)
        self.stackedWidget.setMinimumSize(QSize(775, 524))
        self.stackedWidget.setMaximumSize(QSize(1200, 524))
        self.stackedWidget.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
" \n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"  \n"
"	background-color: rgb(170, 0, 255);\n"
"  \n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	border-color: rgb(170, 0, 255);\n"
"	background-color:rgb(170, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"   \n"
"	background-color: rgb(250, 82, 255);\n"
"    }\n"
"\n"
"")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.dumpbtn = QPushButton(self.home_page)
        self.dumpbtn.setObjectName(u"dumpbtn")
        self.dumpbtn.setEnabled(True)
        self.dumpbtn.setGeometry(QRect(270, 450, 221, 51))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.dumpbtn.setFont(font4)
        self.dumpbtn.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);}\n"
"QPushButton:disabled {\n"
"  \n"
"	background-color: rgb(95, 95, 95);\n"
"   \n"
"	\n"
"    }")
        self.label_6 = QLabel(self.home_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 260, 661, 81))
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.label_6.setFont(font5)
        self.label_6.setAcceptDrops(False)
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 361, 151))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setKerning(False)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"\n"
"image: url(:/newPrefix/animation(1).gif);")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setPixmap(QPixmap(u"icons/logo.png"))
        self.label.setScaledContents(True)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_7 = QLabel(self.home_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 180, 131, 21))
        font7 = QFont()
        font7.setFamilies([u"Verdana"])
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setKerning(False)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.label_7.setFont(font7)
        self.dumploc = QTextEdit(self.home_page)
        self.dumploc.setObjectName(u"dumploc")
        self.dumploc.setGeometry(QRect(80, 370, 451, 31))
        font8 = QFont()
        font8.setFamilies([u"inherit"])
        font8.setPointSize(10)
        font8.setBold(True)
        self.dumploc.setFont(font8)
        self.dumploc.setAcceptDrops(False)
        self.dumploc.setStyleSheet(u"color: rgb(241, 0, 4);\n"
"background-color: rgb(203, 211, 255);\n"
"\n"
"border:3px solid;\n"
"border-radius:20px;\n"
"\n"
"\n"
"font-family: inherit;\n"
"")
        self.pushButton = QPushButton(self.home_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 370, 93, 31))
        font9 = QFont()
        font9.setFamilies([u"Verdana"])
        font9.setPointSize(10)
        font9.setBold(True)
        self.pushButton.setFont(font9)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.checkBox = QCheckBox(self.home_page)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(84, 410, 101, 28))
        self.checkBox.setFont(font1)
        self.checkBox.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 0, 4);\n"
"	padding:2px;\n"
"   border:3px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QCheckBox:hover{\n"
"	\n"
"	background-color: rgb(102, 255, 99);\n"
"}\n"
"QCheckBox:checked{\n"
"	background-color: rgb(0, 255, 38);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.linepass_2 = QLineEdit(self.home_page)
        self.linepass_2.setObjectName(u"linepass_2")
        self.linepass_2.setEnabled(True)
        self.linepass_2.setGeometry(QRect(190, 410, 451, 28))
        self.linepass_2.setFont(font8)
        self.linepass_2.setStyleSheet(u"QLineEdit{color: rgb(241, 0, 4);\n"
"background-color: rgb(203, 211, 255);\n"
"\n"
"border:3px solid;\n"
"border-radius:20px;\n"
"\n"
"\n"
"font-family: inherit;}\n"
"QLineEdit: disabled {\n"
"    \n"
"	background-color: rgb(255, 0, 4);\n"
"}")
        self.linepass_2.setEchoMode(QLineEdit.Password)
        self.stackedWidget.addWidget(self.home_page)
        self.contact_page = QWidget()
        self.contact_page.setObjectName(u"contact_page")
        self.contact_page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.contact_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.contact_page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"\n"
"border:3px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 2, 0)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u"icons/ghan.png"))
        self.label_10.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_10)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"\n"
"border:3px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u"icons/nsp.png"))
        self.label_11.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_11)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"\n"
"border:3px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:10px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u"icons/aksh.png"))
        self.label_12.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_12)


        self.horizontalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_13 = QFrame(self.widget_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 60))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.frame_20 = QFrame(self.frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_20)
        self.label_16.setObjectName(u"label_16")
        font10 = QFont()
        font10.setPointSize(22)
        font10.setBold(True)
        self.label_16.setFont(font10)
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border:4px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:15px;")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setOpenExternalLinks(True)

        self.horizontalLayout_11.addWidget(self.label_16)


        self.horizontalLayout_8.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font10)
        self.label_17.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border:4px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:15px;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setOpenExternalLinks(True)

        self.verticalLayout_14.addWidget(self.label_17)


        self.horizontalLayout_8.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        font11 = QFont()
        font11.setPointSize(21)
        font11.setBold(True)
        self.label_18.setFont(font11)
        self.label_18.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border:4px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:15px;")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setOpenExternalLinks(True)

        self.horizontalLayout_13.addWidget(self.label_18)


        self.horizontalLayout_8.addWidget(self.frame_18)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 250))
        self.frame_10.setStyleSheet(u"\n"
"border:3px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:10px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u"icons/shr.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_13)


        self.horizontalLayout_6.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"\n"
"border:3px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:10px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u"icons/yog.png"))
        self.label_14.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_14)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"\n"
"border:3px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:10px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u"icons/vin.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_15)


        self.horizontalLayout_6.addWidget(self.frame_12)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_14 = QFrame(self.widget_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 60))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 0, 246, 38))
        self.label_19.setFont(font10)
        self.label_19.setLayoutDirection(Qt.LeftToRight)
        self.label_19.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border:4px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:15px;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setOpenExternalLinks(True)

        self.horizontalLayout_7.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 0, 246, 38))
        self.label_20.setFont(font10)
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border:4px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:15px;")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setOpenExternalLinks(True)

        self.horizontalLayout_7.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 246, 38))
        self.label_21.setFont(font10)
        self.label_21.setLayoutDirection(Qt.LeftToRight)
        self.label_21.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border:4px solid;\n"
"border-color: rgb(170, 0, 255);\n"
"border-radius:15px;")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setOpenExternalLinks(True)

        self.horizontalLayout_7.addWidget(self.frame_17)


        self.verticalLayout_3.addWidget(self.frame_14)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.contact_page)
        self.Info_page = QWidget()
        self.Info_page.setObjectName(u"Info_page")
        self.Info_page.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.verticalLayout_11 = QVBoxLayout(self.Info_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.Info_page)
        self.widget.setObjectName(u"widget")
        font12 = QFont()
        font12.setBold(True)
        self.widget.setFont(font12)
        self.widget.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 80, 171, 351))
        self.label_4.setPixmap(QPixmap(u"icons/nsp.png.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setIndent(18)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 70, 531, 61))
        font13 = QFont()
        font13.setFamilies([u"Verdana"])
        font13.setPointSize(12)
        font13.setBold(True)
        self.label_5.setFont(font13)
        self.label_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 150, 511, 241))
        font14 = QFont()
        font14.setFamilies([u"Arial"])
        font14.setPointSize(11)
        font14.setBold(True)
        self.label_8.setFont(font14)
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(True)
        self.label_8.setOpenExternalLinks(True)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(340, 410, 201, 41))
        font15 = QFont()
        font15.setPointSize(23)
        self.label_9.setFont(font15)
        self.label_9.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setStyleSheet(u"color: rgb(255, 1, 35);\n"
"background-color: rgb(255, 216, 213);")
        self.label_9.setFrameShadow(QFrame.Plain)
        self.label_9.setScaledContents(True)
        self.label_9.setOpenExternalLinks(True)

        self.verticalLayout_11.addWidget(self.widget)

        self.stackedWidget.addWidget(self.Info_page)
        self.checkpage = QWidget()
        self.checkpage.setObjectName(u"checkpage")
        self.checkpage.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.dumploc_2 = QTextEdit(self.checkpage)
        self.dumploc_2.setObjectName(u"dumploc_2")
        self.dumploc_2.setGeometry(QRect(90, 90, 451, 31))
        self.dumploc_2.setFont(font8)
        self.dumploc_2.setAcceptDrops(False)
        self.dumploc_2.setStyleSheet(u"color: rgb(241, 0, 4);\n"
"background-color: rgb(203, 211, 255);\n"
"\n"
"border:3px solid;\n"
"border-radius:20px;\n"
"\n"
"\n"
"font-family: inherit;\n"
"")
        self.selectfile = QPushButton(self.checkpage)
        self.selectfile.setObjectName(u"selectfile")
        self.selectfile.setGeometry(QRect(550, 90, 93, 31))
        self.selectfile.setFont(font9)
        self.selectfile.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.encbtn = QPushButton(self.checkpage)
        self.encbtn.setObjectName(u"encbtn")
        self.encbtn.setEnabled(True)
        self.encbtn.setGeometry(QRect(90, 220, 161, 41))
        self.encbtn.setFont(font4)
        self.encbtn.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);}\n"
"QPushButton:disabled {\n"
"  \n"
"	background-color: rgb(95, 95, 95);\n"
"   \n"
"	\n"
"    }")
        self.decbtn = QPushButton(self.checkpage)
        self.decbtn.setObjectName(u"decbtn")
        self.decbtn.setEnabled(True)
        self.decbtn.setGeometry(QRect(260, 220, 161, 41))
        self.decbtn.setFont(font4)
        self.decbtn.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);}\n"
"QPushButton:disabled {\n"
"  \n"
"	background-color: rgb(95, 95, 95);\n"
"   \n"
"	\n"
"    }")
        self.checkbtn = QPushButton(self.checkpage)
        self.checkbtn.setObjectName(u"checkbtn")
        self.checkbtn.setEnabled(True)
        self.checkbtn.setGeometry(QRect(240, 420, 211, 41))
        self.checkbtn.setFont(font4)
        self.checkbtn.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);}\n"
"QPushButton:disabled {\n"
"  \n"
"	background-color: rgb(95, 95, 95);\n"
"   \n"
"	\n"
"    }")
        self.linepass = QLineEdit(self.checkpage)
        self.linepass.setObjectName(u"linepass")
        self.linepass.setEnabled(True)
        self.linepass.setGeometry(QRect(90, 170, 451, 28))
        self.linepass.setFont(font8)
        self.linepass.setStyleSheet(u"QLineEdit{color: rgb(241, 0, 4);\n"
"background-color: rgb(203, 211, 255);\n"
"\n"
"border:3px solid;\n"
"border-radius:20px;\n"
"\n"
"\n"
"font-family: inherit;}\n"
"QLineEdit: disabled {\n"
"    \n"
"	background-color: rgb(255, 0, 4);\n"
"}")
        self.linepass.setEchoMode(QLineEdit.Password)
        self.dumploc_3 = QTextEdit(self.checkpage)
        self.dumploc_3.setObjectName(u"dumploc_3")
        self.dumploc_3.setGeometry(QRect(90, 370, 451, 31))
        self.dumploc_3.setFont(font8)
        self.dumploc_3.setAcceptDrops(False)
        self.dumploc_3.setStyleSheet(u"color: rgb(241, 0, 4);\n"
"background-color: rgb(203, 211, 255);\n"
"\n"
"border:3px solid;\n"
"border-radius:20px;\n"
"\n"
"\n"
"font-family: inherit;\n"
"")
        self.checkselect = QPushButton(self.checkpage)
        self.checkselect.setObjectName(u"checkselect")
        self.checkselect.setGeometry(QRect(550, 370, 93, 31))
        self.checkselect.setFont(font9)
        self.checkselect.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.dumpbtn_5 = QPushButton(self.checkpage)
        self.dumpbtn_5.setObjectName(u"dumpbtn_5")
        self.dumpbtn_5.setEnabled(True)
        self.dumpbtn_5.setGeometry(QRect(90, 310, 241, 41))
        self.dumpbtn_5.setFont(font4)
        self.dumpbtn_5.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.dumpbtn_5.setFlat(True)
        self.dumpbtn_6 = QPushButton(self.checkpage)
        self.dumpbtn_6.setObjectName(u"dumpbtn_6")
        self.dumpbtn_6.setEnabled(True)
        self.dumpbtn_6.setGeometry(QRect(90, 30, 241, 41))
        self.dumpbtn_6.setFont(font4)
        self.dumpbtn_6.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.dumpbtn_6.setFlat(True)
        self.checkbtn_2 = QPushButton(self.checkpage)
        self.checkbtn_2.setObjectName(u"checkbtn_2")
        self.checkbtn_2.setEnabled(True)
        self.checkbtn_2.setGeometry(QRect(240, 470, 211, 41))
        self.checkbtn_2.setFont(font4)
        self.checkbtn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(224, 253, 255);}\n"
"QPushButton:disabled {\n"
"  \n"
"	background-color: rgb(95, 95, 95);\n"
"   \n"
"	\n"
"    }")
        self.checkbtn_3 = QPushButton(self.checkpage)
        self.checkbtn_3.setObjectName(u"checkbtn_3")
        self.checkbtn_3.setEnabled(True)
        self.checkbtn_3.setGeometry(QRect(440, 220, 211, 41))
        self.checkbtn_3.setFont(font4)
        self.checkbtn_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(224, 253, 255);}\n"
"QPushButton:disabled {\n"
"  \n"
"	background-color: rgb(95, 95, 95);\n"
"   \n"
"	\n"
"    }")
        self.selectfolder = QPushButton(self.checkpage)
        self.selectfolder.setObjectName(u"selectfolder")
        self.selectfolder.setGeometry(QRect(550, 130, 93, 31))
        self.selectfolder.setFont(font9)
        self.selectfolder.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.folderlock = QTextEdit(self.checkpage)
        self.folderlock.setObjectName(u"folderlock")
        self.folderlock.setGeometry(QRect(90, 130, 451, 31))
        self.folderlock.setFont(font8)
        self.folderlock.setAcceptDrops(False)
        self.folderlock.setStyleSheet(u"color: rgb(241, 0, 4);\n"
"background-color: rgb(203, 211, 255);\n"
"\n"
"border:3px solid;\n"
"border-radius:20px;\n"
"\n"
"\n"
"font-family: inherit;\n"
"")
        self.stackedWidget.addWidget(self.checkpage)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body_content, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.Main_body)

        RawDumpTool.setCentralWidget(self.centralwidget)

        self.retranslateUi(RawDumpTool)
        self.pushButton_6.toggled.connect(self.frame_8.setHidden)
        self.pushButton_6.toggled.connect(self.side_menu_closed.setVisible)
        self.home.toggled.connect(self.home_btn.setChecked)
        self.home_btn.toggled.connect(self.home.setChecked)
        self.contact.toggled.connect(self.contact_btn.setChecked)
        self.contact_btn.toggled.connect(self.contact.setChecked)
        self.info.toggled.connect(self.infobtn.setChecked)
        self.infobtn.toggled.connect(self.info.setChecked)
        self.checkmini_btn.toggled.connect(self.check_btn.setChecked)
        self.check_btn.toggled.connect(self.checkmini_btn.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RawDumpTool)
    # setupUi

    def retranslateUi(self, RawDumpTool):
        RawDumpTool.setWindowTitle(QCoreApplication.translate("RawDumpTool", u"Raw Data Tool 6.0 - By Rot 6", None))
        self.label_2.setText("")
#if QT_CONFIG(tooltip)
        self.home.setToolTip(QCoreApplication.translate("RawDumpTool", u"Home Tab", None))
#endif // QT_CONFIG(tooltip)
        self.home.setText("")
#if QT_CONFIG(tooltip)
        self.contact.setToolTip(QCoreApplication.translate("RawDumpTool", u"Contact Information", None))
#endif // QT_CONFIG(tooltip)
        self.contact.setText("")
#if QT_CONFIG(tooltip)
        self.checkmini_btn.setToolTip(QCoreApplication.translate("RawDumpTool", u"Contact Information", None))
#endif // QT_CONFIG(tooltip)
        self.checkmini_btn.setText("")
#if QT_CONFIG(tooltip)
        self.info.setToolTip(QCoreApplication.translate("RawDumpTool", u"Show Info about this tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.info.setWhatsThis(QCoreApplication.translate("RawDumpTool", u"Show Info about this tool", None))
#endif // QT_CONFIG(whatsthis)
        self.info.setText("")
        self.label_3.setText("")
        self.home_btn.setText(QCoreApplication.translate("RawDumpTool", u"Home", None))
        self.check_btn.setText(QCoreApplication.translate("RawDumpTool", u"Security + Encryption", None))
        self.contact_btn.setText(QCoreApplication.translate("RawDumpTool", u"Contact", None))
        self.infobtn.setText(QCoreApplication.translate("RawDumpTool", u"Information", None))
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("RawDumpTool", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText("")
#if QT_CONFIG(tooltip)
        self.minibtn_2.setToolTip(QCoreApplication.translate("RawDumpTool", u"Mininmize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minibtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.closebtn.setToolTip(QCoreApplication.translate("RawDumpTool", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closebtn.setText("")
        self.dumpbtn.setText(QCoreApplication.translate("RawDumpTool", u"Dump Memory", None))
        self.label_6.setText(QCoreApplication.translate("RawDumpTool", u"RDT 6.0 is an volatile memory acquisition tool put Together by Rot6 Team, intended to be run directly from a usb without any installion. Works on debian linux , windows platform.", None))
        self.label.setText("")
        self.label_7.setText(QCoreApplication.translate("RawDumpTool", u"-By Rot6 Team", None))
        self.dumploc.setHtml(QCoreApplication.translate("RawDumpTool", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'inherit'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>", None))
        self.dumploc.setPlaceholderText(QCoreApplication.translate("RawDumpTool", u"Select location to store dump file", None))
        self.pushButton.setText(QCoreApplication.translate("RawDumpTool", u"Select", None))
        self.checkBox.setText(QCoreApplication.translate("RawDumpTool", u"Encrypt", None))
#if QT_CONFIG(accessibility)
        self.linepass_2.setAccessibleDescription(QCoreApplication.translate("RawDumpTool", u"ss", None))
#endif // QT_CONFIG(accessibility)
        self.linepass_2.setPlaceholderText(QCoreApplication.translate("RawDumpTool", u"Enter Password to Encrypt/Decrypt Dump File", None))
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_16.setText(QCoreApplication.translate("RawDumpTool", u"<html><head/><body><p><a href=\"https://www.linkedin.com/in/ghanshyam-kumar-yadav-2001/\"><span style=\" text-decoration: underline; color:#2777ff;\">Linkedln</span></a></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("RawDumpTool", u"<html><head/><body><p><a href=\"https://www.linkedin.com/in/neeraj-singh-950a4b1a5\"><span style=\" text-decoration: underline; color:#2777ff;\">Linkedln</span></a></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("RawDumpTool", u"<html><head/><body><p><a href=\"https://www.linkedin.com/in/aksh-choudhary-686466239\"><span style=\" text-decoration: underline; color:#2777ff;\">Linkedln</span></a></p></body></html>", None))
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_19.setText(QCoreApplication.translate("RawDumpTool", u"<html><head/><body><p><a href=\"https://www.linkedin.com/in/shreya-patel-402b861aa/\"><span style=\" text-decoration: underline; color:#2777ff;\">Linkedln</span></a></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("RawDumpTool", u"<html><head/><body><p><a href=\"file:///media/neeraj/Windows-SSD/Users/nirma/Desktop/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/icons/contact.html#\"><span style=\" text-decoration: underline; color:#2777ff;\">Linkedln</span></a></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("RawDumpTool", u"<html><head/><body><p><a href=\"https://www.linkedin.com/in/vinay-pal-a709b0201/\"><span style=\" text-decoration: underline; color:#2777ff;\">Linkedln</span></a></p></body></html>", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("RawDumpTool", u"\u201cGreat computers hardware is only doorstop without great\u00a0software.\u201d", None))
        self.label_8.setText(QCoreApplication.translate("RawDumpTool", u"Here is our tool that will dump ram memory for you just at one \n"
"click and takes minimal space and saves you from undergoing\n"
"a hectic process of downloading dependencies and installation.\n"
"This tool can work without internet and can work on Windows\n"
"and Linux operating system. You can just click and run and \n"
"dump memory using simple GUI and portable\u00a0to\u00a0pass\u00a0on.", None))
        self.label_9.setText(QCoreApplication.translate("RawDumpTool", u"<html><head/><body><p align=\"center\"><a href=\"https://github.com/neerajlovecyber\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub Repo</span></a></p></body></html>", None))
        self.dumploc_2.setHtml(QCoreApplication.translate("RawDumpTool", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'inherit'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>", None))
        self.dumploc_2.setPlaceholderText(QCoreApplication.translate("RawDumpTool", u"Select location of the File", None))
        self.selectfile.setText(QCoreApplication.translate("RawDumpTool", u"Select", None))
        self.encbtn.setText(QCoreApplication.translate("RawDumpTool", u"Encrypt", None))
        self.decbtn.setText(QCoreApplication.translate("RawDumpTool", u"Decrypt", None))
        self.checkbtn.setText(QCoreApplication.translate("RawDumpTool", u"Check", None))
#if QT_CONFIG(accessibility)
        self.linepass.setAccessibleDescription(QCoreApplication.translate("RawDumpTool", u"ss", None))
#endif // QT_CONFIG(accessibility)
        self.linepass.setPlaceholderText(QCoreApplication.translate("RawDumpTool", u"Enter Password to Encrypt/Decrypt Dump File", None))
        self.dumploc_3.setHtml(QCoreApplication.translate("RawDumpTool", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'inherit'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>", None))
        self.dumploc_3.setPlaceholderText(QCoreApplication.translate("RawDumpTool", u"Select File to Check", None))
        self.checkselect.setText(QCoreApplication.translate("RawDumpTool", u"Select", None))
        self.dumpbtn_5.setText(QCoreApplication.translate("RawDumpTool", u"Check integrity ->", None))
        self.dumpbtn_6.setText(QCoreApplication.translate("RawDumpTool", u"Encryption / Decryption", None))
        self.checkbtn_2.setText("")
        self.checkbtn_3.setText("")
        self.selectfolder.setText(QCoreApplication.translate("RawDumpTool", u"Select", None))
        self.folderlock.setHtml(QCoreApplication.translate("RawDumpTool", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'inherit'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>", None))
        self.folderlock.setPlaceholderText(QCoreApplication.translate("RawDumpTool", u"Select location to store Enc/Dec file", None))
    # retranslateUi

