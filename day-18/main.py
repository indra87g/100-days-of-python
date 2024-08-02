"""
Day 18 - Tkinter Lucky Spin
"""

import tkinter as tk
import random


class LuckySpin:
    def __init__(self, root):
        self.root = root
        self.root.title("Lucky Spin")

        self.root.geometry("300x200")

        self.result_label = tk.Label(
            root, text="Click 'Spin' to try your luck!", font=("Helvetica", 14)
        )
        self.result_label.pack(pady=20)

        self.spin_button = tk.Button(
            root, text="Spin", command=self.spin, font=("Helvetica", 12)
        )
        self.spin_button.pack(pady=10)

    def spin(self):
        options = ["🍒🍒🔔", "🔔🍇🍇", "🍇🍒🍒", "🔔🔔🔔\n JACKPOT", "🔔🍇🔔", "🍇🍒🔔"]
        result = random.choice(options)
        self.result_label.config(text=f"You got:\n {result}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LuckySpin(root)
    root.mainloop()
