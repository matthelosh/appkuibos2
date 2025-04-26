import os
import json
from pathlib import Path

def getAnggaran():
    file_config = Path(__file__).resolve().parent.parent / "data" / "config.json"
    with file_config.open('r') as f:
        anggaran = json.load(f)
    return anggaran
