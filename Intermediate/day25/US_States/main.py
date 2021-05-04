import turtle
import pandas
from label import Label

STATE_DATA = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.tracer(0)
screen.setup(width=900, height=1200)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.update()


# Prints the coordinates of any point you click on the screen element
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

state_list = STATE_DATA["state"].to_list()
label_list = []

for s in state_list:
    data_row = STATE_DATA[STATE_DATA.state == s]
    label_list.append(Label(s, int(data_row["x"]), int(data_row["y"])))

states_guessed = []
game_on = True
game_score_count = 0
while game_on:
    if game_score_count == 0:
        answer_state = screen.textinput(title="Guess A State",
                                        prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{game_score_count}/50 States Correct",
                                        prompt="What's another state's name?").title()
    if answer_state == "Exit":
        game_on = False
    else:
        if answer_state in state_list and answer_state not in states_guessed:
            states_guessed.append(answer_state)
            label_list[state_list.index(answer_state)].write_state_name(alignment="left", font_size=10)
            game_score_count += 1
        if game_score_count == 50:
            game_on = False

if game_score_count == 50:
    winner = Label("You Did It!", 0, -350)
    winner.color("green")
    winner.write_state_name(alignment="center", font_size=20)
else:
    states_not_guessed = []
    for state in state_list:
        if state not in states_guessed:
            states_not_guessed.append(state)
    states_to_learn = {
        "State": states_not_guessed
    }
    states_to_learn_data_frame = pandas.DataFrame(states_to_learn)
    states_to_learn_data_frame.to_csv("states_to_learn.csv")

screen.exitonclick()
