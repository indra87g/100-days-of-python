""" 
Day 26 - GUI Reminder App with Desktop Notification
"""
import tkinter as tk 
from tkinter import messagebox
from plyer import notification
import threading
import time

def send_notification(title, message, timeout):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )
    
def start_reminder():
    try:
        title = title_entry.get()
        message = message_entry.get()
        delay = int(time_entry.get())
        
        if title == "" or message == "" or delay <= 0:
            message.showerror("Input Error", "All field must filled.")
            return
        
        start_button.config(state="disabled")
        threading.Thread(target=run_timer, args=(delay, title, message)).start()
    except ValueError:
        messagebox.showerror("Input Error", "Time must be positive number.")
        
def run_timer(delay, title, message):
    time.sleep(delay)
    send_notification(title, message, 10)
    messagebox.showinfo("Reminder", f"Reminder: {title}\n\n{message}")
    
    start_button.config(state="normal")
    
app = tk.Tk()
app.title("Reminder App")
app.geometry("300x250")

tk.Label(app, text="Reminder Title:").pack(pady=5)
title_entry = tk.Entry(app, width=10)
title_entry.pack(pady=5)

tk.Label(app, text="Reminder Message:").pack(pady=5)
message_entry = tk.Entry(app, width=30)
message_entry.pack(pady=5)

tk.Label(app, text="Time (second):").pack(pady=5)
time_entry = tk.Entry(app, width=10)
time_entry.pack(pady=5)

start_button = tk.Button(app, text="Set Reminder", command=start_reminder)
start_button.pack(pady=20)

app.mainloop()
    