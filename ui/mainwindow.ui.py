# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowSkYTcw.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(988, 698)
        MainWindow.setStyleSheet(u"QWidget QPushButton {\n"
"\n"
"}")
        self.act_impor_nku = QAction(MainWindow)
        self.act_impor_nku.setObjectName(u"act_impor_nku")
        self.act_load_db = QAction(MainWindow)
        self.act_load_db.setObjectName(u"act_load_db")
        self.act_close = QAction(MainWindow)
        self.act_close.setObjectName(u"act_close")
        self.act_id_sekolah = QAction(MainWindow)
        self.act_id_sekolah.setObjectName(u"act_id_sekolah")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_toolbar = QFrame(self.frame)
        self.frame_toolbar.setObjectName(u"frame_toolbar")
        self.frame_toolbar.setMaximumSize(QSize(16777215, 50))
        self.frame_toolbar.setStyleSheet(u"QWidget #frame_toolbar {\n"
"	background-color: rgb(225, 251, 255)\n"
"}")
        self.frame_toolbar.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_toolbar.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_toolbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_load_db = QPushButton(self.frame_toolbar)
        self.pb_load_db.setObjectName(u"pb_load_db")
        self.pb_load_db.setMinimumSize(QSize(0, 0))
        self.pb_load_db.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_load_db.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_load_db.setIcon(icon)

        self.horizontalLayout.addWidget(self.pb_load_db)

        self.pb_impor_bku = QPushButton(self.frame_toolbar)
        self.pb_impor_bku.setObjectName(u"pb_impor_bku")
        self.pb_impor_bku.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_impor_bku.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pb_impor_bku)

        self.horizontalSpacer = QSpacerItem(654, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_setting = QPushButton(self.frame_toolbar)
        self.pb_setting.setObjectName(u"pb_setting")
        self.pb_setting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cogwheel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_setting.setIcon(icon2)
        self.pb_setting.setFlat(True)

        self.horizontalLayout.addWidget(self.pb_setting)


        self.verticalLayout_2.addWidget(self.frame_toolbar)

        self.frame_main = QFrame(self.frame)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"background-color: white;")
        self.frame_main.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_main.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.frame_main)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 988, 24))
        self.menuBerkas = QMenu(self.menubar)
        self.menuBerkas.setObjectName(u"menuBerkas")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuBerkas.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuBerkas.addAction(self.act_impor_nku)
        self.menuBerkas.addAction(self.act_load_db)
        self.menuBerkas.addSeparator()
        self.menuBerkas.addAction(self.act_close)
        self.menuTools.addAction(self.act_id_sekolah)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aplikasi Keren", None))
        self.act_impor_nku.setText(QCoreApplication.translate("MainWindow", u"Impor BKU", None))
        self.act_load_db.setText(QCoreApplication.translate("MainWindow", u"Load Database", None))
        self.act_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.act_id_sekolah.setText(QCoreApplication.translate("MainWindow", u"Identitas Sekolah", None))
        self.pb_load_db.setText(QCoreApplication.translate("MainWindow", u"Load DB", None))
        self.pb_impor_bku.setText(QCoreApplication.translate("MainWindow", u"Impor BKU", None))
#if QT_CONFIG(tooltip)
        self.pb_setting.setToolTip(QCoreApplication.translate("MainWindow", u"Pengaturan Sekolah", None))
#endif // QT_CONFIG(tooltip)
        self.pb_setting.setText("")
        self.menuBerkas.setTitle(QCoreApplication.translate("MainWindow", u"Berkas", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

