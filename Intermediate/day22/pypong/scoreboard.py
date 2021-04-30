from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")
PLAY_TO = 3


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 360)
        # self.write(f"{self.left_score}         {self.right_score}", align=ALIGNMENT, font=FONT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}         {self.right_score}", align=ALIGNMENT, font=FONT)

    def is_game_over(self):
        if self.left_score >= PLAY_TO and self.left_score - self.right_score > 1 \
                or self.right_score >= PLAY_TO and self.right_score - self.left_score > 1:
            return True
        else:
            return False

    def declare_winner(self):
        self.clear()
        self.goto(0, 0)
        if self.left_score > self.right_score:
            winner = "Player 1"
        else:
            winner = "Player 2"
        self.write(f"{winner} won!", align=ALIGNMENT, font=FONT)

