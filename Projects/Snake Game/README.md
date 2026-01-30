# 🐍 Snake Game

A classic Snake Game implementation using Python's Turtle graphics library.

## 📖 Overview

This is a fun and interactive Snake Game where players control a snake to eat food and grow longer while avoiding collisions with walls and the snake's own body. The game features a score tracking system and a visually appealing interface.

## 🎮 Game Features

- 🕹️ **Classic Gameplay**: Control the snake with arrow keys to eat food and grow
- 📊 **Score Tracking**: Keep track of your current score and see game-over messages
- 💥 **Collision Detection**: Game ends if the snake hits the wall or itself
- 📈 **Progressive Growth**: The snake grows longer each time it eats food
- ⚡ **Smooth Movement**: Continuous snake movement with keyboard controls

## 📁 Project Structure

- 📄 **main.py**: The main game loop that initializes the game, handles events, and manages game logic
- 🐍 **snake.py**: Snake class that handles the snake's body, movement, and growth
- 🍎 **food.py**: Food class that manages food placement on the game board
- 🏆 **scoreboard.py**: Scoreboard class that tracks and displays the player's score

## ⚙️ Requirements

- 🐍 Python 3.x
- 🐢 Turtle graphics library (comes with Python)

## 🚀 How to Run

1. 📂 Navigate to the Snake Game directory:
   ```bash
   cd "Snake Game"
   ```

2. ▶️ Run the game:
   ```bash
   python main.py
   ```

## 🎮 Game Controls

- ⬆️ **Up Arrow**: Move snake upward
- ⬇️ **Down Arrow**: Move snake downward
- ⬅️ **Left Arrow**: Move snake leftward
- ➡️ **Right Arrow**: Move snake rightward

## 📋 Game Rules

1. ⌨️ Use the arrow keys to direct the snake
2. 🍎 Eat the food (red dot) to increase your score and grow longer
3. ⚠️ Avoid hitting the walls at the edges of the screen
4. ⚠️ Avoid colliding with the snake's own body
5. 💀 The game ends when you hit a wall or your own body

## 🪟 Game Window

- 📏 **Size**: 600x600 pixels
- 🎨 **Background**: Black
- ⚪ **Snake Color**: White
- 📍 **Game Area Boundaries**: ±280 pixels from center

## 📚 Dependencies

The game uses the following Python standard library:
- 🐢 `turtle`: For graphics and game rendering
- ⏱️ `time`: For controlling game speed

## 🎨 Customization

You can easily customize the game by modifying:
- 📏 **Screen size**: Change `width` and `height` parameters in `main.py`
- ⚡ **Game speed**: Adjust the `time.sleep()` value in the game loop
- 🎨 **Snake color**: Modify the `color()` call in `snake.py`
- 📐 **Snake size**: Change the `DISTANCE` constant in `snake.py`

🎉 Enjoy the game!
