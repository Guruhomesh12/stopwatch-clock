import tkinter as tk
from datetime import datetime
import time

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch and Clock")

        # Show the current time
        self.clock_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.clock_label.pack(pady=10)

        # Show the stopwatch time
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.stopwatch_label.pack(pady=20)

        # Start button
        self.start_button = tk.Button(root, text="Start", width=10, command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Stop button
        self.stop_button = tk.Button(root, text="Stop", width=10, command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", width=10, command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Variables to track stopwatch state
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Start updating the clock every second
        self.update_clock()

    def update_clock(self):
        # Update the clock display
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)  

        # If stopwatch is running, update stopwatch time
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.display_stopwatch(self.elapsed_time)

    def display_stopwatch(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        self.stopwatch_label.config(text=f"{hours:02d}:{minutes:02d}:{secs:02d}")

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()
