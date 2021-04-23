from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def turn_right():
    tim.right(5)


def turn_left():
    tim.right(5)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.exitonclick()
