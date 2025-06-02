# Python Radio Player

A modern, modular radio player application built with Python and PySide6.

## Features

- Clean and modern dark theme UI
- System tray integration with custom icon
- Global hotkeys for play/pause and next station
- Volume control
- Station management through JSON configuration
- Minimize to tray functionality

## Prerequisites

- Python 3.7+
- VLC Media Player installed on your system

## Installation

1. Install the required Python packages:
```bash
pip install pillow python-vlc keyboard PySide6
```

2. Generate the application icon:
```bash
python src/generate_icon.py
```

3. Create a `radio_stations.json` file with your favorite radio stations:
```json
{
    "stations": [
        {
            "name": "Example Radio",
            "uri": "http://example.com/stream"
        }
    ]
}
```

## Usage

Run the application:
```bash
python src/main.py
```

### Global Hotkeys

- F7: Play/Pause
- F8: Next Station

### System Tray

The application can be minimized to the system tray. Right-click the tray icon for options:
- Show Radio Player
- Play/Pause
- Exit

## Project Structure

```
radio/
├── assets/               # Icons and resources
├── src/                  # Source code
│   ├── player/          # Radio player logic
│   ├── ui/              # User interface components
│   ├── config.py        # Configuration constants
│   ├── generate_icon.py # Icon generation script
│   └── main.py          # Application entry point
└── radio_stations.json  # Radio stations configuration
```

## Configuration

Edit `src/config.py` to customize:
- Default volume
- Hotkeys
- Radio stations file location
