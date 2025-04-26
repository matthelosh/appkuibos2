# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formsekolahxGTchy.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogSekolah(object):
    def setupUi(self, DialogSekolah):
        if not DialogSekolah.objectName():
            DialogSekolah.setObjectName(u"DialogSekolah")
        DialogSekolah.resize(700, 640)
        DialogSekolah.setMinimumSize(QSize(650, 600))
        DialogSekolah.setMaximumSize(QSize(700, 640))
        self.verticalLayout = QVBoxLayout(DialogSekolah)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DialogSekolah)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(DialogSekolah)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.formLayout_2.setVerticalSpacing(15)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self._npsn = QLineEdit(self.frame_3)
        self._npsn.setObjectName(u"_npsn")
        self._npsn.setMinimumSize(QSize(0, 30))

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self._npsn)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self._alamat = QLineEdit(self.frame_3)
        self._alamat.setObjectName(u"_alamat")
        self._alamat.setMinimumSize(QSize(0, 30))

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self._alamat)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_6)

        self._kode_pos = QLineEdit(self.frame_3)
        self._kode_pos.setObjectName(u"_kode_pos")
        self._kode_pos.setMinimumSize(QSize(0, 30))

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self._kode_pos)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_10)

        self._kabupaten = QLineEdit(self.frame_3)
        self._kabupaten.setObjectName(u"_kabupaten")
        self._kabupaten.setMinimumSize(QSize(0, 30))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self._kabupaten)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_11)

        self._email = QLineEdit(self.frame_3)
        self._email.setObjectName(u"_email")
        self._email.setMinimumSize(QSize(0, 30))

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self._email)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_5 = QFormLayout(self.frame_8)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_5.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.formLayout_5.setVerticalSpacing(15)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self._nama_sekolah = QLineEdit(self.frame_8)
        self._nama_sekolah.setObjectName(u"_nama_sekolah")
        self._nama_sekolah.setMinimumSize(QSize(0, 30))

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self._nama_sekolah)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_7)

        self._desa = QLineEdit(self.frame_8)
        self._desa.setObjectName(u"_desa")
        self._desa.setMinimumSize(QSize(0, 30))

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self._desa)

        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_8)

        self._kecamatan = QLineEdit(self.frame_8)
        self._kecamatan.setObjectName(u"_kecamatan")
        self._kecamatan.setMinimumSize(QSize(0, 30))

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self._kecamatan)

        self.label_21 = QLabel(self.frame_8)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_21)

        self._telp = QLineEdit(self.frame_8)
        self._telp.setObjectName(u"_telp")
        self._telp.setMinimumSize(QSize(0, 30))

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.FieldRole, self._telp)

        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_5.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_22)

        self._website = QLineEdit(self.frame_8)
        self._website.setObjectName(u"_website")
        self._website.setMinimumSize(QSize(0, 30))

        self.formLayout_5.setWidget(4, QFormLayout.ItemRole.FieldRole, self._website)


        self.horizontalLayout.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame)

        self.label_12 = QLabel(DialogSekolah)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"margin-top: 10px;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.frame_4 = QFrame(DialogSekolah)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.formLayout_3 = QFormLayout(self.frame_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_13)

        self._ks = QLineEdit(self.frame_5)
        self._ks.setObjectName(u"_ks")
        self._ks.setMinimumSize(QSize(0, 30))

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self._ks)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_15)

        self._pangkat_ks = QLineEdit(self.frame_5)
        self._pangkat_ks.setObjectName(u"_pangkat_ks")
        self._pangkat_ks.setMinimumSize(QSize(0, 30))

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self._pangkat_ks)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_16)

        self._nip_ks = QLineEdit(self.frame_5)
        self._nip_ks.setObjectName(u"_nip_ks")
        self._nip_ks.setMinimumSize(QSize(0, 30))

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self._nip_ks)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.formLayout_4 = QFormLayout(self.frame_6)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_4.setVerticalSpacing(-1)
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_20)

        self._bendahara = QLineEdit(self.frame_6)
        self._bendahara.setObjectName(u"_bendahara")
        self._bendahara.setMinimumSize(QSize(0, 30))

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self._bendahara)

        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_19)

        self._pangkat_bendahara = QLineEdit(self.frame_6)
        self._pangkat_bendahara.setObjectName(u"_pangkat_bendahara")
        self._pangkat_bendahara.setMinimumSize(QSize(0, 30))

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self._pangkat_bendahara)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_17)

        self._nip_bendahara = QLineEdit(self.frame_6)
        self._nip_bendahara.setObjectName(u"_nip_bendahara")
        self._nip_bendahara.setMinimumSize(QSize(0, 30))

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self._nip_bendahara)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_7 = QFrame(DialogSekolah)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(484, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pb_cancel = QPushButton(self.frame_7)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.pb_cancel)

        self.pb_simpan = QPushButton(self.frame_7)
        self.pb_simpan.setObjectName(u"pb_simpan")

        self.horizontalLayout_3.addWidget(self.pb_simpan)


        self.verticalLayout.addWidget(self.frame_7)

        QWidget.setTabOrder(self._npsn, self._nama_sekolah)
        QWidget.setTabOrder(self._nama_sekolah, self._alamat)
        QWidget.setTabOrder(self._alamat, self._desa)
        QWidget.setTabOrder(self._desa, self._kode_pos)
        QWidget.setTabOrder(self._kode_pos, self._kecamatan)
        QWidget.setTabOrder(self._kecamatan, self._kabupaten)
        QWidget.setTabOrder(self._kabupaten, self._telp)
        QWidget.setTabOrder(self._telp, self._email)
        QWidget.setTabOrder(self._email, self._website)
        QWidget.setTabOrder(self._website, self._ks)
        QWidget.setTabOrder(self._ks, self._pangkat_ks)
        QWidget.setTabOrder(self._pangkat_ks, self._nip_ks)
        QWidget.setTabOrder(self._nip_ks, self._bendahara)
        QWidget.setTabOrder(self._bendahara, self._pangkat_bendahara)
        QWidget.setTabOrder(self._pangkat_bendahara, self._nip_bendahara)
        QWidget.setTabOrder(self._nip_bendahara, self.pb_cancel)
        QWidget.setTabOrder(self.pb_cancel, self.pb_simpan)

        self.retranslateUi(DialogSekolah)

        self.pb_simpan.setDefault(True)


        QMetaObject.connectSlotsByName(DialogSekolah)
    # setupUi

    def retranslateUi(self, DialogSekolah):
        DialogSekolah.setWindowTitle(QCoreApplication.translate("DialogSekolah", u"Data Sekolah", None))
        self.label.setText(QCoreApplication.translate("DialogSekolah", u"Data Sekolah", None))
        self.label_3.setText(QCoreApplication.translate("DialogSekolah", u"NPSN", None))
        self.label_5.setText(QCoreApplication.translate("DialogSekolah", u"Alamat", None))
        self.label_6.setText(QCoreApplication.translate("DialogSekolah", u"Kode Pos", None))
        self.label_10.setText(QCoreApplication.translate("DialogSekolah", u"Kab/Kota", None))
        self.label_11.setText(QCoreApplication.translate("DialogSekolah", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("DialogSekolah", u"Nama Sekolah", None))
        self.label_7.setText(QCoreApplication.translate("DialogSekolah", u"Desa/Kelurahan", None))
        self.label_8.setText(QCoreApplication.translate("DialogSekolah", u"Kecamatan", None))
        self.label_21.setText(QCoreApplication.translate("DialogSekolah", u"No. Telepon", None))
        self.label_22.setText(QCoreApplication.translate("DialogSekolah", u"Website", None))
        self.label_12.setText(QCoreApplication.translate("DialogSekolah", u"Penanggung Jawab", None))
        self.label_13.setText(QCoreApplication.translate("DialogSekolah", u"Kepala Sekolah", None))
        self.label_15.setText(QCoreApplication.translate("DialogSekolah", u"Pangkat", None))
        self.label_16.setText(QCoreApplication.translate("DialogSekolah", u"NIP", None))
        self.label_20.setText(QCoreApplication.translate("DialogSekolah", u"Bendahara", None))
        self.label_19.setText(QCoreApplication.translate("DialogSekolah", u"Pangkat", None))
        self.label_17.setText(QCoreApplication.translate("DialogSekolah", u"NIP", None))
        self.pb_cancel.setText(QCoreApplication.translate("DialogSekolah", u"Batal", None))
        self.pb_simpan.setText(QCoreApplication.translate("DialogSekolah", u"Simpan", None))
    # retranslateUi

