from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def back():
    tim.back(10)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(10)


def clear():
    tim.setposition(0, 0)
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
