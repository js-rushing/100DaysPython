from turtle import Turtle
import random
START_POSITION = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.penup()
        self.goto(START_POSITION)
        self.ball_heading = 0
        self.aim_ball("right")

    def move(self):
        self.setheading(self.ball_heading)
        self.forward(20)

    def bounce_boundary(self):
        print(f"before {self.ball_heading}")
        new_heading = self.ball_heading
        if new_heading > 180:
            new_heading -= 180
            if new_heading > 90:
                new_heading -= (new_heading - 90) * 2
            else:
                new_heading += (90 - new_heading) * 2
        else:
            new_heading += 180
            if new_heading > 270:
                new_heading -= (new_heading - 270) * 2
            else:
                new_heading += (270 - new_heading) * 2
        self.ball_heading = new_heading
        print(f"after {self.ball_heading}")

    def bounce_paddle(self):
        new_heading = self.ball_heading
        if new_heading < 90 or new_heading > 270:
            if new_heading < 90:
                new_heading = 180 - new_heading
            else:
                new_heading = 180 + (360 - new_heading)
        else:
            if new_heading < 180:
                new_heading = 0 + (180 - new_heading)
            else:
                new_heading = 360 - (new_heading - 180)
        self.ball_heading = new_heading + random.randint(-30, 30)

    def aim_ball(self, direction):
        rand_num = random.randint(1, 2)
        if direction == "right":
            if rand_num == 1:
                self.ball_heading = random.randint(0, 30)
            else:
                self.ball_heading = random.randint(330, 359)
        else:
            self.ball_heading = random.randint(150, 210)

    def reset_ball(self, current_direction):
        self.goto(START_POSITION)
        if current_direction == "right":
            self.aim_ball("left")
        else:
            self.aim_ball("right")
