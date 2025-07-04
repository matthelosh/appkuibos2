import sqlite3
from pathlib import Path
import os
import re
from datetime import datetime

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
            penerima VARCHAR(30),
            bukti BLOB
        )
    """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_table)
            conn.commit()
            
        # Check and add missing columns if they don't exist
        self.migrate_add_penerima_column()
        self.migrate_add_bukti_column()
    
    def migrate_add_penerima_column(self):
        """Add penerima column to existing bkus table if it doesn't exist"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if penerima column exists
                cursor.execute("PRAGMA table_info(bkus)")
                columns = [column[1] for column in cursor.fetchall()]
                
                if 'penerima' not in columns:
                    # Add penerima column with default value
                    cursor.execute("ALTER TABLE bkus ADD COLUMN penerima VARCHAR(30) DEFAULT 'Penerima'")
                    conn.commit()
                    print("Added penerima column to existing bkus table")
                    
        except Exception as e:
            print(f"Error during migration: {e}")
    
    def migrate_add_bukti_column(self):
        """Add bukti column to existing bkus table if it doesn't exist"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if bukti column exists
                cursor.execute("PRAGMA table_info(bkus)")
                columns = [column[1] for column in cursor.fetchall()]
                
                if 'bukti' not in columns:
                    # Add bukti column for storing image files
                    cursor.execute("ALTER TABLE bkus ADD COLUMN bukti BLOB")
                    conn.commit()
                    print("Added bukti column to existing bkus table")
                    
        except Exception as e:
            print(f"Error during bukti column migration: {e}")

    def storeBku(self, data):
        """Store single BKU transaction"""
        if not self.check_table('bkus'):
            self.create_table_bku()
        
        sql_insert = """
        INSERT INTO bkus (tanggal, kode_kegiatan, kode_rekening, no_bukti, uraian, nilai, penerima)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_insert, (
                    data.get('tanggal', ''),
                    data.get('kode_kegiatan', ''),
                    data.get('kode_rekening', ''),
                    data.get('no_bukti', ''),
                    data.get('uraian', ''),
                    data.get('nilai', ''),
                    data.get('penerima', '')
                ))
                conn.commit()
            return True
        except Exception as e:
            print(f"Error storing BKU: {e}")
            return False

    def storeBkus(self, datas):
        """Store multiple BKU transactions"""
        if not self.check_table('bkus'):
            self.create_table_bku()
        
        # First clear existing data
        self.clearBkus()
        
        sql_insert = """
        INSERT INTO bkus (tanggal, kode_kegiatan, kode_rekening, no_bukti, uraian, nilai, penerima)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                for data in datas:
                    cursor.execute(sql_insert, (
                        data.get('tanggal', ''),
                        data.get('kode_kegiatan', ''),
                        data.get('kode_rekening', ''),
                        data.get('no_bukti', ''),
                        data.get('uraian', ''),
                        data.get('nilai', ''),
                        data.get('penerima', '')
                    ))
                conn.commit()
            return True
        except Exception as e:
            print(f"Error storing BKUs: {e}")
            return False

    def clearBkus(self):
        """Clear all BKU data from database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM bkus")
                conn.commit()
            return True
        except Exception as e:
            print(f"Error clearing BKUs: {e}")
            return False

    def getBku(self, file_path=None):
        """Get all BKU transactions from database"""
        if file_path:
            self.file_db = file_path
        try:
            if not self.check_table('bkus'):
                self.create_table_bku()
                return []
            
            # Ensure penerima column exists
            self.migrate_add_penerima_column()
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if penerima column exists in the current table
                cursor.execute("PRAGMA table_info(bkus)")
                columns = [column[1] for column in cursor.fetchall()]
                
                if 'penerima' in columns:
                    cursor.execute("""
                        SELECT tanggal, kode_kegiatan, kode_rekening, no_bukti, uraian, nilai, penerima 
                        FROM bkus ORDER BY tanggal, no_bukti
                    """)
                    results = cursor.fetchall()
                    
                    # Convert to dictionary format
                    bkus = []
                    for row in results:
                        bku = {
                            'tanggal': row[0],
                            'kode_kegiatan': row[1],
                            'kode_rekening': row[2],
                            'no_bukti': row[3],
                            'uraian': row[4],
                            'nilai': row[5],
                            'nominal': row[5],  # For compatibility
                            'penerima': row[6] if len(row) > 6 else 'Penerima'
                        }
                        bkus.append(bku)
                else:
                    # Fallback for tables without penerima column
                    cursor.execute("""
                        SELECT tanggal, kode_kegiatan, kode_rekening, no_bukti, uraian, nilai 
                        FROM bkus ORDER BY tanggal, no_bukti
                    """)
                    results = cursor.fetchall()
                    
                    # Convert to dictionary format with default penerima
                    bkus = []
                    for row in results:
                        bku = {
                            'tanggal': row[0],
                            'kode_kegiatan': row[1],
                            'kode_rekening': row[2],
                            'no_bukti': row[3],
                            'uraian': row[4],
                            'nilai': row[5],
                            'nominal': row[5],  # For compatibility
                            'penerima': 'Penerima'  # Default value
                        }
                        bkus.append(bku)
            
            return bkus
        except Exception as e:
            print(f"Error getting BKU data: {e}")
            return []

    def updateBku(self, no_bukti, penerima):
        """Update penerima field for a specific BKU transaction"""
        # Ensure the penerima column exists
        if not self.check_table('bkus'):
            self.create_table_bku()
        else:
            self.migrate_add_penerima_column()
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE bkus SET penerima = ? WHERE no_bukti = ?
                """, (penerima, no_bukti))
                conn.commit()
                return cursor.rowcount > 0  # Returns True if any row was updated
        except Exception as e:
            print(f"Error updating BKU: {e}")
            return False
    
    def updateBukuBukti(self, no_bukti, image_data):
        """Update bukti (evidence) image for a specific BKU transaction"""
        # Ensure the bukti column exists
        if not self.check_table('bkus'):
            self.create_table_bku()
        else:
            self.migrate_add_bukti_column()
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE bkus SET bukti = ? WHERE no_bukti = ?
                """, (image_data, no_bukti))
                conn.commit()
                return cursor.rowcount > 0  # Returns True if any row was updated
        except Exception as e:
            print(f"Error updating BKU bukti: {e}")
            return False
    
    def getBukuBukti(self, no_bukti):
        """Get bukti (evidence) image for a specific BKU transaction"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT bukti FROM bkus WHERE no_bukti = ?
                """, (no_bukti,))
                result = cursor.fetchone()
                return result[0] if result and result[0] else None
        except Exception as e:
            print(f"Error getting BKU bukti: {e}")
            return None
    
    def resetDatabase(self):
        """Reset database by dropping and recreating the bkus table"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Drop the existing table
                cursor.execute("DROP TABLE IF EXISTS bkus")
                
                # Recreate the table with proper structure
                cursor.execute("""
                    CREATE TABLE bkus(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tanggal DATE,
                        kode_kegiatan VARCHAR(60),
                        kode_rekening VARCHAR(50),
                        no_bukti VARCHAR(20),
                        uraian TEXT,
                        nilai VARCHAR(12),
                        penerima VARCHAR(30) DEFAULT 'Penerima'
                    )
                """)
                
                conn.commit()
                print("Database reset successfully")
            return True
        except Exception as e:
            print(f"Error resetting database: {e}")
            return False
    
    @staticmethod
    def getAvailableYears():
        """Get list of available database years"""
        cur_dir = Path(__file__).resolve().parent
        data_dir = cur_dir.parent / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        
        years = []
        current_year = datetime.now().year
        
        # Add current year and few years before/after
        for year in range(current_year - 2, current_year + 3):
            years.append(year)
        
        # Check for existing database files and extract years
        if data_dir.exists():
            for file in data_dir.glob("*.sqlite"):
                # Extract year from filename like "db2025.sqlite" or "Db2025.sqlite"
                match = re.search(r'db(\d{4})\.sqlite', file.name, re.IGNORECASE)
                if match:
                    year = int(match.group(1))
                    if year not in years:
                        years.append(year)
        
        return sorted(years, reverse=True)
    
    @staticmethod
    def getDatabaseInfo(year):
        """Get information about database for specific year"""
        cur_dir = Path(__file__).resolve().parent
        data_dir = cur_dir.parent / "data"
        db_file = f"Db{year}.sqlite"
        db_path = data_dir / db_file
        
        info = {
            'year': year,
            'filename': db_file,
            'exists': db_path.exists(),
            'path': str(db_path),
            'size': 0,
            'transaction_count': 0
        }
        
        if db_path.exists():
            # Get file size
            info['size'] = db_path.stat().st_size
            
            # Get transaction count
            try:
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bkus'")
                    if cursor.fetchone():
                        cursor.execute("SELECT COUNT(*) FROM bkus")
                        info['transaction_count'] = cursor.fetchone()[0]
            except Exception as e:
                print(f"Error getting database info: {e}")
        
        return info
    
    @staticmethod
    def createYearDatabase(year):
        """Create database for specific year"""
        try:
            db_file = f"Db{year}.sqlite"
            db = Db(db_file)
            db.create_table_bku()
            return True
        except Exception as e:
            print(f"Error creating year database: {e}")
            return False
