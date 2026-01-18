import random
from game_data import data
import art


def random_data():
    compare = random.choice(data)
    return compare


def game_a():
    a_details = random_data()
    print(art.logo)
    print(f"Compare A: {a_details['name']}, {a_details['description']}, {a_details['country']}")
    return a_details


def game_b():
    b_details = random_data()
    print(art.vs)
    print(f"Against B: {b_details['name']}, {b_details['description']}, {b_details['country']}")
    return b_details


def download():
    choose = input("Who has more downloads? Type 'A' or 'B': ").lower()
    return choose


def calculate(a_downloads, b_downloads, choose, score):
    if choose == "a":
        if a_downloads > b_downloads:
            score += 1
            print(f"You're right! Current score: {score}")
            return score, "win"
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return score, "lose"
    elif choose == "b":
        if b_downloads > a_downloads:
            score += 1
            print(f"You're right! Current score: {score}")
            return score, "win"
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return score, "lose"
    else:
        return score, "invalid"


game_over = False
score = 0

while not game_over:
    dic_a = game_a()
    dic_b = game_b()
    choice = download()
    
    score, result = calculate(dic_a['downloads'], dic_b['downloads'], choice, score)
    
    if result == "lose":
        game_over = True
    elif result == "win":
        dic_a = dic_b  # Move to next round with dic_b as the new dic_a
    elif result == "invalid":
        print("Invalid choice. Try again.")
    else:
        print("May code have bugs. Please report if you find anyone.")


