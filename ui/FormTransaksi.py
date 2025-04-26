from PySide6.QtWidgets import QDialog, QLineEdit, QTextEdit, QLabel, QPushButton, QFormLayout,QHBoxLayout, QVBoxLayout

from modules.db import Db

class DialogTransaksi(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__()

        self.transaksi = {}
        if data:
            for key,_ in data:
                self.transaksi[key] = data[key]
