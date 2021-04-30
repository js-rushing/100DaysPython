from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, orientation):
        super().__init__()
        self.orientation = orientation
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=4)
        self.penup()
        self.color("white")
        self.place_paddle(self.orientation)

    def place_paddle(self, orientation):
        if orientation == "left":
            self.goto(-550, 0)
        elif orientation == "right":
            self.goto(550, 0)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)
