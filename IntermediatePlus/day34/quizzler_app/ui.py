from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
WHITE = "#eeeedd"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=340, height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0")
        self.score_label.config(font=("Arial", 12, "normal"), bg=THEME_COLOR, fg=WHITE)
        self.score_label.grid(column=1, row=0)

        self.question_box = Canvas(width=300, height=250)
        self.question_box.config(bg=WHITE)
        self.question_text = self.question_box.create_text(
            150,
            125,
            # setting the width forces wordwrap
            width=280,
            text="Hey",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.question_box.grid(column=0, row=1, columnspan=2, pady=40)

        true_img = PhotoImage(file="/home/boss/web/python/IntermediatePlus/day34/quizzler_app/images/true.png")
        self.true_btn = Button()
        self.true_btn.config(image=true_img, highlightthickness=0, command=self.true_click)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="/home/boss/web/python/IntermediatePlus/day34/quizzler_app/images/false.png")
        self.false_btn = Button()
        self.false_btn.config(image=false_img, highlightthickness=0, command=self.false_click)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_box.config(bg=WHITE)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_box.itemconfig(self.question_text, text=q_text)
        else:
            self.question_box.itemconfig(self.question_text,
                                         text=f"You've reached the end of the quiz.\n\n"
                                              f"You got {self.quiz.score} out of 10 correct.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_click(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_click(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_box.config(bg="green")
        else:
            self.question_box.config(bg="red")
        self.window.update()
        self.window.after(1000, self.get_next_question())
