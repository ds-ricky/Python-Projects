import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose difficulty level. Type 'easy' or 'hard': ").lower()

num = random.randint(1,100)

def calculate(life):
    won = False
    while not won:
        print(f"You have {life} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == num:
            won = True
            print(f"You got it! The answer was {num}.")
        elif guess > num:
            life -= 1
            print("Too High")
        elif guess < num:
            life -= 1
            print("Too Low")
        if life == 0:
            won = True
            print(f"You've run out of guesses, The answer was {num}.")
    return None


if difficulty == "easy":
    life = 10
    calculate(life)
elif difficulty == "hard":
    life = 5
    calculate(life)

