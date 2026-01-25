# ✊🧻✂️ Rock Paper Scissors

Play the classic hand game against the computer via a lightweight CLI or a simple Tkinter GUI.

## 📋 Description

Choose rock, paper, or scissors and see if you can beat the computer's random pick. The CLI version shows ASCII art for each choice, while the GUI version provides buttons for quick play.

## 🎯 Features

- 🤖 Computer opponent with randomized choices
- 🖼️ ASCII art for each selection in the CLI version
- 🪟 Optional Tkinter GUI for click-to-play controls
- 🔁 Replay loop so you can keep playing rounds

## 📁 Project Structure

```
Rock Paper Scissors/
├── project.py  # Command-line game logic
├── gui.py      # Tkinter GUI version
└── README.md   # Project documentation
```

## 🚀 How to Run

CLI version:

```bash
python project.py
```

GUI version:

```bash
python gui.py
```

## 🕹️ How to Play

1. Pick rock (0), paper (1), or scissors (2) in the CLI, or click the button in the GUI.
2. The computer reveals its choice.
3. Results follow the rules: rock beats scissors, scissors beats paper, paper beats rock; same choice is a draw.
4. Play another round or exit.

## 🛠️ Requirements

- Python 3.x (Tkinter ships with standard Python installations)