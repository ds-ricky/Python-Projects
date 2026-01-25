# 🪓 Hangman (Console)

Guess the hidden word one letter at a time before the hangman is complete.

## 📋 Description

This Python console version of Hangman selects a random word and challenges you to uncover it with limited lives. ASCII art tracks your progress after each guess.

## 🎯 Features

- 🎨 ASCII art for each hangman stage and the game logo
- 🧠 Curated word list to keep rounds varied
- ✅ Input validation and win/lose detection
- 🔁 Play-again prompt to start a new round quickly

## 📁 Project Structure

```
Hangman/
├── hangman_art.py   # ASCII art for stages and logo
├── hangman_words.py # Word list
├── main.py          # Game loop and logic
└── README.md        # Project documentation
```

## 🚀 How to Run

```bash
python main.py
```

## 🕹️ How to Play

1. The game picks a random word and shows blanks.
2. Guess one letter at a time.
3. Correct letters fill in their positions; wrong guesses cost a life and advance the hangman art.
4. Win by revealing the full word before lives reach zero.

## 🛠️ Requirements

- Python 3.x