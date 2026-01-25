# 🃏 Blackjack Game

Play a quick round of Blackjack against a computer dealer in the terminal.

## 📋 Description

This Python implementation follows classic Blackjack rules, handling Ace values dynamically and auto-playing the dealer's turn. ASCII art sets the mood for each hand.

## 🎯 Features

- 🤖 Computer dealer with standard hit/stand behavior
- 🂡 Ace handling (counts as 11 or 1 as needed)
- 🖼️ ASCII art logo
- 🔁 Replay loop to play multiple hands

## 📁 Project Structure

```
Black Jack/
├── art.py   # ASCII art logo
├── main.py  # Game logic
└── README.md
```

## 🚀 How to Run

```bash
python main.py
```

## 🕹️ How to Play

1. Run the game and choose to start a round.
2. Receive your initial two cards; the dealer shows one card.
3. Choose to `hit` or `stand` until you stick or bust.
4. The dealer draws to 17 and then stands; totals are compared to decide the winner.

## 📜 Rules Recap

- Goal: finish at or below 21 with a higher total than the dealer.
- Face cards = 10; Ace = 11 or 1 (auto-adjusted).
- Blackjack: 21 with exactly two cards.
- Dealer hits on 16 and stands on 17.

## 🛠️ Requirements

- Python 3.x