from turtle import Turtle
DASH_LENGTH = 10
DASH_WIDTH = 5
SPACE_LENGTH = 15


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 440)
        self.setheading(270)
        self.width(DASH_WIDTH)
        self.draw_net()

    def draw_net(self):
        self.speed("fastest")
        while self.ycor() > -440:
            self.pendown()
            self.forward(DASH_LENGTH)
            self.penup()
            self.forward(SPACE_LENGTH)
