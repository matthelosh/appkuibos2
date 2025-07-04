# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_bku.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogEditBku(object):
    def setupUi(self, DialogEditBku):
        if not DialogEditBku.objectName():
            DialogEditBku.setObjectName(u"DialogEditBku")
        DialogEditBku.resize(400, 300)
        DialogEditBku.setWindowTitle("Edit BKU")
        
        self.verticalLayout = QVBoxLayout(DialogEditBku)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Title
        self.label_title = QLabel(DialogEditBku)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setText("Edit Data BKU")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_title)
        
        # Form layout
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        
        # No Bukti (read-only)
        self.label_no_bukti = QLabel(DialogEditBku)
        self.label_no_bukti.setObjectName(u"label_no_bukti")
        self.label_no_bukti.setText("No. Bukti:")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_no_bukti)
        
        self.lineEdit_no_bukti = QLineEdit(DialogEditBku)
        self.lineEdit_no_bukti.setObjectName(u"lineEdit_no_bukti")
        self.lineEdit_no_bukti.setReadOnly(True)
        self.lineEdit_no_bukti.setStyleSheet("background-color: #f0f0f0;")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_no_bukti)
        
        # Tanggal (read-only)
        self.label_tanggal = QLabel(DialogEditBku)
        self.label_tanggal.setObjectName(u"label_tanggal")
        self.label_tanggal.setText("Tanggal:")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_tanggal)
        
        self.lineEdit_tanggal = QLineEdit(DialogEditBku)
        self.lineEdit_tanggal.setObjectName(u"lineEdit_tanggal")
        self.lineEdit_tanggal.setReadOnly(True)
        self.lineEdit_tanggal.setStyleSheet("background-color: #f0f0f0;")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_tanggal)
        
        # Uraian (read-only)
        self.label_uraian = QLabel(DialogEditBku)
        self.label_uraian.setObjectName(u"label_uraian")
        self.label_uraian.setText("Uraian:")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_uraian)
        
        self.lineEdit_uraian = QLineEdit(DialogEditBku)
        self.lineEdit_uraian.setObjectName(u"lineEdit_uraian")
        self.lineEdit_uraian.setReadOnly(True)
        self.lineEdit_uraian.setStyleSheet("background-color: #f0f0f0;")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_uraian)
        
        # Nilai (read-only)
        self.label_nilai = QLabel(DialogEditBku)
        self.label_nilai.setObjectName(u"label_nilai")
        self.label_nilai.setText("Nilai:")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_nilai)
        
        self.lineEdit_nilai = QLineEdit(DialogEditBku)
        self.lineEdit_nilai.setObjectName(u"lineEdit_nilai")
        self.lineEdit_nilai.setReadOnly(True)
        self.lineEdit_nilai.setStyleSheet("background-color: #f0f0f0;")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_nilai)
        
        # Penerima (editable)
        self.label_penerima = QLabel(DialogEditBku)
        self.label_penerima.setObjectName(u"label_penerima")
        self.label_penerima.setText("Penerima:")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_penerima)
        
        self.lineEdit_penerima = QLineEdit(DialogEditBku)
        self.lineEdit_penerima.setObjectName(u"lineEdit_penerima")
        self.lineEdit_penerima.setStyleSheet("background-color: white; border: 2px solid #4CAF50;")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_penerima)
        
        self.verticalLayout.addLayout(self.formLayout)
        
        # Spacer
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        
        # Button layout
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)
        
        self.pushButton_cancel = QPushButton(DialogEditBku)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setText("Batal")
        self.pushButton_cancel.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 8px 16px;
                font-weight: bold;
                border-radius: 4px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        
        self.pushButton_save = QPushButton(DialogEditBku)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setText("Simpan")
        self.pushButton_save.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                font-weight: bold;
                border-radius: 4px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.horizontalLayout.addWidget(self.pushButton_save)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        QMetaObject.connectSlotsByName(DialogEditBku)
    # setupUi

    def retranslateUi(self, DialogEditBku):
        pass
    # retranslateUi
