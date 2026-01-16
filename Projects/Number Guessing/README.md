# Number Guessing Game

A fun and interactive number guessing game built in Python where you try to guess a randomly chosen number between 1 and 100.

## Description

The program generates a random number and you have a limited number of attempts to guess it. After each guess, the program provides hints telling you whether your guess is too high or too low. The game offers two difficulty levels:

- **Easy Mode**: 10 attempts to guess the number
- **Hard Mode**: 5 attempts to guess the number

## How to Play

1. Run the program: `python main.py`
2. Choose your difficulty level by typing 'easy' or 'hard'
3. Make your guesses based on the hints provided
4. Win by guessing the correct number before running out of attempts!

## Features

- Two difficulty levels with different attempt counts
- Real-time feedback on each guess (Too High/Too Low)
- Remaining attempts counter
- Decorative ASCII art logo

## Files

- `main.py`: Main game logic and gameplay flow
- `art.py`: ASCII art logo for the game

## Requirements

- Python 3.x

## Example Game Flow

```
Choose difficulty level. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too High
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too Low
...
You got it! The answer was 37.
```

## Author

Created as part of Python learning projects.
