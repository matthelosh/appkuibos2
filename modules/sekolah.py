import os
import sys
import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
parent_dir = base_dir.parent

file_path = parent_dir / "data/sekolah.json"

def saveIdentitas(**kwargs):
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open("w", encoding="UTF-8") as file:
            json.dump(kwargs, file, indent=4)
        return True, "Data Sekolah Disimpan"
    except (IOError, TypeError, ValueError) as e:
        return f"Gagal menyiman data sekolah: { str(e)}"
    
def getIdentitas():
    try:
        if file_path.exists():
            with file_path.open("r", encoding="UTF-8") as file:
                data = json.load(file)
                return data
    
    except Exception as e:
        return f"Gagal membaca: {e}"