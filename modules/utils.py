import pandas as pd
import camelot
from pathlib import Path
from PySide6.QtWidgets import QMessageBox
import datetime
from collections import defaultdict

current_dir = Path(__file__).resolve().parent
base_dir = current_dir.parent


def extractTable(file_path=None):
    if not file_path:
        file_path = base_dir / "contoh" / "bku.pdf"
    print("Start extracting..")
    tables = camelot.read_pdf(file_path, pages="all", flavor="lattice")
    if tables.n == 0:
        QMessageBox.warning(None, "Error", "File tidak memeiliki tabel")
        return False
    
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

    data_rows = data_rows.drop(columns=[5,7], errors='ignore')
    header_row = header_row.drop(columns=[5,7], errors='ignore')
    final_data = pd.concat([header_row, data_rows], ignore_index=True)
    final_data.columns = final_data.iloc[0]
    final_data = final_data.drop(index=0)
    data_dict = final_data.to_dict(orient='records')
    print("Extracting finished.")
    return groupBku(data_dict)

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
        item["penerima"] = "Penerima"
        hasil.append(item)

    return hasil
    

# print(groupBku(extractTable()))