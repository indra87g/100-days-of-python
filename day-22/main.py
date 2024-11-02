"""
Day 22 - Tkinter AI Rock Paper Scissor
"""

import tkinter as tk
from tkinter import messagebox
import random

app = tk.Tk()
app.title("Tkinter AI Rock Paper Scissor")


def determine_winner(human_choice, ai_choice):
    if human_choice == ai_choice:
        return "It's a tie!"
    elif (
        (human_choice == "Scissor" and ai_choice == "Paper")
        or (human_choice == "Rock" and ai_choice == "Scissor")
        or (human_choice == "Paper" and ai_choice == "Rock")
    ):
        return "You Win!"
    else:
        return "AI Win!"


def make_choice(human_choice):
    ai_choice = random.choice(["Rock", "Paper", "Scissor"])
    result = determine_winner(human_choice, ai_choice)
    result_label.config(
        text=f"You: {human_choice} | AI: {ai_choice} | Result: {result}"
    )


btn_rock = tk.Button(app, text="Rock", command=lambda: make_choice("Rock"))
btn_rock.pack(side=tk.LEFT, padx=10)

btn_paper = tk.Button(app, text="Paper", command=lambda: make_choice("Paper"))
btn_paper.pack(side=tk.LEFT, padx=10)

btn_scissor = tk.Button(app, text="Scissor", command=lambda: make_choice("Scissor"))
btn_scissor.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(app, text="Select your choice to start!")
result_label.pack(pady=30, padx=10)

app.mainloop()
