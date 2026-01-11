# Hangman Game

A classic word-guessing game implemented in Python with both console and GUI versions.

## Files

- `main.py`: Console-based version of the Hangman game.
- `gui.py`: Graphical User Interface version using Tkinter.
- `hangman_words.py`: Contains the list of words used in the game.
- `hangman_art.py`: Contains the ASCII art for the hangman stages and logo.

## How to Run

### Console Version
1. Ensure you have Python installed.
2. Navigate to the `Hangman` directory.
3. Run `python main.py` in the terminal.

### GUI Version
1. Ensure you have Python and Tkinter installed (Tkinter comes with most Python installations).
2. Navigate to the `Hangman` directory.
3. Run `python gui.py` to launch the graphical interface.

## Game Rules

- A random word is chosen from the word list.
- You have 6 lives to guess the word.
- Guess one letter at a time.
- If the letter is in the word, it will be revealed.
- If not, you lose a life and part of the hangman is drawn.
- Win by guessing all letters before running out of lives.
- Lose when the hangman is complete (6 wrong guesses).

## Requirements

- Python 3.x
- Tkinter (for GUI version, usually included with Python)

## Features

- Console and GUI versions available
- ASCII art hangman stages
- Input validation
- Win/lose detection
- New game functionality</content>
<parameter name="filePath">e:\Python Project\Projects\Hangman\README.md