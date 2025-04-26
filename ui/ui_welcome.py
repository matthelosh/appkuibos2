# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomezPbSxc.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DialogWelcome(object):
    def setupUi(self, DialogWelcome):
        if not DialogWelcome.objectName():
            DialogWelcome.setObjectName(u"DialogWelcome")
        DialogWelcome.resize(600, 500)
        DialogWelcome.setMinimumSize(QSize(600, 500))
        DialogWelcome.setMaximumSize(QSize(600, 500))
        DialogWelcome.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(DialogWelcome)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(DialogWelcome)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(600, 500))
        self.main_frame.setMaximumSize(QSize(600, 500))
        self.main_frame.setStyleSheet(u"QWidget #main_frame {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(105, 216, 255, 255), stop:1 rgba(212, 213, 255, 255));}")
        self.main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.main_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(234, 252, 255)")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 200))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(40)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(250,255,255);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.progressBar = QProgressBar(self.main_frame)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.frame_bottom = QFrame(self.main_frame)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(600, 40))
        self.frame_bottom.setMaximumSize(QSize(600, 40))
        self.frame_bottom.setStyleSheet(u"QWidget #frame_bottom {\n"
"border-top: 1px solid #fff;\n"
"}")
        self.frame_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frame_bottom)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #5699ff;")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(222, 11, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.frame_bottom)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #5699ff;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout_3.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.main_frame)


        self.retranslateUi(DialogWelcome)

        QMetaObject.connectSlotsByName(DialogWelcome)
    # setupUi

    def retranslateUi(self, DialogWelcome):
        DialogWelcome.setWindowTitle(QCoreApplication.translate("DialogWelcome", u"Welcome", None))
        self.label.setText(QCoreApplication.translate("DialogWelcome", u"Selamat Datang!", None))
        self.label_2.setText(QCoreApplication.translate("DialogWelcome", u"Aplikasi Kuitansi\n"
"BOS", None))
        self.label_4.setText(QCoreApplication.translate("DialogWelcome", u"\u00a9 2025 mathelosh <matthelosh@gmail.com>", None))
        self.label_5.setText(QCoreApplication.translate("DialogWelcome", u"Versi 0.1.1", None))
    # retranslateUi

