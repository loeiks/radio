from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

def get_dark_theme_palette():
    """Returns the dark theme palette for the application."""
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#2C3E50"))  # Dark Blue background
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor("#34495E"))  # Darker blue for text fields
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor("#3498DB"))  # Blue buttons
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.Highlight, QColor("#2ECC71"))  # Green highlight
    palette.setColor(QPalette.HighlightedText, Qt.white)
    return palette

def get_dark_theme_stylesheet():
    """Returns the dark theme stylesheet for the application."""
    return """
        QMainWindow {
            border: 2px solid #1A242F;
            border-radius: 10px;
        }
        QLabel#titleLabel {
            font-size: 24px;
            font-weight: bold;
            color: white;
            background-color: #1A242F;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }
        QLabel#currentStationLabel {
            font-size: 18px;
            color: #ECF0F1;
            background-color: #34495E;
            padding: 8px;
            border-radius: 6px;
            text-align: center;
        }
        QPushButton {
            font-size: 16px;
            font-weight: bold;
            padding: 10px 15px;
            border: 2px solid;
            border-radius: 8px;
            min-width: 80px;
        }
        QPushButton#playPauseButton {
            background-color: #2ECC71;
            border-color: #27AE60;
        }
        QPushButton#playPauseButton:hover {
            background-color: #27AE60;
        }
        QPushButton#prevNextButton {
            background-color: #3498DB;
            border-color: #2980B9;
        }
        QPushButton#prevNextButton:hover {
            background-color: #2980B9;
        }
        QPushButton#minimizeButton {
            background-color: #F39C12;
            border-color: #E67E22;
        }
        QPushButton#minimizeButton:hover {
            background-color: #E67E22;
        }
        QPushButton#exitButton {
            background-color: #E74C3C;
            border-color: #C0392B;
        }
        QPushButton#exitButton:hover {
            background-color: #C0392B;
        }
        QSlider::groove:horizontal {
            border: 1px solid #999999;
            height: 8px;
            background: #BDC3C7;
            margin: 2px 0;
            border-radius: 4px;
        }
        QSlider::handle:horizontal {
            background: #2ECC71;
            border: 1px solid #27AE60;
            width: 18px;
            margin: -5px 0;
            border-radius: 9px;
        }
        QSlider::sub-page:horizontal {
            background: #2ECC71;
            border-radius: 4px;
        }
        QFrame#separator {
            background-color: #555555;
            height: 2px;
            border-radius: 1px;
        }    """
