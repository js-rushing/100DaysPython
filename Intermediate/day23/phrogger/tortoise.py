from turtle import Turtle
SCREEN_SIZE = 600


class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(125, 255, 165)
        self.setheading(90)
        self.penup()
        self.to_start()

    def jump(self):
        self.forward(30)

    def has_crossed_finish(self):
        if self.ycor() > int(SCREEN_SIZE * .35):
            return True
        else:
            return False

    def to_start(self):
        self.goto(0, -int(SCREEN_SIZE * .45))

    def do_nothing(self):
        pass
