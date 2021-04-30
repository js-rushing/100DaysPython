from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Arial", 16, "normal")
SCREEN_SIZE = 600


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-int(SCREEN_SIZE * .45), int(SCREEN_SIZE * .425))
        self.update_level()

    def level_up(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def end_game(self):
        # self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
