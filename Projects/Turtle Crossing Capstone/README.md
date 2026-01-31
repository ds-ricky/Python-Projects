# 🐢 Turtle Crossing Game

A fun and challenging arcade-style game built with Python's Turtle module! Help the turtle cross the busy road while avoiding colorful cars. Each successful crossing increases the difficulty! 🚗💨

## 📋 Description

This is a classic **Frogger-style** game where you control a turtle trying to cross a busy highway. The cars move from right to left at increasing speeds as you progress through levels. One collision and it's game over!

## ✨ Features

- 🎮 **Simple Controls**: Use the Up arrow key to move the turtle forward
- 🏎️ **Dynamic Difficulty**: Cars move faster with each level
- 🌈 **Colorful Graphics**: Random colored cars (red, orange, yellow, green, blue, purple)
- 📊 **Level Tracking**: Real-time level display showing your progress
- 🎯 **Collision Detection**: Precise detection when the turtle gets too close to cars

## 🎯 How to Play

1. **Start the Game**: Run `main.py` to begin
2. **Move Forward**: Press the **Up Arrow** key to move the turtle upward
3. **Avoid Cars**: Don't let the turtle collide with any passing cars
4. **Reach the Top**: Guide the turtle to the finish line at the top of the screen
5. **Level Up**: Successfully crossing increases your level and car speed
6. **Game Over**: The game ends when you collide with a car

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Turtle module (comes pre-installed with Python)

### Installation

1. Clone or download this project
2. Navigate to the project directory
3. Run the game:

```bash
python main.py
```

## 📁 File Structure

```
Turtle Crossing Capstone/
│
├── main.py           # 🎮 Main game loop and logic
├── player.py         # 🐢 Player (turtle) class and movement
├── car_manager.py    # 🚗 Car generation and management
├── scoreboard.py     # 📊 Level display and game over screen
└── README.md         # 📖 This file
```

## 🎨 Game Components

### Player (player.py)
- 🐢 Turtle-shaped character
- Starting position at the bottom of the screen
- Moves forward with each Up arrow press
- Resets to starting position after each successful crossing

### Car Manager (car_manager.py)
- 🚗 Generates random cars at random intervals
- Cars appear in 6 different colors
- Speed increases with each level
- Cars move from right to left across the screen

### Scoreboard (scoreboard.py)
- 📊 Displays current level in the top-left corner
- Shows "Game Over" message when collision occurs
- Automatically updates when player levels up

## 🎲 Game Mechanics

- **Starting Speed**: Cars begin at a moderate pace
- **Speed Increase**: Each level adds 10 units to car speed
- **Collision Distance**: 25 pixels (game over if turtle gets this close to a car)
- **Finish Line**: 280 pixels from center (top of screen)
- **Car Spawn Rate**: 1 in 6 chance per frame

## 🏆 Tips & Strategies

1. ⏱️ **Timing is Everything**: Wait for gaps in traffic before moving forward
2. 👀 **Watch Multiple Lanes**: Cars spawn at random Y positions
3. 🐢 **Steady Pace**: You can't move backward, so plan your moves carefully
4. 🎯 **Focus on Speed Changes**: Each level makes the game progressively harder

## 🛠️ Customization Ideas

Want to modify the game? Here are some ideas:

- 🎨 Change the color palette in `car_manager.py`
- ⚡ Adjust difficulty by modifying `MOVE_INCREMENT` and `STARTING_MOVE_DISTANCE`
- 🐢 Change the player shape or color in `player.py`
- 📊 Add a high score system to `scoreboard.py`
- 🎵 Add sound effects for crossing and collisions

## 📚 Learning Concepts

This project demonstrates:

- ✅ Object-Oriented Programming (OOP)
- ✅ Game loop implementation
- ✅ Collision detection
- ✅ Event handling (keyboard input)
- ✅ Progressive difficulty scaling
- ✅ Turtle graphics module

## 🐛 Known Issues

None currently! If you find any bugs, feel free to report them.

## 📄 License

This project is part of a Python learning journey. Feel free to use and modify as needed!

## 🎉 Enjoy the Game!

Good luck crossing the road! 🐢🏁

---

Made with 💚 and Python 🐍
