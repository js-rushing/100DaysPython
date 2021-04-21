import turtle as t
from random import choice
import colorgram as cg

colors = cg.extract('download.jpeg', 14)
# colors = cg.extract('image_2.jpg', 14)

color_list = []
for color in colors:
    if color.rgb.r < 220 or color.rgb.g < 220 or color.rgb.b < 220:
        color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))


dot = t.Turtle()
t.colormode(255)
dot.speed("fastest")
dot.hideturtle()


def set_brush_position(brush, x, y):
    brush.penup()
    brush.setposition(x, y)
    brush.pendown()


def line_of_dots(brush, spacing, dot_size):
    brush.pendown()
    for b in range(0, 10):
        brush.color(choice(color_list))
        brush.dot(dot_size)
        brush.setheading(0)
        brush.penup()
        brush.forward(spacing)
        brush.pendown()
    brush.penup()


def draw_painting(brush, square_size):
    x = int(-square_size/2)
    y = int(square_size/2)
    dot_spacing = square_size/10
    dot_size = int(square_size*.04)

    set_brush_position(brush, x, y)
    for lines in range(0, 10):
        line_of_dots(brush, dot_spacing, dot_size)
        y -= dot_spacing
        set_brush_position(brush, x, y)


draw_painting(dot, 577)


screen = t.Screen()
screen.exitonclick()
