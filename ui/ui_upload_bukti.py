# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload_bukti.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogUploadBukti(object):
    def setupUi(self, DialogUploadBukti):
        if not DialogUploadBukti.objectName():
            DialogUploadBukti.setObjectName(u"DialogUploadBukti")
        DialogUploadBukti.resize(500, 600)
        DialogUploadBukti.setWindowTitle("Upload Bukti Transaksi")
        
        self.verticalLayout = QVBoxLayout(DialogUploadBukti)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Title
        self.label_title = QLabel(DialogUploadBukti)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setText("Upload Bukti Transaksi")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_title)
        
        # Form layout for transaction info
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        
        # No Bukti (read-only)
        self.label_no_bukti = QLabel(DialogUploadBukti)
        self.label_no_bukti.setObjectName(u"label_no_bukti")
        self.label_no_bukti.setText("No. Bukti:")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_no_bukti)
        
        self.label_no_bukti_value = QLabel(DialogUploadBukti)
        self.label_no_bukti_value.setObjectName(u"label_no_bukti_value")
        self.label_no_bukti_value.setStyleSheet("font-weight: bold; color: #2196F3;")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_no_bukti_value)
        
        # Uraian (read-only)
        self.label_uraian = QLabel(DialogUploadBukti)
        self.label_uraian.setObjectName(u"label_uraian")
        self.label_uraian.setText("Uraian:")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_uraian)
        
        self.label_uraian_value = QLabel(DialogUploadBukti)
        self.label_uraian_value.setObjectName(u"label_uraian_value")
        self.label_uraian_value.setWordWrap(True)
        self.label_uraian_value.setStyleSheet("font-weight: bold; color: #333;")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_uraian_value)
        
        self.verticalLayout.addLayout(self.formLayout)
        
        # Upload section
        self.label_upload = QLabel(DialogUploadBukti)
        self.label_upload.setObjectName(u"label_upload")
        self.label_upload.setText("Bukti Pelaksanaan:")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_upload.setFont(font2)
        self.verticalLayout.addWidget(self.label_upload)
        
        # Upload button
        self.pushButton_browse = QPushButton(DialogUploadBukti)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setText("📁 Pilih File Gambar")
        self.pushButton_browse.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px 20px;
                font-weight: bold;
                border-radius: 4px;
                margin: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.verticalLayout.addWidget(self.pushButton_browse)
        
        # Image preview area
        self.scrollArea = QScrollArea(DialogUploadBukti)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 300))
        self.scrollArea.setStyleSheet("""
            QScrollArea {
                border: 2px dashed #ccc;
                border-radius: 8px;
                background-color: #f9f9f9;
            }
        """)
        self.scrollArea.setWidgetResizable(True)
        
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 494, 298))
        
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.label_preview = QLabel(self.scrollAreaWidgetContents)
        self.label_preview.setObjectName(u"label_preview")
        self.label_preview.setText("Belum ada gambar dipilih")
        self.label_preview.setAlignment(Qt.AlignCenter)
        self.label_preview.setStyleSheet("""
            QLabel {
                color: #666;
                font-style: italic;
                padding: 20px;
            }
        """)
        self.label_preview.setMinimumSize(QSize(0, 280))
        self.verticalLayout_2.addWidget(self.label_preview)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        
        # File info
        self.label_file_info = QLabel(DialogUploadBukti)
        self.label_file_info.setObjectName(u"label_file_info")
        self.label_file_info.setText("")
        self.label_file_info.setStyleSheet("color: #666; font-size: 11px; margin: 5px;")
        self.verticalLayout.addWidget(self.label_file_info)
        
        # Spacer
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        
        # Button layout
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.pushButton_remove = QPushButton(DialogUploadBukti)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setText("🗑️ Hapus Bukti")
        self.pushButton_remove.setEnabled(False)
        self.pushButton_remove.setStyleSheet("""
            QPushButton {
                background-color: #ff9800;
                color: white;
                border: none;
                padding: 10px 20px;
                font-weight: bold;
                border-radius: 4px;
                margin: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #f57c00;
            }
            QPushButton:disabled {
                background-color: #ccc;
                color: #666;
            }
        """)
        self.horizontalLayout.addWidget(self.pushButton_remove)
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)
        
        self.pushButton_cancel = QPushButton(DialogUploadBukti)
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
        
        self.pushButton_save = QPushButton(DialogUploadBukti)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setText("Simpan")
        self.pushButton_save.setEnabled(False)
        self.pushButton_save.setStyleSheet("""
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
            QPushButton:disabled {
                background-color: #ccc;
                color: #666;
            }
        """)
        self.horizontalLayout.addWidget(self.pushButton_save)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        QMetaObject.connectSlotsByName(DialogUploadBukti)
    # setupUi

    def retranslateUi(self, DialogUploadBukti):
        pass
    # retranslateUi
