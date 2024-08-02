"""
Day 12 - Tkinter Timer
"""

import tkinter as tk
from tkinter import messagebox as msgb
import time


class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        self.time_input = tk.Entry(root, width=10)
        self.time_input.pack(pady=10)

        self.time_label = tk.Label(root, text="Time left: 0", font=("Helvetica", 24))
        self.time_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.RIGHT, padx=5)

        self.running = False
        self.time_left = 0

    def start(self):
        if not self.running:
            try:
                self.time_left = int(self.time_input.get())
                self.running = True
                self.update()
            except ValueError:
                msgb.showerror("Error", "Invalid time in second.")

    def stop(self):
        self.running = False

    def update(self):
        if self.running:
            if self.time_left > 0:
                self.time_label.config(text=f"Time left: {self.time_left}")
                self.time_left -= 1
                self.root.after(1000, self.update)
            else:
                self.running = False
                self.time_label.config(text="Time up!")
                msgb.showinfo("Timer App", "Time Up!")


if __name__ == "__main__":
    root = tk.Tk()
    app = Timer(root)
    root.mainloop()
