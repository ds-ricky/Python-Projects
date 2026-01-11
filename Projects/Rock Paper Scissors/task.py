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
print("Welcome to the rock paper scissors game.")
choice = int(input("What do you want to choose, Type 0 for rock, 1 for paper, 2 for scissors.\n"))
print(images[choice])
computer_choice = random.randint(0,2)
print(images[computer_choice])

if 3<choice<0:
    print("You typed invalid number.\nYou lose!")

if choice == computer_choice:
    print("Both choose same. Draw!")

if choice == 0 and computer_choice == 2:
    print("Congratulation!, You win!")
if computer_choice == 0 and choice == 2:
    print("You lose!")

if choice == 1 and computer_choice == 0:
    print("Congratulation!, You win!")
if computer_choice == 1 and choice == 0:
    print("You lose!")

if choice == 1 and computer_choice == 2:
    print("You lose!")
if computer_choice == 1 and choice == 2:
    print("Congratulation!, You win!")
