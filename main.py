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
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from PySide6.QtGui import QPixmap, QIcon
import io
from ui.ui_welcome import Ui_DialogWelcome
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_formsekolah import Ui_DialogSekolah
from ui.ui_edit_bku import Ui_DialogEditBku
from ui.ui_select_year import Ui_DialogSelectYear
from ui.ui_upload_bukti import Ui_DialogUploadBukti
import ui.resources_rc
import time

from modules.sekolah import saveIdentitas, getIdentitas
from modules.config import getAnggaran
from modules.db import Db
from modules.utils import extractTable
from modules.print_docx import cetakTransaksiDocx, cetakSemuaTransaksiDocx
from datetime import datetime

app = QApplication(sys.argv)

# Set application icon
app_icon = QIcon()
app_icon.addFile("ui/icons/receipt--exclamation.png", QSize(64, 64))
app_icon.addFile("ui/icons/receipt--exclamation.png", QSize(32, 32))
app_icon.addFile("ui/icons/receipt--exclamation.png", QSize(16, 16))
app.setWindowIcon(app_icon)

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

class EditBkuDialog(QDialog):
    def __init__(self, data, parent=None):
        super(EditBkuDialog, self).__init__(parent)
        self.ui = Ui_DialogEditBku()
        self.ui.setupUi(self)
        self.data = data
        self.parent_window = parent
        
        # Load data into form
        self.loadData()
        
        # Connect buttons
        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_save.clicked.connect(self.saveData)
        
        # Focus on penerima field
        self.ui.lineEdit_penerima.setFocus()
        self.ui.lineEdit_penerima.selectAll()
    
    def loadData(self):
        """Load BKU data into form fields"""
        self.ui.lineEdit_no_bukti.setText(str(self.data.get('no_bukti', '')))
        self.ui.lineEdit_tanggal.setText(str(self.data.get('tanggal', '')))
        self.ui.lineEdit_uraian.setText(str(self.data.get('uraian', '')))
        self.ui.lineEdit_nilai.setText(str(self.data.get('nilai', '')))
        self.ui.lineEdit_penerima.setText(str(self.data.get('penerima', '')))
    
    def saveData(self):
        """Save updated penerima to database"""
        new_penerima = self.ui.lineEdit_penerima.text().strip()
        
        if not new_penerima:
            QMessageBox.warning(self, "Peringatan", "Nama penerima tidak boleh kosong!")
            return
        
        # Update database
        db = Db()
        no_bukti = self.data.get('no_bukti')
        
        if db.updateBku(no_bukti, new_penerima):
            # Update the data object
            self.data['penerima'] = new_penerima
            
            # Update current_transaksis in parent window
            if hasattr(self.parent_window, 'current_transaksis'):
                for transaksi in self.parent_window.current_transaksis:
                    if transaksi.get('no_bukti') == no_bukti:
                        transaksi['penerima'] = new_penerima
                        break
            
            QMessageBox.information(self, "Sukses", "Data penerima berhasil diperbarui!")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Gagal memperbarui data penerima!")

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


class SelectYearDialog(QDialog):
    def __init__(self, parent=None):
        super(SelectYearDialog, self).__init__(parent)
        self.ui = Ui_DialogSelectYear()
        self.ui.setupUi(self)
        
        # Populate year combo box with available years
        available_years = Db.getAvailableYears()
        for year in available_years:
            self.ui.comboBox_year.addItem(str(year))

        # Set default selected year
        current_year = datetime.now().year
        index = self.ui.comboBox_year.findText(str(current_year))
        if index != -1:
            self.ui.comboBox_year.setCurrentIndex(index)
        
        # Connect buttons
        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_select.clicked.connect(self.selectYear)
    
    def selectYear(self):
        selected_year = self.ui.comboBox_year.currentText()
        
        # Retrieve database info for the selected year
        db_info = Db.getDatabaseInfo(selected_year)
        
        # Set the parent database path
        self.parent().db = Db(db_info['filename'])

        # Create the database if it does not exist
        if not db_info['exists']:
            Db.createYearDatabase(selected_year)
        
        # Update info label
        transaction_count = db_info['transaction_count']
        self.parent().status_label.setText(f"Database Analis Anggaran Tahun {selected_year} (Transaksi: {transaction_count})")
        QMessageBox.information(self, "Info", f"Database Tahun {selected_year} dipilih\nFile: {db_info['filename']}")
        
        self.accept()

