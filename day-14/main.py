"""
Day 14 - Tkinter Color Toggler
"""

import tkinter as tk


def toggle_theme():
    global is_dark_mode
    if is_dark_mode:
        window.config(bg="white")
        label.config(bg="white", fg="black")
        toggle_button.config(bg="lightgray", fg="black", text="Switch to Dark Mode")
        is_dark_mode = False
    else:
        window.config(bg="black")
        label.config(bg="black", fg="white")
        toggle_button.config(bg="gray", fg="white", text="Switch to Light Mode")
        is_dark_mode = True


window = tk.Tk()
window.title("Tkinter Color Toggler")
is_dark_mode = False

label = tk.Label(window, text="Hello World!", font=("Arial", 24))
label.pack(pady=20)

toggle_button = tk.Button(window, text="Switch to Dark Mode", command=toggle_theme)
toggle_button.pack(pady=10)

window.config(bg="white")
label.config(bg="white", fg="black")
toggle_button.config(bg="lightgray", fg="black")

window.mainloop()
