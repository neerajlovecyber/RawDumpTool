# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingdailog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)
import res_rc

class Ui_loaddailog(object):
    def setupUi(self, loaddailog):
        if not loaddailog.objectName():
            loaddailog.setObjectName(u"loaddailog")
        loaddailog.setWindowModality(Qt.NonModal)
        loaddailog.resize(400, 300)
        loaddailog.setMinimumSize(QSize(400, 300))
        loaddailog.setMaximumSize(QSize(400, 300))
        font = QFont()
        font.setBold(False)
        loaddailog.setFont(font)
        loaddailog.setModal(True)
        self.label = QLabel(loaddailog)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(90, 200, 241, 31))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label_2 = QLabel(loaddailog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 40, 151, 131))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"loadlogo.png")
        self.label_2.setPixmap(QPixmap(u"icons/loadlogo.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(loaddailog)

        QMetaObject.connectSlotsByName(loaddailog)
    # setupUi

    def retranslateUi(self, loaddailog):
        loaddailog.setWindowTitle(QCoreApplication.translate("loaddailog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("loaddailog", u"Memory dump Created", None))
        self.label_2.setText("")
    # retranslateUi

