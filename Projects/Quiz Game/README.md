# 🎮 Quiz Game

A fun and interactive **True/False quiz game** about video game trivia! Test your gaming knowledge with 25 questions covering gaming history, famous characters, and industry facts.

## 📋 Description

This is a console-based quiz game built with Python that features:
- 25 True/False questions about video game trivia
- Real-time score tracking
- Immediate feedback after each answer
- Final score summary at the end

## 🎯 Features

✅ Object-oriented design with separate classes for Question and QuizBrain  
✅ 25 curated questions about gaming history and trivia  
✅ User-friendly command-line interface  
✅ Score tracking throughout the game  
✅ Answer validation and feedback  

## 📁 Project Structure

```
Quiz Game/
├── main.py              # Main game loop and entry point
├── question_model.py    # Question class definition
├── quiz_brain.py        # Quiz logic and game mechanics
├── data.py              # Question database (25 True/False questions)
└── README.md            # Project documentation
```

## 🚀 How to Run

1. Make sure you have Python 3 installed
2. Navigate to the Quiz Game directory
3. Run the main file:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. The game will present you with questions one at a time
2. Answer each question by typing **True** or **False**
3. Get immediate feedback on your answer
4. See your current score after each question
5. Complete all 25 questions to see your final score!

## 💡 Sample Questions

- "Mario was originally called 'Jumpman' in Donkey Kong." ✅
- "The first video game ever created was Pong." ❌
- "Minecraft is the best-selling video game of all time." ✅
- "The Legend of Zelda protagonist's name is Zelda." ❌

## 🏆 Scoring

- Each correct answer: **+1 point**
- Your score is displayed after each question
- Final score shows: `Your final score was: X/25`

## 🛠️ Technical Details

### Classes

- **Question**: Stores question text and answer
- **QuizBrain**: Manages game flow, tracks score, and validates answers

### Key Methods

- `still_has_questions()`: Checks if there are more questions
- `next_question()`: Displays next question and gets user input
- `check_answer()`: Validates answer and updates score

## 📚 Learning Concepts

This project demonstrates:
- 🎓 Object-Oriented Programming (OOP)
- 🎓 Class initialization and methods
- 🎓 List comprehension and iteration
- 🎓 User input handling
- 🎓 Modular code organization

## 🎨 Future Enhancements

Some ideas for improvement:
- 📊 Add difficulty levels
- 🌐 Fetch questions from an API (e.g., Open Trivia Database)
- 💾 Save high scores
- ⏱️ Add time limits for answers
- 🎭 Add multiple categories

## 👨‍💻 Author

Part of the Python Projects collection

## 📜 License

This project is open source and available for educational purposes.

---

**Enjoy the quiz and test your gaming knowledge! 🎮🏆**
