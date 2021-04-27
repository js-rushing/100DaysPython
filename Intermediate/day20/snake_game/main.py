import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("THERPENTH")
screen.tracer(0)
snake_body = []
game_on = True
sleep_time = .005
current_heading = 0


def make_square(size, color):
    STAMP_SIZE = 20
    stretch = size/STAMP_SIZE
    square = Turtle()
    square.shape("square")
    square.color(color)
    square.shapesize(stretch_wid=stretch, stretch_len=stretch, outline=1)
    square.penup()
    # square.speed("fast")

    return square


def place_squares(body, head_x, head_y):
    x_displacement = head_x
    for square in body:
        square.setposition(head_x + x_displacement, head_y)
        x_displacement -= 20


def move(body):
    for piece in body:
        piece.forward(1)
    time.sleep(sleep_time)
    screen.update()


def turn(body, heading):
    temp_square = make_square(20, "white")
    temp_square.setposition(body[0].position())
    temp_square.setheading(heading)
    global sleep_time
    for sect in body:
        sect.setheading(heading)
        for steps in range(0, 20):
            for piece in body:
                piece.forward(1)
                time.sleep(sleep_time)
                if temp_square.position() == body[len(body) - 1].position():
                    temp_square.hideturtle()
            screen.update()
    # temp_square.forward(1)
    # screen.update()
    # temp_square.hideturtle()
    # screen.update()


def turn_left():
    global snake_body
    global current_heading
    current_heading += 90
    turn(snake_body, current_heading)


def turn_right():
    global snake_body
    global current_heading
    current_heading += 270
    turn(snake_body, current_heading)


for section in range(0, 6):
    snake_body.append(make_square(20, "white"))

head_pos_x = snake_body[0].position()[0]
head_pos_y = snake_body[0].position()[1]

place_squares(snake_body, head_pos_x, head_pos_y)

screen.update()

# while game_on:
#     move(snake_body)

while game_on:
    for n in range(0, 8):
        move(snake_body)
    turn_left()
    for n in range(0, 8):
        move(snake_body)
    turn_right()
    for n in range(0, 8):
        move(snake_body)
    turn_left()
    for n in range(0, 8):
        move(snake_body)
    turn_left()

screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.exitonclick()
