# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_year.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogSelectYear(object):
    def setupUi(self, DialogSelectYear):
        if not DialogSelectYear.objectName():
            DialogSelectYear.setObjectName(u"DialogSelectYear")
        DialogSelectYear.resize(350, 200)
        DialogSelectYear.setWindowTitle("Pilih Tahun Database")
        
        self.verticalLayout = QVBoxLayout(DialogSelectYear)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Title
        self.label_title = QLabel(DialogSelectYear)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setText("Pilih Tahun Database")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_title)
        
        # Description
        self.label_description = QLabel(DialogSelectYear)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setText("Pilih tahun anggaran untuk database transaksi BKU:")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_description.setWordWrap(True)
        self.label_description.setStyleSheet("color: #666; margin: 10px;")
        self.verticalLayout.addWidget(self.label_description)
        
        # Form layout
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        
        # Year selection
        self.label_year = QLabel(DialogSelectYear)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setText("Tahun:")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_year)
        
        self.comboBox_year = QComboBox(DialogSelectYear)
        self.comboBox_year.setObjectName(u"comboBox_year")
        self.comboBox_year.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid #4CAF50;
                border-radius: 4px;
                padding: 8px 12px;
                font-size: 14px;
                font-weight: bold;
            }
            QComboBox:hover {
                border-color: #45a049;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: none;
                border: none;
                width: 0px;
                height: 0px;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #4CAF50;
            }
        """)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_year)
        
        self.verticalLayout.addLayout(self.formLayout)
        
        # Info label
        self.label_info = QLabel(DialogSelectYear)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setText("")
        self.label_info.setStyleSheet("color: #2196F3; font-style: italic; margin: 5px;")
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_info.setWordWrap(True)
        self.verticalLayout.addWidget(self.label_info)
        
        # Spacer
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        
        # Button layout
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)
        
        self.pushButton_cancel = QPushButton(DialogSelectYear)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setText("Batal")
        self.pushButton_cancel.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 10px 20px;
                font-weight: bold;
                border-radius: 4px;
                margin: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        
        self.pushButton_select = QPushButton(DialogSelectYear)
        self.pushButton_select.setObjectName(u"pushButton_select")
        self.pushButton_select.setText("Pilih")
        self.pushButton_select.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-weight: bold;
                border-radius: 4px;
                margin: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.horizontalLayout.addWidget(self.pushButton_select)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        QMetaObject.connectSlotsByName(DialogSelectYear)
    # setupUi

    def retranslateUi(self, DialogSelectYear):
        pass
    # retranslateUi
