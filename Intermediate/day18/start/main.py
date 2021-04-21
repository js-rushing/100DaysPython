# from turtle import Turtle, Screen
import turtle as t
from random import randint, choice

# import heroes
#
# for h in range(20):
#     print(heroes.gen())

tim = t.Turtle()
colors = ["#F7F6CF", "#B6D8F2", "#F4CFDF", "#5784BA", "#9AC8EB", "#CCD4BF", "#E7CBA9", "#EEBAB2"]
line_color = 0


def random_color_rgb():
    t.colormode(255)
    rgb_color = (randint(1, 255), randint(1, 255), randint(1, 255))
    return rgb_color


def random_color_hex():
    t.colormode(1.0)
    # VARIABLES
    letter_list = ['A', 'B', 'C', 'D', 'E', 'F']
    color_arr = []
    color = ""

    # Populate color array
    for n in range(0, 6):
        let_or_num = randint(1, 2)
        if let_or_num == 1:
            low_or_up = randint(1, 2)
            if low_or_up == 1:
                color_arr.append(choice(letter_list))
            else:
                color_arr.append(choice(letter_list).lower())
        else:
            color_arr.append(str(randint(0, 9)))

    # Generate color
    while len(color_arr) > 0:
        rand_num = randint(0, len(color_arr) - 1)
        color += color_arr[rand_num]
        color_arr.pop(rand_num)

    color = "#" + color

    return color


def draw_shape(sides, size):
    angle = 360 / sides
    for s in range(sides):
        tim.forward(size)
        tim.right(angle)


def random_walk(distance):
    tim.pensize(10)
    tim.speed("fastest")
    for d in range(distance):
        right_or_left = randint(1, 2)
        # tim.color(random_color_hex())
        tim.color(random_color_rgb())
        tim.forward(20)
        for t in range(0, randint(1, 4)):
            if right_or_left == 1:
                tim.right(90)
            else:
                tim.left(90)


def draw_spirograph(gap):
    for turn in range(round(360 / gap)):
        tim.color(random_color_rgb())
        tim.circle(100)
        tim.right(gap)


# DRAWING SHAPES
# for n in range(3, 11):
#     tim.color(colors[line_color])
#     draw_shape(n, 60)
#     if line_color < len(colors) - 1:
#         line_color += 1
#     else:
#         line_color = 0

# RANDOM WALK
# random_walk(200)

# SPIROGRAPH
tim.speed("fastest")
draw_spirograph(5)
tim.penup()
tim.left(90)
tim.forward(200)
tim.pendown()
draw_spirograph(5)
tim.penup()
tim.right(180)
tim.forward(400)
tim.pendown()
draw_spirograph(5)
tim.penup()
tim.left(180)
tim.forward(200)
tim.right(90)
tim.forward(200)
tim.pendown()
draw_spirograph(5)
tim.penup()
tim.left(180)
tim.forward(400)
tim.pendown()
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
