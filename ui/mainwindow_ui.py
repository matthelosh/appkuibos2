# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
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
        self.pb_home = QPushButton(self.frame_toolbar)
        self.pb_home.setObjectName(u"pb_home")
        self.pb_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/receipt--exclamation.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_home.setIcon(icon)

        self.horizontalLayout.addWidget(self.pb_home)

        self.pb_load_db = QPushButton(self.frame_toolbar)
        self.pb_load_db.setObjectName(u"pb_load_db")
        self.pb_load_db.setMinimumSize(QSize(0, 0))
        self.pb_load_db.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_load_db.setStyleSheet(u"color: #555;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/document-code.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_load_db.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pb_load_db)

        self.pb_impor_bku = QPushButton(self.frame_toolbar)
        self.pb_impor_bku.setObjectName(u"pb_impor_bku")
        self.pb_impor_bku.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_impor_bku.setStyleSheet(u"color: #555;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_impor_bku.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pb_impor_bku)

        self.horizontalSpacer = QSpacerItem(654, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_setting = QPushButton(self.frame_toolbar)
        self.pb_setting.setObjectName(u"pb_setting")
        self.pb_setting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/calculator-gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_setting.setIcon(icon3)
        self.pb_setting.setFlat(True)

        self.horizontalLayout.addWidget(self.pb_setting)


        self.verticalLayout_2.addWidget(self.frame_toolbar)

        self.frame_main = QFrame(self.frame)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"background-color: white;")
        self.frame_main.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_main.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"color: #555;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(50, 20, 50, 20)
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.textBrowser = QTextBrowser(self.page_home)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_5.addWidget(self.textBrowser)

        self.stackedWidget.addWidget(self.page_home)
        self.page_bku = QWidget()
        self.page_bku.setObjectName(u"page_bku")
        self.page_bku.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page_bku)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.frame_2 = QFrame(self.page_bku)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_table_tool = QFrame(self.frame_2)
        self.frame_table_tool.setObjectName(u"frame_table_tool")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_table_tool.sizePolicy().hasHeightForWidth())
        self.frame_table_tool.setSizePolicy(sizePolicy)
        self.frame_table_tool.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_table_tool.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_table_tool)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_table_tool)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_table_tool)

        self.frame_filter = QFrame(self.frame_2)
        self.frame_filter.setObjectName(u"frame_filter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_filter.sizePolicy().hasHeightForWidth())
        self.frame_filter.setSizePolicy(sizePolicy1)
        self.frame_filter.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_filter.setFrameShadow(QFrame.Shadow.Plain)
        self.formLayout = QFormLayout(self.frame_filter)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.label_3 = QLabel(self.frame_filter)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.le_search = QLineEdit(self.frame_filter)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setStyleSheet(u"padding: 4px 6px;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.le_search)


        self.horizontalLayout_2.addWidget(self.frame_filter)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.tableWidget = QTableWidget(self.page_bku)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page_bku)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame_main)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 24))
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aplikasi Kuitansi BOS", None))
        self.act_impor_nku.setText(QCoreApplication.translate("MainWindow", u"Impor BKU", None))
        self.act_load_db.setText(QCoreApplication.translate("MainWindow", u"Load Database", None))
        self.act_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.act_id_sekolah.setText(QCoreApplication.translate("MainWindow", u"Identitas Sekolah", None))
        self.pb_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pb_load_db.setText(QCoreApplication.translate("MainWindow", u"Load DB", None))
        self.pb_impor_bku.setText(QCoreApplication.translate("MainWindow", u"Impor BKU", None))
#if QT_CONFIG(tooltip)
        self.pb_setting.setToolTip(QCoreApplication.translate("MainWindow", u"Pengaturan Sekolah", None))
#endif // QT_CONFIG(tooltip)
        self.pb_setting.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Aplikasi Cetak Kuitansi BOS", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Alhamdulillah, dengan gembira telah diluncurkan aplikasi yang dapat membantu operator dan bendahara BOS di lembaga sekolah unutk mencetak kuitansi. Guna memudahkan dalam pembuatan laporan pertanggung jawaban penggunaan dana BOS di lembaga sekolah.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Aplikasi ini memiliki berbagai fitur yang berguna. Pengguna dapat mengekstrak data transaksi dari file BKU yang berupa pdf dari aplikasi ARKAS 4.0 menjadi data yang ditampilkan dalam tabel. Pengguna dapat mencetak kuitansi dari data tersebut. Selain dicetak, dat tersebut juga dapat disimpan ke database unutk digunakan lagi.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Kedepannya, pengguna juga dapat menambahkan bukti transaksi berupa nota, foto barang dan lainnya sehingga lebih terorga"
                        "nisir dan mudah dalam pembuatan laporan.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Semoga aplikasi ini dapat bermanfaat.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tabel Transaksi", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Filter:", None))
        self.le_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cari..", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kode Kegiatan", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Kode Kegiatan", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"No. Bukti", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nominal", None));
        self.menuBerkas.setTitle(QCoreApplication.translate("MainWindow", u"Berkas", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

