from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    questions_text = questions["text"]
    questions_answers = questions["answer"]
    new_questions = Question(questions_text, questions_answers)
    question_bank.append(new_questions)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")