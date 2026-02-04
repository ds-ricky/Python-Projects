# 🍅 Pomodoro Timer

A simple and elegant Pomodoro Timer application built with Python and Tkinter to help you boost your productivity! ⏱️

## 📖 About

The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This application implements the classic Pomodoro workflow:

- 🔴 **Work Session**: 25 minutes of focused work
- ☕ **Short Break**: 5 minutes of rest
- 🌴 **Long Break**: 20 minutes of rest (after 4 work sessions)

## ✨ Features

- ⏰ Automatic timer countdown
- 🎨 Color-coded sessions (Work in green, breaks in pink/red)
- ✅ Visual checkmarks to track completed work sessions
- 🔄 Reset functionality to start over
- 🖼️ Beautiful tomato-themed UI

## 🚀 How to Use

1. **Start**: Click the "Start" button to begin your first Pomodoro session
2. **Work**: Focus on your task for 25 minutes
3. **Break**: Take a 5-minute break when the timer ends
4. **Repeat**: After 4 work sessions, enjoy a longer 20-minute break
5. **Reset**: Click "Reset" to restart the cycle anytime

## 🛠️ Requirements

- Python 3.x 🐍
- Tkinter (usually comes pre-installed with Python)
- `tomato.png` image file in the same directory 🍅

## 💻 Installation & Running

1. Ensure you have Python installed on your system
2. Clone or download this project
3. Make sure `tomato.png` is in the same directory as `main.py`
4. Run the application:
   ```bash
   python main.py
   ```

## 🎮 Controls

- **Start Button**: Begin or continue the Pomodoro cycle
- **Reset Button**: Stop the timer and reset to the initial state

## 📊 Progress Tracking

The app displays checkmarks (✔️) at the bottom for each completed work session, helping you visualize your productivity throughout the day!

## 🎨 Customization

You can easily customize the timer durations by modifying these constants in the code:
- `WORK_MIN`: Work session duration (default: 25 minutes)
- `SHORT_BREAK_MIN`: Short break duration (default: 5 minutes)
- `LONG_BREAK_MIN`: Long break duration (default: 20 minutes)

## 📝 License

This project is part of a Python learning journey. Feel free to use and modify it! 🚀

---

Made with ❤️ and Python
