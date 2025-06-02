from PySide6.QtCore import QSize

# Package metadata
__version__ = '1.0.0'

# Import all public interfaces
from .player.radio_player import RadioPlayer
from .ui.main_window import RadioPlayerWindow
from .ui.ui_styles import get_dark_theme_palette, get_dark_theme_stylesheet

__all__ = ['RadioPlayer', 'RadioPlayerWindow', 'get_dark_theme_palette', 'get_dark_theme_stylesheet']
