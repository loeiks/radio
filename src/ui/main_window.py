from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QSlider, QFrame, QSystemTrayIcon, QMenu, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction, QColor, QPalette
import os

from src.ui.ui_styles import get_dark_theme_palette, get_dark_theme_stylesheet
from src.player.radio_player import RadioPlayer
from src.config import DEFAULT_VOLUME

class RadioPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.radio_player = RadioPlayer()
        self.radio_player.on_state_changed = self.update_ui_for_station
        self.tray_icon = None
        
        self.setWindowTitle("Python Radio Player")
        self.setFixedSize(400, 300)
          # Load custom icon
        icon_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'radio_icon.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        self.init_ui()
        self.setup_tray_icon()
        
        # Initialize station if available
        if self.radio_player.has_stations():
            self.radio_player.play_current_station()
            self.update_ui_for_station()
        else:
            self.current_station_label.setText("No stations loaded.")
            self.play_pause_button.setText("▶ Play")
    
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Apply dark theme
        self.setPalette(get_dark_theme_palette())
        self.setStyleSheet(get_dark_theme_stylesheet())
        
        # Title Label
        title_label = QLabel("Radio Player")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("titleLabel")
        main_layout.addWidget(title_label)
        
        # Add UI components (stations, controls, volume)
        self._add_station_display(main_layout)
        self._add_control_buttons(main_layout)
        self._add_volume_control(main_layout)
        self._add_bottom_buttons(main_layout)
    
    def _add_station_display(self, layout):
        self.current_station_label = QLabel("Now Playing: -")
        self.current_station_label.setAlignment(Qt.AlignCenter)
        self.current_station_label.setObjectName("currentStationLabel")
        layout.addWidget(self.current_station_label)
        
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setObjectName("separator")
        layout.addWidget(separator)
    
    def _add_control_buttons(self, layout):
        control_layout = QHBoxLayout()
        control_layout.setAlignment(Qt.AlignCenter)
        control_layout.setSpacing(10)
        
        self.previous_button = QPushButton("⏮ Previous")
        self.previous_button.setObjectName("prevNextButton")
        self.previous_button.clicked.connect(self.previous_station)
        control_layout.addWidget(self.previous_button)
        
        self.play_pause_button = QPushButton("▶ Play")
        self.play_pause_button.setObjectName("playPauseButton")
        self.play_pause_button.clicked.connect(self.toggle_play_pause)
        control_layout.addWidget(self.play_pause_button)
        
        self.next_button = QPushButton("Next ⏭")
        self.next_button.setObjectName("prevNextButton")
        self.next_button.clicked.connect(self.next_station)
        control_layout.addWidget(self.next_button)
        
        layout.addLayout(control_layout)
    
    def _add_volume_control(self, layout):
        volume_layout = QHBoxLayout()
        volume_layout.setAlignment(Qt.AlignCenter)
        
        volume_label = QLabel("Volume:")
        volume_label.setStyleSheet("font-size: 16px; color: white;")
        volume_layout.addWidget(volume_label)
        
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(DEFAULT_VOLUME)
        self.volume_slider.setSingleStep(1)
        self.volume_slider.valueChanged.connect(self.radio_player.set_volume)
        self.volume_slider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        volume_layout.addWidget(self.volume_slider)
        
        layout.addLayout(volume_layout)
    
    def _add_bottom_buttons(self, layout):
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(10)
        
        self.minimize_button = QPushButton("Minimize to Tray")
        self.minimize_button.setObjectName("minimizeButton")
        self.minimize_button.clicked.connect(self.hide)
        button_layout.addWidget(self.minimize_button)
        
        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("exitButton")
        self.exit_button.clicked.connect(self.close_application)
        button_layout.addWidget(self.exit_button)
        
        layout.addLayout(button_layout)
    
    def setup_tray_icon(self):
        icon_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'radio_icon.ico')
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)
        self.tray_icon.setToolTip("Python Radio Player")
        
        tray_menu = QMenu()
        
        show_action = QAction("Show Radio Player", self)
        show_action.triggered.connect(self.show_window_from_tray)
        tray_menu.addAction(show_action)
        
        play_pause_action = QAction("Play/Pause", self)
        play_pause_action.triggered.connect(self.toggle_play_pause)
        tray_menu.addAction(play_pause_action)
        
        tray_menu.addSeparator()
        
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close_application)
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self._on_tray_activated)
        self.tray_icon.show()
    
    def _on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.show_window_from_tray()
    
    def show_window_from_tray(self):
        self.showNormal()
        self.activateWindow()
        self.raise_()
    
    def update_ui_for_station(self):
        station = self.radio_player.get_current_station()
        if station:
            self.current_station_label.setText(f"Now Playing: {station['name']}")
            self.play_pause_button.setText("⏸ Pause")
        else:
            self.current_station_label.setText("No station selected.")
            self.play_pause_button.setText("▶ Play")
    
    def next_station(self):
        """Wrapper to handle next station and update UI."""
        self.radio_player.next_station()
        self.update_ui_for_station()
    
    def previous_station(self):
        """Wrapper to handle previous station and update UI."""
        self.radio_player.previous_station()
        self.update_ui_for_station()
    
    def toggle_play_pause(self):
        """Wrapper to handle play/pause and update UI."""
        self.radio_player.toggle_play_pause()
        self.update_ui_for_station()
    
    def close_application(self):
        self.radio_player.cleanup()
        if self.tray_icon:
            self.tray_icon.hide()
        QApplication.instance().quit()
    
    def closeEvent(self, event):
        """Handle cleanup when the window is closed."""
        self.radio_player.stop()  # This will stop both playback and media key handler
        super().closeEvent(event)
