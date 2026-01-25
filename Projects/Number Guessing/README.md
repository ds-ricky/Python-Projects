# 🔢 Number Guessing Game

Guess the secret number between 1 and 100 before you run out of attempts.

## 📋 Description

The program picks a random number and challenges you to find it. Choose a difficulty, then use the high/low hints after each guess to close in on the answer.

## 🎯 Features

- 🎚️ Two difficulty levels: Easy (10 attempts) and Hard (5 attempts)
- 📣 Instant feedback if your guess is too high or too low
- ⏳ Attempts counter displayed each turn
- 🖼️ ASCII art banner to start the game

## 📁 Project Structure

```
Number Guessing/
├── art.py    # ASCII art logo
├── main.py   # Game logic and loop
└── README.md # Project documentation
```

## 🚀 How to Run

```bash
python main.py
```

## 🕹️ How to Play

1. Start the game and pick a difficulty (`easy` or `hard`).
2. Enter guesses; follow the "Too high" / "Too low" hints.
3. Win by guessing correctly before attempts hit zero.

## 🧪 Example Round

```
Choose difficulty level. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.
...
You got it! The answer was 37.
```

## 🛠️ Requirements

- Python 3.x
