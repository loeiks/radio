import sys
import os
import ctypes
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from .ui.main_window import RadioPlayerWindow

# COM initialization constants
COINIT_MULTITHREADED = 0x0
COINIT_APARTMENTTHREADED = 0x2
COINIT_DISABLE_OLE1DDE = 0x4

def main():
    # Initialize COM in multi-threaded mode
    ctypes.windll.ole32.CoInitializeEx(None, COINIT_MULTITHREADED | COINIT_DISABLE_OLE1DDE)
    
    try:
        app = QApplication(sys.argv)
        
        # Set application icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'radio_icon.ico')
        if os.path.exists(icon_path):
            app.setWindowIcon(QIcon(icon_path))
        
        window = RadioPlayerWindow()
        window.show()
        sys.exit(app.exec())
    finally:
        # Cleanup COM
        ctypes.windll.ole32.CoUninitialize()

if __name__ == "__main__":
    main()
