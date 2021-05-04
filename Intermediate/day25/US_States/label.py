from turtle import Turtle


class Label(Turtle):
    def __init__(self, state, x, y):
        super().__init__()

        self.text = state
        self.penup()
        self.hideturtle()
        self.goto(x, y)

    def write_state_name(self, alignment, font_size):
        self.write(self.text, align=alignment, font=("Aria", font_size, "normal"))
