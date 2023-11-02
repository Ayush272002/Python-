import tkinter as tk
import random

round_count = 0
player_score = 0
computer_score = 0
results = []

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def selectionOfWinner(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        return "It's a tie!"
    elif ((player_choice == "Rock" and computer_choice == "Scissors") or
          (player_choice == "Paper" and computer_choice == "Rock") or
          (player_choice == "Scissors" and computer_choice == "Paper")):
        player_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def play(player_choice):
    global round_count
    if round_count < 3:
        computer_choice = get_computer_choice()
        result = selectionOfWinner(player_choice, computer_choice)
        results.append(f"Round {round_count + 1}: {player_choice} vs. {computer_choice}. {result}")
        result_label.config(text="\n".join(results))
        round_count += 1
        if round_count == 3:
            determine_winner()

def determine_winner():
    global player_score, computer_score
    if player_score > computer_score:
        results.append("You win the game!")
    elif player_score < computer_score:
        results.append("Computer wins the game!")
    else:
        results.append("It's a tie!")
    result_label.config(text="\n".join(results))
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)
    restart_button.config(state=tk.NORMAL)
    quit_button.config(state=tk.NORMAL)

def restart_game():
    global round_count, player_score, computer_score, results
    round_count = 0
    player_score = 0
    computer_score = 0
    results = []
    result_label.config(text="")
    restart_button.config(state=tk.DISABLED)
    quit_button.config(state=tk.DISABLED)
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)

def quit_game():
    window.quit()

window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("350x300")

instructions = tk.Label(window, text="Choose Rock, Paper, or Scissors:")
instructions.pack()

button_width = 15
button_height = 2

rock_button = tk.Button(window, text="Rock", command=lambda: play("Rock"), width=button_width, height=button_height)
paper_button = tk.Button(window, text="Paper", command=lambda: play("Paper"), width=button_width, height=button_height)
scissors_button = tk.Button(window, text="Scissors", command=lambda: play("Scissors"), width=button_width, height=button_height)
restart_button = tk.Button(window, text="Restart", command=restart_game, width=button_width, height=button_height, state=tk.DISABLED)
quit_button = tk.Button(window, text="Quit", command=quit_game, width=button_width, height=button_height, state=tk.DISABLED)

rock_button.pack()
paper_button.pack()
scissors_button.pack()
restart_button.pack()
quit_button.pack()

result_label = tk.Label(window, text="", justify="left")
result_label.pack()

window.mainloop()
