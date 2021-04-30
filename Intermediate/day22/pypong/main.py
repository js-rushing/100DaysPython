import time
from turtle import Screen
from net import Net
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
sleep_time = .1

net = Net()
scoreboard = Scoreboard()
left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
screen.update()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

game_on = True
while game_on:
    collision = False
    while not collision:
        ball_return = False
        ball.move()
        time.sleep(sleep_time)
        screen.update()
        # Paddle misses ball
        if ball.xcor() >= 570 or ball.xcor() <= -580:
            collision = True
            sleep_time = .1
            if 270 > ball.ball_heading > 90:
                ball.reset_ball("left")
                scoreboard.right_score += 1
            else:
                ball.reset_ball("right")
                scoreboard.left_score += 1
            scoreboard.update_score()
            if scoreboard.is_game_over():
                ball.color("black")
                net.clear()
                left_paddle.color("black")
                right_paddle.color("black")
                screen.update()
                scoreboard.declare_winner()
                game_on = False
        # Ball bounces off floor or ceiling
        if ball.ycor() >= 430 or ball.ycor() <= -430:
            collision = True
        # Ball is returned by paddle
        if ball.xcor() > 520 and ball.distance(right_paddle.position()) < 40 \
                or ball.xcor() < -520 and ball.distance(left_paddle.position()) < 40:
            ball_return = True
        if collision and game_on:
            ball.bounce_boundary()
        if ball_return:
            if sleep_time > .03:
                sleep_time -= .005
            ball.bounce_paddle()
    screen.update()


screen.exitonclick()
