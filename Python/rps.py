import random
import tkinter as tk
from tkinter import ttk

class RPSGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")

        # Create frames
        self.user_frame = ttk.Frame(master, padding=10)
        self.computer_frame = ttk.Frame(master, padding=10)
        self.result_frame = ttk.Frame(master, padding=10)
        self.button_frame = ttk.Frame(master, padding=10)
        self.user_frame.pack()
        self.computer_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

        # Create labels
        self.user_label = ttk.Label(self.user_frame, text="Your choice:", font=("Helvetica", 12))
        self.computer_label = ttk.Label(self.computer_frame, text="Computer's choice:", font=("Helvetica", 12))
        self.result_label = ttk.Label(self.result_frame, text="", font=("Helvetica", 18, "bold"))
        self.user_label.pack(side="left")
        self.computer_label.pack(side="left")
        self.result_label.pack()

    

        # Create buttons
        self.rock_button = ttk.Button(self.button_frame, image=self.rock_image, command=lambda: self.play("rock"))
        self.paper_button = ttk.Button(self.button_frame, image=self.paper_image, command=lambda: self.play("paper"))
        self.scissors_button = ttk.Button(self.button_frame, image=self.scissors_image, command=lambda: self.play("scissors"))
        self.rock_button.pack(side="left", padx=10)
        self.paper_button.pack(side="left", padx=10)
        self.scissors_button.pack(side="left", padx=10)

        # Create quit button
        self.quit_button = ttk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(side="bottom", pady=10)

    def play(self, user_choice):
        # Generate computer choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine winner
        if user_choice == computer_choice:
            result = f"Tie! Both players chose {user_choice}."
        elif user_choice == "rock":
            if computer_choice == "paper":
                result = "You lose! Paper covers rock."
            else:
                result = "You win! Rock smashes scissors."
        elif user_choice == "paper":
            if computer_choice == "scissors":
                result = "You lose! Scissors cut paper."
            else:
                result = "You win! Paper covers rock."
        elif user_choice == "scissors":
            if computer_choice == "rock":
                result = "You lose! Rock smashes scissors."
            else:
                result = "You win! Scissors cut paper."
        else:
            result = "Invalid input. Please try again."

        # Update labels
        self.user_label.configure(text=f"Your choice: {user_choice.capitalize()}")
        self.computer_label.configure(text=f"Computer's choice: {computer_choice.capitalize()}")
        self.result_label.configure(text=result)

# Create the GUI
root = tk.Tk()
game = RPSGame(root)
root.mainloop()

