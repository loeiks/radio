import vlc
import json
from pathlib import Path

from src.config import (
    RADIO_STATIONS_FILE, DEFAULT_VOLUME
)

class RadioPlayer:
    def __init__(self):
        self._instance = vlc.Instance()
        self._player = self._instance.media_player_new()
        self._is_playing = False
        self.current_station_index = 0
        self.radio_stations = []
        self.on_state_changed = None  # Callback for state changes
        self.load_radio_stations()

    def load_radio_stations(self):
        """Loads radio station data from the JSON file."""
        try:
            stations_path = Path(__file__).parent.parent.parent / RADIO_STATIONS_FILE
            with open(stations_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.radio_stations = data.get('stations', [])
            return bool(self.radio_stations)
        except FileNotFoundError:
            print(f"Error: {RADIO_STATIONS_FILE} not found. Please create it with radio station data.")
            return False
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {RADIO_STATIONS_FILE}. Check file format.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while loading stations: {e}")
            return False

    def has_stations(self):
        """Check if there are any stations loaded."""
        return bool(self.radio_stations)

    def get_current_station(self):
        """Returns the current radio station dictionary."""
        if self.radio_stations and 0 <= self.current_station_index < len(self.radio_stations):
            return self.radio_stations[self.current_station_index]
        return None

    def play_station(self, station_uri):
        """Plays the given radio station URI."""
        if self._player:
            self._player.stop()

        try:
            media = self._instance.media_new(station_uri)
            self._player.set_media(media)
            self._player.audio_set_volume(DEFAULT_VOLUME)
            self._player.play()
            self._is_playing = True
        except Exception as e:
            print(f"Error playing station: {e}")
            self._is_playing = False

    def play_current_station(self):
        """Plays the current station."""
        station = self.get_current_station()
        if station:
            self.play_station(station['uri'])

    def toggle_play_pause(self):
        """Toggles play/pause state of the current radio."""
        if self._is_playing:
            self._player.pause()
        else:
            self._player.play()
        self._is_playing = not self._is_playing

        if self.on_state_changed:
            self.on_state_changed()

    def next_station(self):
        """Switches to the next radio station."""
        if not self.radio_stations:
            return

        self.current_station_index = (
            self.current_station_index + 1) % len(self.radio_stations)
        station = self.get_current_station()
        if station:
            self.play_station(station['uri'])
            self._is_playing = True
            if self.on_state_changed:
                self.on_state_changed()

    def previous_station(self):
        """Switches to the previous radio station."""
        if not self.radio_stations:
            return

        self.current_station_index = (
            self.current_station_index - 1) % len(self.radio_stations)
        station = self.get_current_station()
        if station:
            self.play_station(station['uri'])
            self._is_playing = True
            if self.on_state_changed:
                self.on_state_changed()

    def set_volume(self, volume):
        """Sets the player volume."""
        if self._player:
            self._player.audio_set_volume(int(volume))

    def stop(self):
        """Stop playback."""
        if self._player:
            self._player.stop()

    def cleanup(self):
        """Cleanup resources before closing."""
        self.stop()
        if self._instance:
            self._instance.release()
