# Higher or Lower Game

A fun and interactive command-line game where you guess which famous game or app has more downloads!

## Overview

In this game, you're presented with two games/apps and must decide which one has more downloads. The game keeps track of your score as you progress. One wrong answer and it's game over!

## How to Play

1. Run the program: `python main.py`
2. Two games/apps will be displayed (A and B)
3. Type **'A'** or **'B'** to choose which one has more downloads
4. Get it right and your score increases, then move to the next comparison
5. Get it wrong and the game ends with your final score
6. The winner from each round becomes option A in the next round

## Features

- **50+ Games/Apps** in the database including mobile games, PC games, and console games
- **Progressive Difficulty** - Winners stay as option A for the next round
- **Score Tracking** - Your current score is displayed after each correct answer
- **Input Validation** - Invalid inputs are caught and you can try again

## Files

- `main.py` - Main game logic
- `game_data.py` - Database of games/apps with download counts
- `art.py` - ASCII art for the game logo and VS symbol

## Requirements

- Python 3.x

## Example Gameplay

```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: PUBG Mobile, Battle royale mobile game, South Korea
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Angry Birds, Physics-based puzzle game, Finland
Who has more downloads? Type 'A' or 'B': b
You're right! Current score: 1
```

## Game Data

The game includes popular titles such as:
- Mobile games: PUBG Mobile, Free Fire, Subway Surfers, Candy Crush
- PC games: Minecraft, GTA V, Fortnite, League of Legends
- Console games: Roblox, Apex Legends, Elden Ring
