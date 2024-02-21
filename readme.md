# Annoying Doxxing Caterpillar

## Overview
This aims to replicate the infamous "Doxxing Caterpillar" video on your machine. Using your hardware, this application creates a humorous experience featuring the legendary green caterpillar meme.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/krater-caterpillar.git
   cd krater-caterpillar
   ```

2. Ensure you have the required Python packages installed by running:
    ```bash
    pip install -r requirements.txt
    ```

# Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. The main window will be minimized, and videos will be displayed on each connected monitor with animated system information and the legendary "Krater Caterpillar" meme.

## Configuration
Customize configuration settings in the `config.py` file based on your preferences.

### config.py
- **WINDOW_TITLE:** Title for the main window.
- **VIDEO_PATH:** Path to the video file for playback.
- **MUSIC_PATH:** Path to the audio file for background music.
- **MUSIC_VOLUME:** Volume level for the background music (0.0 to 1.0).
- **TEXT_COMMANDS:** List of system commands to retrieve information for display.
- **TEXT_INTERVAL:** Interval (in milliseconds) for updating the displayed text.
- **TEXT_STEPS:** Number of characters to increment in each animation step.

## License
This project is licensed under the [MIT License](LICENSE).

---