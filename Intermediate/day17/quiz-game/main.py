from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_item = Question(question["question"], question["correct_answer"])
    question_bank.append(question_item)

quiz = QuizBrain(question_bank)

while quiz.more_questions():
    quiz.next_question()


quiz.quiz_complete()
