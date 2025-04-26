import sqlite3
from pathlib import Path

class Db():
    def __init__(self, db_file=None):
        cur_dir = Path(__file__).resolve().parent
        base_dir = cur_dir.parent / "data"
        base_dir.mkdir(parents=True, exist_ok=True)
        file_db = "db.sqlite" if not db_file else db_file
        self.db_path = base_dir / file_db
        if not self.db_path.exists():
            self.db_path.touch(exist_ok=True)
        # db = sqlite3.connect(db_path)
        # cursor = db.cursor()
    
    

    def check_table(self,table_name):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
            result = cursor.fetchone() is not None
        return result

    def create_table_bku(self):
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS bkus(
            id INT AUTO_INCREMENT PRIMARY KEY,
            tanggal DATE,
            kode_kegiatan VARCHAR(60),
            kode_rekening VARCHAR(50),
            no_bukti VARCHAR(20),
            uraian TEXT,
            nilai VARCHAR(12),
            penerima VARCHAR(30)
        )
    """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_table)
            conn.commit()

    def storeBku(self, data):
        pass

    def storeBkus(self, datas):
        pass

    def getBku(self,file_path=None):
        if file_path:
            self.file_db = file_path
        try:
            if not self.check_table('bkus'):
                self.create_table_bku()
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM bkus")
                results = cursor.fetchall()
            return results
        except Exception as e:
            return f"Gagal ambil data BKU: {e}"
