import tkinter as tk
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

def play(choice):
    user_choice = choice
    computer_choice = random.randint(0, 2)
    
    user_label.config(text=f"You chose:\n{images[user_choice]}")
    comp_label.config(text=f"Computer chose:\n{images[computer_choice]}")
    
    if user_choice == computer_choice:
        result_label.config(text="It's a Draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        result_label.config(text="You Win!")
    else:
        result_label.config(text="You Lose!")

root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose your move:").pack()

button_frame = tk.Frame(root)
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", command=lambda: play(0))
rock_btn.pack(side=tk.LEFT)

paper_btn = tk.Button(button_frame, text="Paper", command=lambda: play(1))
paper_btn.pack(side=tk.LEFT)

scissors_btn = tk.Button(button_frame, text="Scissors", command=lambda: play(2))
scissors_btn.pack(side=tk.LEFT)

user_label = tk.Label(root, text="", font=("Courier", 10))
user_label.pack()

comp_label = tk.Label(root, text="", font=("Courier", 10))
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

root.mainloop()