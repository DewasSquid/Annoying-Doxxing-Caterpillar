import tkinter as tk
from tkvideo import tkvideo
from pygame import mixer
from screeninfo import get_monitors, Monitor
import config
import subprocess


class Video(tk.Toplevel):
    def __init__(self, monitor: Monitor, *args, **kwargs):
        super().__init__(
            cursor="none",
            *args,
            **kwargs
        )
        self.monitor = monitor
        self.setup_window()
        self.create_video_label()
        self.play_video()

    def setup_window(self):
        self.title(config.WINDOW_TITLE)
        self.geometry(f"{self.monitor.width}x{self.monitor.height}+{self.monitor.x}+{self.monitor.y}")
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", lambda: print("No!"))

    def create_video_label(self):
        self.video_label = tk.Label(
            self,
            compound=tk.CENTER,
            foreground="white",
            font=("Arial", config.TEXT_SIZE)
        )
        self.video_label.pack(fill=tk.BOTH, expand=True)
        
        self.update()
        self.video_label_size = (self.video_label.winfo_width(), self.video_label.winfo_height())

    def play_video(self):
        self.video = tkvideo(
            path=config.VIDEO_PATH,
            label=self.video_label,
            loop=True,
            size=self.video_label_size
        )
        self.video.play()

    def animate_text(self, text: str):
        text_length = len(text)
        text_index = 0
        max_display_length = 20*config.TEXT_SIZE

        def _animate():
            nonlocal text_index
            if text_index >= text_length:
                self.after(5000, self.safe_exit)
                return
            
            start_index = max(0, text_index - max_display_length)
            self.video_label.configure(text=text[start_index:text_index])
            text_index += config.TEXT_STEPS
            self.after(config.TEXT_INTERVAL, _animate)
        _animate()
    
    def safe_exit(self):
        self.destroy()
        exit(0)


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mixer.init()

        self.title(config.WINDOW_TITLE)
        self.iconify()  # Minimize the window
        self.overrideredirect(True)
        
        self.display_top_levels()
        self.play_music()
    
    def display_top_levels(self):
        total_text = ""
        for command in config.TEXT_COMMANDS:
            try:
                total_text += subprocess.check_output(command, encoding="oem")
            except Exception as e:
                print(e)
        
        for monitor in get_monitors():
            video = Video(monitor=monitor, master=self)
            video.animate_text(total_text)
    
    def play_music(self):
        self.music = mixer.Sound(config.MUSIC_PATH)
        self.music.set_volume(config.MUSIC_VOLUME)
        self.music.play(loops=-1)

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
