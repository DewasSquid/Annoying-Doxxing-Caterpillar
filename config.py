import sys
import os

def resource_path(relative_path):
    """Support for pyinstaller"""
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Title for the main window.
WINDOW_TITLE = "Doxxing Caterpillar"
# Path to the video file for playback.
VIDEO_PATH = resource_path("assets/video.mp4")
# Path to the audio file for background music.
MUSIC_PATH = resource_path("assets/audio.mp3")
# Volume level for the background music (0.0 to 1.0).
MUSIC_VOLUME = .1
# List of system commands to retrieve information for display.
TEXT_COMMANDS = ["ipconfig", "systeminfo", "netsh wlan show profiles"]
# Font size of the information text
TEXT_SIZE = 30
# Interval (in milliseconds) for updating the displayed text.
TEXT_INTERVAL = 10
# Number of characters to increment in each update.
TEXT_STEPS = 5