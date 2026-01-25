# 📈 Higher or Lower

Guess which game or app has more downloads in this fast-paced command-line challenge.

## 📋 Description

Two contenders are shown each round. Pick which one has the higher download count, stack up points, and keep going until you miss. The winner of a round stays on as the next challenger.

## 🎯 Features

- 🗂️ 50+ games and apps covering mobile, PC, and console titles
- 📊 Score tracking that updates every correct answer
- 🔁 Winner-stays-on mechanic for escalating comparisons
- ✅ Input validation to catch typos before ending your streak

## 📁 Project Structure

```
Higher or Lower/
├── art.py        # ASCII art for the logo and VS graphic
├── game_data.py  # Dataset of games/apps with download counts
├── main.py       # Game loop and logic
└── README.md     # Project documentation
```

## 🚀 How to Run

```bash
python main.py
```

## 🕹️ How to Play

1. Two options (A and B) are displayed with brief descriptions.
2. Type `A` or `B` to choose the one you believe has more downloads.
3. Correct picks increase your score and move you to the next round.
4. One wrong answer ends the game and shows your final score.

## 🧪 Example Gameplay

```
Compare A: PUBG Mobile, Battle royale mobile game, South Korea

Against B: Angry Birds, Physics-based puzzle game, Finland
Who has more downloads? Type 'A' or 'B': b
You're right! Current score: 1
```

## 🛠️ Requirements

- Python 3.x
