import tkinter as tk
import random
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Stone Paper Scissors Game")
root.geometry("400x400")
root.resizable(False, False)

# Choices
choices = ["Stone", "Paper", "Scissors"]

# Functions
def play(user_choice):
    comp_choice = random.choice(choices)
    result = ""
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Stone" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Stone") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    result_label.config(text=f"You: {user_choice}\nComputer: {comp_choice}\n{result}")

def reset():
    result_label.config(text="Make your move!")

# UI Elements
label = tk.Label(root, text="Stone Paper Scissors", font=("Arial", 20, "bold"))
label.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

stone_btn = tk.Button(frame, text="Stone", width=10, height=2, command=lambda: play("Stone"))
paper_btn = tk.Button(frame, text="Paper", width=10, height=2, command=lambda: play("Paper"))
scissors_btn = tk.Button(frame, text="Scissors", width=10, height=2, command=lambda: play("Scissors"))

stone_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14))
result_label.pack(pady=30)

reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.pack(pady=10)

root.mainloop()