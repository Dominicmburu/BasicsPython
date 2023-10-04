from day_17_question_model import Question
from day_17_data import question_data
from day_17_quiz_brain import QuizBrain
from day_17_UI import QuizInterface

question_bank = []


for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_question():
#     quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}") 



