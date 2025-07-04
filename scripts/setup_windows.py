#!/usr/bin/env python3
"""
Windows setup script for AppKuitansiBOS
Ensures Ghostscript and Poppler are properly configured
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_portable_dependencies():
    """Setup portable Ghostscript and Poppler for Windows"""
    
    # Get the application directory
    if getattr(sys, 'frozen', False):
        # Running from PyInstaller bundle
        app_dir = Path(sys._MEIPASS)
    else:
        # Running from source
        app_dir = Path(__file__).parent.parent
    
    # Setup Ghostscript
    gs_dir = app_dir / 'portable' / 'ghostscript' / 'bin'
    if gs_dir.exists():
        gs_path = str(gs_dir)
        current_path = os.environ.get('PATH', '')
        if gs_path not in current_path:
            os.environ['PATH'] = f"{gs_path};{current_path}"
        
        # Set Ghostscript executable
        os.environ['GS'] = str(gs_dir / 'gswin64c.exe')
        print(f"Ghostscript configured: {os.environ['GS']}")
    else:
        print("Warning: Portable Ghostscript not found")
    
    # Setup Poppler
    poppler_dir = app_dir / 'portable' / 'poppler' / 'Library' / 'bin'
    if poppler_dir.exists():
        poppler_path = str(poppler_dir)
        current_path = os.environ.get('PATH', '')
        if poppler_path not in current_path:
            os.environ['PATH'] = f"{poppler_path};{current_path}"
        print(f"Poppler configured: {poppler_path}")
    else:
        print("Warning: Portable Poppler not found")

def test_dependencies():
    """Test if Ghostscript and Poppler are working"""
    
    # Test Ghostscript
    try:
        result = subprocess.run(['gs', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✓ Ghostscript version: {result.stdout.strip()}")
        else:
            print("✗ Ghostscript test failed")
    except Exception as e:
        print(f"✗ Ghostscript not available: {e}")
    
    # Test Poppler (pdfinfo)
    try:
        result = subprocess.run(['pdfinfo', '-v'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✓ Poppler available")
        else:
            print("✗ Poppler test failed")
    except Exception as e:
        print(f"✗ Poppler not available: {e}")

if __name__ == "__main__":
    print("Setting up Windows dependencies...")
    setup_portable_dependencies()
    test_dependencies()
    print("Setup complete!")