class UploadBuktiDialog(QDialog):
    def __init__(self, data, parent=None):
        super(UploadBuktiDialog, self).__init__(parent)
        self.ui = Ui_DialogUploadBukti()
        self.ui.setupUi(self)
        self.data = data
        self.parent_window = parent
        self.image_data = None
        
        # Load transaction data
        self.loadTransactionData()
        
        # Load existing image if available
        self.loadExistingImage()
        
        # Connect buttons
        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_browse.clicked.connect(self.browseImage)
        self.ui.pushButton_save.clicked.connect(self.saveImage)
        self.ui.pushButton_remove.clicked.connect(self.removeImage)
    
    def loadTransactionData(self):
        """Load transaction data into form"""
        self.ui.label_no_bukti_value.setText(str(self.data.get('no_bukti', '')))
        self.ui.label_uraian_value.setText(str(self.data.get('uraian', '')))
    
    def loadExistingImage(self):
        """Load existing image if available"""
        db = Db()
        existing_image = db.getBukuBukti(self.data.get('no_bukti'))
        
        if existing_image:
            self.image_data = existing_image
            self.displayImage(existing_image)
            self.ui.pushButton_save.setEnabled(False)  # No changes yet
            self.ui.pushButton_remove.setEnabled(True)
        else:
            self.ui.label_preview.setText("Belum ada gambar dipilih")
            self.ui.pushButton_save.setEnabled(False)
            self.ui.pushButton_remove.setEnabled(False)
    
    def browseImage(self):
        """Browse and select image file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Pilih File Gambar Bukti", 
            "", 
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        
        if file_path:
            try:
                # Read image file
                with open(file_path, 'rb') as file:
                    self.image_data = file.read()
                
                # Display image
                self.displayImage(self.image_data)
                
                # Show file info
                file_size = len(self.image_data) / 1024  # KB
                self.ui.label_file_info.setText(f"File: {file_path.split('/')[-1]} ({file_size:.1f} KB)")
                
                # Enable save button
                self.ui.pushButton_save.setEnabled(True)
                self.ui.pushButton_remove.setEnabled(True)
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal membaca file gambar:\n{str(e)}")
    
    def displayImage(self, image_data):
        """Display image in preview area"""
        try:
            # Create QPixmap from image data
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            
            # Scale image to fit preview area while maintaining aspect ratio
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    self.ui.label_preview.size(), 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                self.ui.label_preview.setPixmap(scaled_pixmap)
                self.ui.label_preview.setText("")  # Clear text
            else:
                self.ui.label_preview.setText("Format gambar tidak didukung")
                
        except Exception as e:
            self.ui.label_preview.setText(f"Error menampilkan gambar: {str(e)}")
    
    def saveImage(self):
        """Save image to database"""
        if not self.image_data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada gambar untuk disimpan!")
            return
        
        db = Db()
        no_bukti = self.data.get('no_bukti')
        
        if db.updateBukuBukti(no_bukti, self.image_data):
            QMessageBox.information(self, "Sukses", "Bukti gambar berhasil disimpan!")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Gagal menyimpan bukti gambar!")
    
    def removeImage(self):
        """Remove image from database"""
        reply = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            "Apakah Anda yakin ingin menghapus bukti gambar ini?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            db = Db()
            no_bukti = self.data.get('no_bukti')
            
            if db.updateBukuBukti(no_bukti, None):
                self.image_data = None
                self.ui.label_preview.setText("Belum ada gambar dipilih")
                self.ui.label_preview.setPixmap(QPixmap())  # Clear pixmap
                self.ui.label_file_info.setText("")
                self.ui.pushButton_save.setEnabled(False)
                self.ui.pushButton_remove.setEnabled(False)
                QMessageBox.information(self, "Sukses", "Bukti gambar berhasil dihapus!")
            else:
                QMessageBox.critical(self, "Error", "Gagal menghapus bukti gambar!")

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
        self.ui.act_reset_db.triggered.connect(self.resetDatabase)

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
            
            # Store extracted data to database
            if progress_callback:
                progress_callback("Menyimpan data ke database...", 95)
            
            db = Db()
            if db.storeBkus(transaksis):
                self.status_label.setText(f"Berhasil memuat dan menyimpan {len(transaksis)} transaksi")
            else:
                self.status_label.setText(f"Berhasil memuat {len(transaksis)} transaksi, gagal menyimpan ke database")

            # Add "Cetak Semua" buttons above the table
            if not hasattr(self.ui, 'btn_cetak_semua_docx'):
                # Create container widget for buttons
                self.ui.cetak_semua_container = QWidget()
                container_layout = QHBoxLayout()


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

                container_layout.addWidget(self.ui.btn_cetak_semua_docx)
                container_layout.addStretch()  # Push buttons to left
                self.ui.cetak_semua_container.setLayout(container_layout)

                # Insert container before table in the layout
                layout = self.ui.page_bku.layout()
                if layout:
                    layout.insertWidget(1, self.ui.cetak_semua_container)

            # Clear previous connections safely and connect buttons
            try:
                # self.ui.btn_cetak_semua_html.clicked.disconnect()
                self.ui.btn_cetak_semua_docx.clicked.disconnect()
            except:
                pass  # No connections to disconnect

            # self.ui.btn_cetak_semua_html.clicked.connect(lambda: cetakSemuaTransaksi(self, self.current_transaksis))
            self.ui.btn_cetak_semua_docx.clicked.connect(lambda: cetakSemuaTransaksiDocx(self, self.current_transaksis))
            # self.ui.btn_cetak_semua_html.setText(f"📄 Cetak Semua HTML ({len(transaksis)} transaksi)")
            self.ui.btn_cetak_semua_docx.setText(f"📝 Cetak Semua DOCX ({len(transaksis)} transaksi)")
            self.ui.cetak_semua_container.show()

            # Define proper column order for import as well
            column_mapping = [
                'tanggal',          # Column 0: TANGGAL
                'kode_kegiatan',    # Column 1: KODE KEGIATAN
                'kode_rekening',    # Column 2: KODE REKENING  
                'no_bukti',         # Column 3: NO. BUKTI
                'uraian',           # Column 4: URAIAN
                'nilai',            # Column 5: NOMINAL
                'penerima',         # Column 6: PENERIMA
                'opsi'              # Column 7: OPSI
            ]
            
            table.setColumnCount(8)
            table.setRowCount(len(transaksis))
            table.setHorizontalHeaderLabels(["TANGGAL", "KODE KEGIATAN", "KODE REKENING", "NO. BUKTI", "URAIAN", "NOMINAL", "PENERIMA", "OPSI"])

            for row_idx, data in enumerate(transaksis):
                for col_idx, field in enumerate(column_mapping):
                    if col_idx == 4:  # URAIAN column
                        label = QLabel(data.get('uraian', ''))
                        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                        label.setWordWrap(True)
                        label.setStyleSheet("padding: 6px")
                        table.setCellWidget(row_idx, col_idx, label)
                    elif col_idx == 7:  # OPSI column
                        btn_edit = QPushButton("Edit")
                        btn_upload = QPushButton("📷 Bukti")
                        btn_print_docx = QPushButton("📝 DOCX")
                        btn_edit.clicked.connect(lambda _, data=transaksis[row_idx]: self.editTransaksi(data))
                        btn_upload.clicked.connect(lambda _, data=transaksis[row_idx]: self.uploadBukti(data))
                        btn_print_docx.clicked.connect(lambda _, data=transaksis[row_idx]: cetakTransaksiDocx(self, data))
                        cell_widget = QWidget()
                        layout = QHBoxLayout()
                        layout.addWidget(btn_edit)
                        layout.addWidget(btn_upload)
                        layout.addWidget(btn_print_docx)
                        layout.setContentsMargins(5,2,5,2)
                        cell_widget.setLayout(layout)
                        table.setCellWidget(row_idx, col_idx, cell_widget)
                        table.setColumnWidth(col_idx, 280)
                    else:
                        # Map the correct data to the correct column
                        value = data.get(field, "")
                        item = QTableWidgetItem(str(value))
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
        """Load BKU data from database and display in table"""
        db = Db()
        transaksis = db.getBku()
        
        if not transaksis:
            QMessageBox.information(self, "Info", "Tidak ada data transaksi yang tersimpan di database")
            return
        
        # Store transaksis in instance variable for later use
        self.current_transaksis = transaksis
        
        # Update status
        self.status_label.setText(f"Memuat {len(transaksis)} transaksi dari database")
        
        # Setup table
        table = self.ui.tableWidget
        
        # Add "Cetak Semua" buttons above the table
        if not hasattr(self.ui, 'btn_cetak_semua_docx'):
            # Create container widget for buttons
            self.ui.cetak_semua_container = QWidget()
            container_layout = QHBoxLayout()
            
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
            
            container_layout.addWidget(self.ui.btn_cetak_semua_docx)
            container_layout.addStretch()  # Push buttons to left
            self.ui.cetak_semua_container.setLayout(container_layout)
            
            # Insert container before table in the layout
            layout = self.ui.page_bku.layout()
            if layout:
                layout.insertWidget(1, self.ui.cetak_semua_container)
        
        # Clear previous connections safely and connect buttons
        try:
            self.ui.btn_cetak_semua_docx.clicked.disconnect()
        except:
            pass  # No connections to disconnect
        
        self.ui.btn_cetak_semua_docx.clicked.connect(lambda: cetakSemuaTransaksiDocx(self, self.current_transaksis))
        self.ui.btn_cetak_semua_docx.setText(f"📝 Cetak Semua DOCX ({len(transaksis)} transaksi)")
        self.ui.cetak_semua_container.show()
        
        # Define proper column order
        column_mapping = [
            'tanggal',          # Column 0: TANGGAL
            'kode_kegiatan',    # Column 1: KODE KEGIATAN
            'kode_rekening',    # Column 2: KODE REKENING  
            'no_bukti',         # Column 3: NO. BUKTI
            'uraian',           # Column 4: URAIAN
            'nilai',            # Column 5: NOMINAL
            'penerima',         # Column 6: PENERIMA
            'opsi'              # Column 7: OPSI
        ]
        
        table.setColumnCount(8)
        table.setRowCount(len(transaksis))
        table.setHorizontalHeaderLabels(["TANGGAL", "KODE KEGIATAN", "KODE REKENING", "NO. BUKTI", "URAIAN", "NOMINAL", "PENERIMA", "OPSI"])
        
        for row_idx, data in enumerate(transaksis):
            for col_idx, field in enumerate(column_mapping):
                if col_idx == 4:  # URAIAN column
                    label = QLabel(data.get('uraian', ''))
                    label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                    label.setWordWrap(True)
                    label.setStyleSheet("padding: 6px")
                    table.setCellWidget(row_idx, col_idx, label)
                elif col_idx == 7:  # OPSI column
                    btn_edit = QPushButton("Edit")
                    btn_upload = QPushButton("📷 Bukti")
                    btn_print_docx = QPushButton("📝 DOCX")
                    btn_edit.clicked.connect(lambda _, data=transaksis[row_idx]: self.editTransaksi(data))
                    btn_upload.clicked.connect(lambda _, data=transaksis[row_idx]: self.uploadBukti(data))
                    btn_print_docx.clicked.connect(lambda _, data=transaksis[row_idx]: cetakTransaksiDocx(self, data))
                    cell_widget = QWidget()
                    layout = QHBoxLayout()
                    layout.addWidget(btn_edit)
                    layout.addWidget(btn_upload)
                    layout.addWidget(btn_print_docx)
                    layout.setContentsMargins(5,2,5,2)
                    cell_widget.setLayout(layout)
                    table.setCellWidget(row_idx, col_idx, cell_widget)
                    table.setColumnWidth(col_idx, 280)
                else:
                    # Map the correct data to the correct column
                    value = data.get(field, "")
                    item = QTableWidgetItem(str(value))
                    table.setItem(row_idx, col_idx, item)
        
        table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        table.setWordWrap(True)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        
        self.status_label.setText(f"Berhasil memuat {len(transaksis)} transaksi dari database")
        
        self.resize((table.verticalHeader().width() + 40), 900)
        self.ui.stackedWidget.setCurrentIndex(1)

    def showDialogSekolah(self):
        dialog = DialogSekolah()
        if dialog.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Info", "Ok")
        else:
            QMessageBox.warning(self, "Warning", "Data sekolah tidak disimpan")

    def editTransaksi(self, data):
        """Open edit dialog for BKU transaction"""
        dialog = EditBkuDialog(data, self)
        if dialog.exec() == QDialog.Accepted:
            # Refresh the table to show updated data
            self.refreshTable()
            QMessageBox.information(self, "Sukses", "Data berhasil diperbarui!")
    
    def refreshTable(self):
        """Refresh the table with current data"""
        if not hasattr(self, 'current_transaksis') or not self.current_transaksis:
            return
        
        table = self.ui.tableWidget
        
        # Update the table cells with new data
        for row_idx, data in enumerate(self.current_transaksis):
            # Update penerima column (index 6)
            item = QTableWidgetItem(str(data.get('penerima', '')))
            table.setItem(row_idx, 6, item)
    
    def uploadBukti(self, data):
        """Open upload bukti dialog for BKU transaction"""
        dialog = UploadBuktiDialog(data, self)
        if dialog.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Sukses", "Bukti gambar berhasil dikelola!")
    
    def resetDatabase(self):
        """Reset database after user confirmation"""
        reply = QMessageBox.question(
            self, 
            "Konfirmasi Reset Database", 
            "Apakah Anda yakin ingin mereset database?\n\n"
            "⚠️ PERINGATAN: Semua data transaksi yang tersimpan akan dihapus secara permanen!\n\n"
            "Operasi ini tidak dapat dibatalkan.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            # Ask for double confirmation
            confirm_reply = QMessageBox.question(
                self,
                "Konfirmasi Terakhir",
                "Anda akan menghapus SEMUA data transaksi.\n\n"
                "Apakah Anda benar-benar yakin?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if confirm_reply == QMessageBox.StandardButton.Yes:
                db = Db()
                if db.resetDatabase():
                    # Clear current data from memory
                    if hasattr(self, 'current_transaksis'):
                        self.current_transaksis = []
                    
                    # Clear table
                    self.ui.tableWidget.setRowCount(0)
                    
                    # Hide "Cetak Semua" buttons if they exist
                    if hasattr(self.ui, 'cetak_semua_container'):
                        self.ui.cetak_semua_container.hide()
                    
                    # Update status
                    self.status_label.setText("Database berhasil direset")
                    
                    # Go back to home page
                    self.ui.stackedWidget.setCurrentIndex(0)
                    
                    QMessageBox.information(
                        self, 
                        "Sukses", 
                        "Database berhasil direset!\n\n"
                        "Semua data transaksi telah dihapus."
                    )
                else:
                    QMessageBox.critical(
                        self, 
                        "Error", 
                        "Gagal mereset database!\n\n"
                        "Silakan coba lagi atau hubungi administrator."
                    )
            else:
                self.status_label.setText("Reset database dibatalkan")
        else:
            self.status_label.setText("Reset database dibatalkan")


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
