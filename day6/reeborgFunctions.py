def turn_right():
    turn_left()
    turn_left()
    turn_left()


def face_north():
    while not is_facing_north():
        turn_left()


def advance():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        if front_is_clear():
            move()


face_north()
if not right_is_clear and not front_is_clear:
    turn_left()
    turn_left()
while not at_goal():
    advance()
