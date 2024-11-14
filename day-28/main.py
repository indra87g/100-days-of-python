""" 
Day 28 - Text Operation GUI
"""
import tkinter as tk
from tkinter import StringVar

app = tk.Tk()
app.title("Text Operation GUI")
app.geometry("400x300")

def update_count(event=None):
    text = text_input.get("1.0", tk.END).strip()
    char_count.set(f"Total Character: {len(text)}")
    word_count.set(f"Total Words: {len(text.split())}")
    
def clear():
    text = text_input.get("1.0", tk.END).strip()
    text_input.delete("1.0", tk.END)
    update_count()

def to_uppercase():
    text = text_input.get("1.0", tk.END).strip().upper()
    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, text)
    update_count()
    
def to_lowercase ():
    text = text_input.get("1.0", tk.END).strip().lower()
    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, text)
    update_count()
    
def reverse_text():
    text = text_input.get("1.0", tk.END).strip()[::-1]
    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, text)
    update_count()
    
if __name__ == "__main__":
    text_input = tk.Text(app, wrap=tk.WORD, height=6)
    text_input.pack(pady=10)
    text_input.bind("<KeyRelease>>", update_count)
    
    char_count = StringVar()
    char_count.set("Total Character: 0")
    word_count = StringVar()
    word_count.set("Total Word: 0")
    
    char_count_label = tk.Label(app, textvariable=char_count)
    char_count_label.pack()
    
    word_count_label = tk.Label(app, textvariable=word_count)
    word_count_label.pack()
    
    btn_count = tk.Button(app, text="Count", command=update_count)
    btn_count.pack(side=tk.LEFT, padx=10, pady=20)
    
    btn_clear = tk.Button(app, text="Clear", command=clear)
    btn_clear.pack(side=tk.LEFT, padx=10)
    
    btn_upper = tk.Button(app, text="Uppercase", command=to_uppercase)
    btn_upper.pack(side=tk.LEFT, padx=10)
    
    btn_lower = tk.Button(app, text="Lowercase", command=to_lowercase)
    btn_lower.pack(side=tk.LEFT, padx=10)
    
    btn_reverse = tk.Button(app, text="Reverse", command=reverse_text)
    btn_reverse.pack(side=tk.LEFT, padx=10)
    
    app.mainloop()
