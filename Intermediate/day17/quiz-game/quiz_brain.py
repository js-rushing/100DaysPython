class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.evaluate_answer(user_answer, current_question.answer)

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("That's right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def more_questions(self):
        return self.question_number < len(self.question_list)

    def quiz_complete(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.score}/{len(self.question_list)}")