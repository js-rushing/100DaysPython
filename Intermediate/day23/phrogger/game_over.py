from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
