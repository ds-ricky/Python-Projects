import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def start_game():
    print(art.logo)
    user_cards = []
    comp_cards = []
    user_score = -1
    comp_score = -1
    game = True

    while (len(user_cards) and len(comp_cards)) <2:
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while game:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score > 21 or comp_score == 0 or user_score == 0:
            game = False
        else:
            again = input("Do you want to pick a card?. Type 'yes or no'\n")
            if again == "yes":
                user_cards.append(deal_card())
            else:
                game = False

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    print("\n" * 20)
    start_game()