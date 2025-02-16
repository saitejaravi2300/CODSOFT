import tkinter as tk
import random 

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.configure(bg="light green")  

user_score = 0
computer_score = 0

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg="light green")
instruction_label.pack()

user_choice_var = tk.StringVar()
user_choice_var.set("Rock")
user_choice_options = ["Rock", "Paper", "Scissors"]
user_choice_menu = tk.OptionMenu(root, user_choice_var, *user_choice_options)
user_choice_menu.pack()

play_button = tk.Button(root, text="Play", command=lambda: play_round())
play_button.pack()

user_choice_label = tk.Label(root, text="", bg="light green")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="", bg="light green")
computer_choice_label.pack()

result_label = tk.Label(root, text="", bg="light green")
result_label.pack()

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", bg="light green")
score_label.pack()

def play_round():
    global user_score, computer_score

    user_choice = user_choice_var.get()
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or 
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

new_game_button = tk.Button(root, text="New Game", command=reset_scores)
new_game_button.pack()

root.mainloop()
