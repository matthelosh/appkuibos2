import sys
import time
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QDialog,
    QMessageBox,
    QFileDialog,
    QTableWidgetItem,
    QLabel,
    QHeaderView,
    QPushButton,
    QHBoxLayout,
    QProgressBar
)
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from ui.ui_welcome import Ui_DialogWelcome
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_formsekolah import Ui_DialogSekolah
import ui.resources_rc
import time

from modules.sekolah import saveIdentitas, getIdentitas
from modules.config import getAnggaran
from modules.db import Db
from modules.utils import extractTable
from modules.print import cetakTransaksi, cetakSemuaTransaksi
from modules.print_docx import cetakTransaksiDocx, cetakSemuaTransaksiDocx

app = QApplication(sys.argv)

class SplashScreen(QDialog):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.ui = Ui_DialogWelcome()
        self.ui.setupUi(self)

        self.progress = 0
        self.ui.progressBar.setValue(self.progress)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(30)

    def update_progress(self):
        self.progress += 1
        self.ui.progressBar.setValue(self.progress)

        if self.progress >= 100:
            self.timer.stop()
            self.accept()

class DialogSekolah(QDialog):
    def __init__(self):
        super(DialogSekolah, self).__init__()
        self.ui = Ui_DialogSekolah()
        self.ui.setupUi(self)
        self.ui.pb_cancel.clicked.connect(self.closeMe)
        self.ui.pb_simpan.clicked.connect(self.saveDataSekolah)
        self.loadDataSekolah()

    def closeMe(self):
        self.reject()

    def loadDataSekolah(self):
        data = getIdentitas()
        if data:
            self.ui._npsn.setText(data["npsn"])
            self.ui._nama_sekolah.setText(data["sekolah"])
            self.ui._alamat.setText(data["alamat"])
            self.ui._kode_pos.setText(data["kode_pos"])
            self.ui._kabupaten.setText(data["kabupaten"])
            self.ui._email.setText(data["email"])
            self.ui._desa.setText(data["desa"])
            self.ui._kecamatan.setText(data["kecamatan"])
            self.ui._telp.setText(data["telp"])
            self.ui._website.setText(data["website"])
            self.ui._ks.setText(data["ks"])
            self.ui._pangkat_ks.setText(data["pangkat_ks"])
            self.ui._nip_ks.setText(data["nip_ks"])
            self.ui._bendahara.setText(data["bendahara"])
            self.ui._pangkat_bendahara.setText(data["pangkat_bendahara"])
            self.ui._nip_bendahara.setText(data["nip_bendahara"])

    def saveDataSekolah(self):
        self.npsn               = self.ui._npsn.text()
        self.sekolah            = self.ui._nama_sekolah.text()
        self.alamat             = self.ui._alamat.text()
        self.kode_pos           = self.ui._kode_pos.text()
        self.kabupaten          = self.ui._kabupaten.text()
        self.email              = self.ui._email.text()
        self.desa               = self.ui._desa.text()
        self.kecamatan          = self.ui._kecamatan.text()
        self.telp               = self.ui._telp.text()
        self.website            = self.ui._website.text()
        self.ks                 = self.ui._ks.text()
        self.pangkat_ks         = self.ui._pangkat_ks.text()
        self.nip_ks             = self.ui._nip_ks.text()
        self.bendahara          = self.ui._bendahara.text()
        self.pangkat_bendahara  = self.ui._pangkat_bendahara.text()
        self.nip_bendahara      = self.ui._nip_bendahara.text()
        result = saveIdentitas(
            npsn=self.npsn,
            sekolah=self.sekolah,
            alamat=self.alamat,
            desa=self.desa,
            kecamatan=self.kecamatan,
            kode_pos=self.kode_pos,
            kabupaten=self.kabupaten,
            telp=self.telp,
            email=self.email,
            website=self.website,
            ks=self.ks,
            pangkat_ks=self.pangkat_ks,
            nip_ks=self.nip_ks,
            bendahara=self.bendahara,
            pangkat_bendahara=self.pangkat_bendahara,
            nip_bendahara=self.nip_bendahara
        )
        if result:
            # QMessageBox.information(self, "Info", result[])
            # print(result)
            self.accept()
        else:
            self.reject()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Aplikasi Cetak Kuitansi BOS v0.1.1")
        self.bkus = []
        self.anggaran = getAnggaran()
        #Menu Bar Action
        self.ui.act_close.triggered.connect(closeApp)
        self.ui.act_impor_nku.triggered.connect(self.imporBku)
        self.ui.act_load_db.triggered.connect(self.loadDB)
        self.ui.act_id_sekolah.triggered.connect(self.showDialogSekolah)

        # Button
        self.ui.pb_home.clicked.connect(self.toHome)
        self.ui.pb_home.setStyleSheet("color: #555")
        self.ui.pb_load_db.setText("Lihat Transaksi")
        self.ui.pb_load_db.clicked.connect(self.loadDB)
        self.ui.pb_impor_bku.clicked.connect(self.imporBku)
        self.ui.pb_setting.clicked.connect(self.showDialogSekolah)

        # Status Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.progress_bar.hide()
        self.status_label = QLabel("Idle.")
        self.statusBar().addWidget(self.status_label)

        #Filter
        self.ui.le_search.textChanged.connect(self.filterTable)

    def toHome(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def imporBku(self):
        # self.bkus.append("bku01")
        file_bku, _ = QFileDialog.getOpenFileName(self, "Pilih file BKU:", "", "PDF (*.pdf)")
        table = self.ui.tableWidget
        if file_bku:
            # print("File dipilih:", file_bku)
            # Show progress bar
            self.progress_bar.show()
            self.progress_bar.setValue(0)
            
            # Define progress callback
            def progress_callback(message, value):
                self.status_label.setText(message)
                self.progress_bar.setValue(value)
                QApplication.processEvents()  # Update UI immediately
            
            # Extract table with progress callback
            transaksis = extractTable(file_bku, progress_callback)
            
            # Store transaksis in instance variable for later use
            self.current_transaksis = transaksis
            
            # Add "Cetak Semua" buttons above the table
            if not hasattr(self.ui, 'btn_cetak_semua_html'):
                # Create container widget for buttons
                self.ui.cetak_semua_container = QWidget()
                container_layout = QHBoxLayout()
                
                # HTML Print All button
                self.ui.btn_cetak_semua_html = QPushButton("📄 Cetak Semua HTML")
                self.ui.btn_cetak_semua_html.setStyleSheet("""
                    QPushButton {
                        background-color: #2196F3;
                        color: white;
                        border: none;
                        padding: 8px 16px;
                        font-weight: bold;
                        border-radius: 4px;
                        margin: 5px;
                    }
                    QPushButton:hover {
                        background-color: #1976D2;
                    }
                """)
                
                # DOCX Print All button
                self.ui.btn_cetak_semua_docx = QPushButton("📝 Cetak Semua DOCX")
                self.ui.btn_cetak_semua_docx.setStyleSheet("""
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
                
                container_layout.addWidget(self.ui.btn_cetak_semua_html)
                container_layout.addWidget(self.ui.btn_cetak_semua_docx)
                container_layout.addStretch()  # Push buttons to left
                self.ui.cetak_semua_container.setLayout(container_layout)
                
                # Insert container before table in the layout
                layout = self.ui.page_bku.layout()
                if layout:
                    layout.insertWidget(1, self.ui.cetak_semua_container)
            
            # Clear previous connections safely and connect buttons
            try:
                self.ui.btn_cetak_semua_html.clicked.disconnect()
                self.ui.btn_cetak_semua_docx.clicked.disconnect()
            except:
                pass  # No connections to disconnect
            
            self.ui.btn_cetak_semua_html.clicked.connect(lambda: cetakSemuaTransaksi(self, self.current_transaksis))
            self.ui.btn_cetak_semua_docx.clicked.connect(lambda: cetakSemuaTransaksiDocx(self, self.current_transaksis))
            self.ui.btn_cetak_semua_html.setText(f"📄 Cetak Semua HTML ({len(transaksis)} transaksi)")
            self.ui.btn_cetak_semua_docx.setText(f"📝 Cetak Semua DOCX ({len(transaksis)} transaksi)")
            self.ui.cetak_semua_container.show()
            
            headers = list(transaksis[0].keys())
            headers.append('opsi')
            table.setColumnCount(8)
            table.setRowCount(len(transaksis))
            table.setHorizontalHeaderLabels(["TANGGAL", "KODE KEGIATAN", "KODE REKENING", "NO. BUKTI", "URAIAN", "NOMINAL", "PENERIMA", "OPSI"])

            for row_idx, data in enumerate(transaksis):
                for col_idx, key in enumerate(headers):
                    if col_idx == 4:
                        label = QLabel(data.get('uraian', ''))
                        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                        label.setWordWrap(True)
                        label.setStyleSheet("padding: 6px")
                        table.setCellWidget(row_idx, col_idx, label)
                    elif col_idx == 7:
                        btn_edit = QPushButton("Edit")
                        btn_print_html = QPushButton("📄 HTML")
                        btn_print_docx = QPushButton("📝 DOCX")
                        btn_edit.clicked.connect(lambda _, data=transaksis[row_idx]: self.editTransaksi(data))
                        btn_print_html.clicked.connect(lambda _, data=transaksis[row_idx]: cetakTransaksi(self, data))
                        btn_print_docx.clicked.connect(lambda _, data=transaksis[row_idx]: cetakTransaksiDocx(self, data))
                        cell_widget = QWidget()
                        layout = QHBoxLayout()
                        layout.addWidget(btn_edit)
                        layout.addWidget(btn_print_html)
                        layout.addWidget(btn_print_docx)
                        layout.setContentsMargins(5,2,5,2)
                        cell_widget.setLayout(layout)
                        table.setCellWidget(row_idx, col_idx, cell_widget)
                        table.setColumnWidth(col_idx, 200)
                    else:
                        item = QTableWidgetItem(str(data.get(key, "")))
                        table.setItem(row_idx, col_idx, item)

            table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
            table.setWordWrap(True)
            table.resizeColumnsToContents()
            table.resizeRowsToContents()
            
            # Hide progress bar and reset status
            self.progress_bar.hide()
            self.status_label.setText(f"Berhasil memuat {len(transaksis)} transaksi")
            
            self.resize((table.verticalHeader().width() + 40), 900)
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            # Reset status jika tidak ada file dipilih
            self.status_label.setText("Tidak ada file dipilih")
        # QMessageBox.information(self, "Info", "Tes Tombol")

    def filterTable(self, keyword):
        keyword = keyword.lower()
        for row in range(self.ui.tableWidget.rowCount()):
            match = False
            for col in range(self.ui.tableWidget.columnCount()):
                text = ""
                item = self.ui.tableWidget.item(row, col)
                if item:
                    text = item.text()
                else:
                    widget = self.ui.tableWidget.cellWidget(row,col)
                    if isinstance(widget, QLabel):
                        text = widget.text()
                if keyword in text.lower():
                    match = True
                    break
            self.ui.tableWidget.setRowHidden(row, not match)

    def loadDB(self):
        print(Db('db2025.sqlite').getBku())

    def showDialogSekolah(self):
        dialog = DialogSekolah()
        if dialog.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Info", "Ok")
        else:
            QMessageBox.warning(self, "Warning", "Data sekolah tidak disimpan")

    def editTransaksi(self, data):
        pass


def closeApp():
    app.exit(0)


if __name__ == "__main__":
    splash = SplashScreen()

    def showMainWindow():
        splash.close()

        main_win = MainWindow()
        main_win.show()
        app.main_win = main_win

    if splash.exec() == QDialog.Accepted:
        showMainWindow()

    sys.exit(app.exec())
