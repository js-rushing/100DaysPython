from turtle import Turtle
import random
SCREEN_SIZE = 600


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = 5
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.paint_car()
        self.choose_lane()

    def paint_car(self):
        # colors = ["green", "yellow", "violet", "red", "blue"]
        rgb_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        # self.color(colors[random.randint(0, len(colors) - 1)])
        self.color(rgb_color)

    def choose_lane(self):
        start_line = -int((SCREEN_SIZE * .45) - 30)
        finish_line = int(SCREEN_SIZE * .35)
        xcor = int(SCREEN_SIZE * .45)
        ycor = start_line
        ycor_list = []
        while ycor < finish_line:
            ycor_list.append(ycor)
            ycor += 30
        self.goto(xcor + random.randint(0, (SCREEN_SIZE / 2)),
                  ycor_list[random.randint(0, len(ycor_list) - 1)])

    def drive(self):
        self.forward(self.move_distance)

    def speed_up(self):
        self.move_distance += 2
