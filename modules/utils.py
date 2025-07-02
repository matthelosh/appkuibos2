import pandas as pd
import camelot
from pathlib import Path
from PySide6.QtWidgets import QMessageBox
import datetime
from collections import defaultdict

current_dir = Path(__file__).resolve().parent
base_dir = current_dir.parent


def extractTable(file_path=None, progress_callback=None):
    if not file_path:
        file_path = base_dir / "contoh" / "bku.pdf"
    
    if progress_callback:
        progress_callback("Memulai ekstraksi PDF...", 10)
    print("Start extracting..")
    
    if progress_callback:
        progress_callback("Membaca tabel dari PDF...", 30)
    tables = camelot.read_pdf(file_path, pages="all", flavor="lattice")
    
    if tables.n == 0:
        if progress_callback:
            progress_callback("Error: File tidak memiliki tabel", 0)
        QMessageBox.warning(None, "Error", "File tidak memeiliki tabel")
        return False

    if progress_callback:
        progress_callback("Menggabungkan data tabel...", 50)
    all_tables = [tables[i].df for i in range(tables.n)]
    bkus = pd.concat(all_tables, ignore_index=True)

    def format_tanggal(tanggal):
        try:
            return datetime.datetime.strptime(tanggal, "%d-%m-%Y").strftime("%Y-%m-%d")
        except ValueError:
            return tanggal

    bkus.iloc[:,0] = bkus.iloc[:,0].apply(format_tanggal)
    header_row = bkus.iloc[[0]]
    header_row = header_row.map(
        lambda x: str(x).strip().lower().replace(" ","_").replace(".","").replace("pengeluaran", "nilai").replace("\n","_")
    )

    data_rows = bkus.iloc[1:]
    data_rows = data_rows[data_rows[1].notna() & (data_rows[1].astype(str).str.len() >= 3)]
    data_rows = data_rows[~data_rows[4].astype(str).str.contains("PPh|PPn", na=False, case=False)]
    data_rows = data_rows[data_rows[5].astype(str).str.strip().isin(["0","0.00","0,00",""])]

    data_rows[6] = (data_rows[6].astype(str).str.replace(".","", regex=False))
    data_rows[2] = (data_rows[2].astype(str).str.replace("\n","", regex=False))

    if progress_callback:
        progress_callback("Memproses data transaksi...", 70)
    
    data_rows = data_rows.drop(columns=[5,7], errors='ignore')
    header_row = header_row.drop(columns=[5,7], errors='ignore')
    final_data = pd.concat([header_row, data_rows], ignore_index=True)
    final_data.columns = final_data.iloc[0]
    final_data = final_data.drop(index=0)
    data_dict = final_data.to_dict(orient='records')
    
    if progress_callback:
        progress_callback("Mengelompokkan data BKU...", 90)
    
    print("Extracting finished.")
    hasil = groupBku(data_dict)
    
    if progress_callback:
        progress_callback("Ekstraksi selesai!", 100)
    
    return hasil

def groupBku(bkus):
    grouped = defaultdict( lambda: {
        "tanggal": "",
        "kode_kegiatan": "",
        "kode_rekening": "",
        "no_bukti": "",
        "uraian": [],
        "nilai": 0,
        "penerima": ""
    })

    for bku in bkus:
        key = bku["no_bukti"]
        group = grouped[key]

        group["tanggal"]        = bku["tanggal"]
        group["kode_kegiatan"]  = bku["kode_kegiatan"]
        group["kode_rekening"]  = bku["kode_rekening"]
        group["no_bukti"]       = bku["no_bukti"]

        group["uraian"].append(bku["uraian"])
        try:
            group["nilai"] += int(str(bku["nilai"]).replace(".","").replace(",",""))
        except ValueError:
            group["nilai"] = 0

        group["penerima"] = "Penerima"

    hasil = []
    for item in grouped.values():
        item["uraian"] = "; ".join(item["uraian"])
        nilai_asli = item["nilai"]
        nilai_format = "{:,.0f}".format(nilai_asli)
        item["nilai"] = nilai_format.replace(",",".")
        item["nominal"] = item["nilai"]  # Add nominal field for compatibility
        item["penerima"] = "Penerima"
        hasil.append(item)

    return hasil

def terbilang(angka):
    """
    Mengkonversi angka menjadi kata-kata dalam bahasa Indonesia
    
    Args:
        angka (int/float/str): Angka yang akan dikonversi
        
    Returns:
        str: Hasil konversi angka dalam kata-kata bahasa Indonesia
        
    Example:
        terbilang(1234567) -> "satu juta dua ratus tiga puluh empat ribu lima ratus enam puluh tujuh"
    """
    
    # Konversi input ke integer
    try:
        if isinstance(angka, str):
            # Hapus pemisah ribuan (titik atau koma)
            angka = angka.replace('.', '').replace(',', '')
        angka = int(angka)
    except (ValueError, TypeError):
        return "nol"
    
    if angka == 0:
        return "nol"
    
    if angka < 0:
        return "minus " + terbilang(-angka)
    
    # Satuan dasar
    satuan = [
        "", "satu", "dua", "tiga", "empat", "lima", 
        "enam", "tujuh", "delapan", "sembilan"
    ]
    
    # Belasan
    belasan = [
        "sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", 
        "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
    ]
    
    # Puluhan
    puluhan = [
        "", "", "dua puluh", "tiga puluh", "empat puluh", "lima puluh",
        "enam puluh", "tujuh puluh", "delapan puluh", "sembilan puluh"
    ]
    
    def konversi_ratusan(n):
        """Konversi angka 0-999 menjadi kata"""
        hasil = []
        
        # Ratusan
        ratus = n // 100
        if ratus > 0:
            if ratus == 1:
                hasil.append("seratus")
            else:
                hasil.append(satuan[ratus] + " ratus")
        
        # Puluhan dan satuan
        sisa = n % 100
        if sisa >= 20:
            hasil.append(puluhan[sisa // 10])
            if sisa % 10 > 0:
                hasil.append(satuan[sisa % 10])
        elif sisa >= 10:
            hasil.append(belasan[sisa - 10])
        elif sisa > 0:
            hasil.append(satuan[sisa])
        
        return " ".join(hasil)
    
    def konversi_grup(n, nama_grup):
        """Konversi grup angka (ribuan, jutaan, dll)"""
        if n == 0:
            return ""
        
        kata_angka = konversi_ratusan(n)
        
        # Khusus untuk "satu ribu" menjadi "seribu"
        if nama_grup == "ribu" and n == 1:
            return "seribu"
        
        return kata_angka + " " + nama_grup
    
    # Pecah angka berdasarkan grup
    hasil = []
    
    # Triliun
    if angka >= 1000000000000:
        triliun = angka // 1000000000000
        hasil.append(konversi_grup(triliun, "triliun"))
        angka %= 1000000000000
    
    # Miliar
    if angka >= 1000000000:
        miliar = angka // 1000000000
        hasil.append(konversi_grup(miliar, "miliar"))
        angka %= 1000000000
    
    # Juta
    if angka >= 1000000:
        juta = angka // 1000000
        hasil.append(konversi_grup(juta, "juta"))
        angka %= 1000000
    
    # Ribu
    if angka >= 1000:
        ribu = angka // 1000
        hasil.append(konversi_grup(ribu, "ribu"))
        angka %= 1000
    
    # Ratusan, puluhan, satuan
    if angka > 0:
        hasil.append(konversi_ratusan(angka))
    
    return " ".join(filter(None, hasil))
# print(groupBku(extractTable()))
