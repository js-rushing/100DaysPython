from turtle import Turtle, Screen
from random import sample, randint

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()
finish_line = Turtle()
finish_line.hideturtle()
turtles = [t1, t2, t3, t4, t5, t6]
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
winning_color = ""
screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def init_turtles():
    random_colors = sample(colors, len(colors))
    c = 0
    y = 175
    for turtle in turtles:
        turtle.turtlesize(1, 1, 1)
        turtle.setheading(0)
        turtle.shape("turtle")
        turtle.penup()
        y -= 50
        turtle.color(random_colors[c])
        turtle.setposition(-250, y)
        c += 1


def draw_finish_line():
    finish_line.penup()
    finish_line.setposition(250, 175)
    finish_line.setheading(270)
    finish_line.pendown()
    finish_line.forward(350)
    finish_line.hideturtle()


def race():
    global winning_color
    while not has_finished():
        for turtle in turtles:
            step = randint(0, 10)
            turtle.forward(step)
            if turtle.xcor() > 250:
                winning_color = turtle.pencolor()

    if has_finished():
        for turtle in turtles:
            if turtle.pencolor() == winning_color:
                turtle.setposition(0, 0)
                turtle.turtlesize(5, 5, 1)
                heading = 0
                for spin in range(int(360/5)):
                    heading += 5
                    turtle.setheading(heading)
        if user_bet == winning_color:
            screen.title("You win!")
        else:
            screen.title("You lose!")


def has_finished():
    turtle_finish = []
    for turtle in turtles:
        if turtle.xcor() > 250:
            turtle_finish.append(True)
    if True in turtle_finish:
        return True
    else:
        return False


init_turtles()
draw_finish_line()


screen.listen()
screen.onkey(key="space", fun=race)

screen.exitonclick()
