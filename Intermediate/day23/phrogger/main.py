from turtle import Screen
from tortoise import Tortoise
from level import Level
from game_over import GameOver
from car import Car
import time
SCREEN_SIZE = 600

screen = Screen()
screen.bgcolor("white")
screen.colormode(255)
screen.tracer(0)
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
sleep_time = .1

tim = Tortoise()
level = Level()
num_of_cars = 5
car_list = []

for c in range(0, num_of_cars):
    car_list.append(Car())

screen.update()
screen.listen()
screen.onkeypress(tim.jump, "Up")

game_on = True
while game_on:
    time.sleep(sleep_time)
    screen.update()
    # Make all the cars drive
    for auto in car_list:
        auto.drive()
        if auto.xcor() < -int(SCREEN_SIZE * .55):
            auto.choose_lane()
        for car in car_list:
            # Make sure cars aren't occupying the same space
            while auto.distance(car.position()) != 0 and auto.distance(car.position()) < 50:
                if auto.xcor() > SCREEN_SIZE * .55:
                    auto.choose_lane()
                else:
                    auto.back(10)

    # Detect collision
    for car in car_list:
        if car.distance(tim.position()) < 30 and car.ycor() == tim.ycor():
            # Turn off listener
            screen.onkeypress(tim.do_nothing, "Up")

            # Squash turtle
            tim.shapetransform(-1, -1, 0, 1)

            # So that the "GAME OVER" will be on top
            screen.update()

            game_on = False
            end_game = GameOver()
            screen.update()
    if tim.has_crossed_finish():
        tim.to_start()
        level.level += 1
        level.update_level()
        for c in range(0, 3):
            car_list.append(Car())
        if sleep_time > .05:
            sleep_time -= .005
        else:
            for car in car_list:
                car.speed_up()


screen.exitonclick()
