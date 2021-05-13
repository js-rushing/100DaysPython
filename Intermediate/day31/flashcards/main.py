from tkinter import *
from random import choice
import pandas

word_obj = {}

# Read CSV File and format as dictionary
try:
    to_learn_list = pandas.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    to_learn_list = pandas.read_csv("./data/german_english.csv").to_dict(orient="records")


def new_card():
    global word_obj, flip_timer
    window.after_cancel(flip_timer)
    word_obj = choice(to_learn_list)
    card.itemconfig(card_title, text="German")
    card.itemconfig(card_word, text=word_obj["German"])
    card.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card.itemconfig(card_title, text="English")
    card.itemconfig(card_word, text=word_obj["English"])
    card.itemconfig(card_image, image=card_back_img)


def known_word():
    update_to_learn()
    new_card()


def update_to_learn():
    to_learn_list.remove(word_obj)
    to_learn_data_frame = pandas.DataFrame(to_learn_list)
    to_learn_data_frame.to_csv("./data/words_to_learn.csv", index=False)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Karteikarten")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_image = card.create_image(400, 263, image=card_front_img)
card_title = card.create_text(400, 150, text="Language", font=("Arial", 24, "normal"))
card_word = card.create_text(400, 250, text="Word", font=("Arial", 32, "bold"))
card.grid(column=0, row=0, columnspan=2)

wrong_btn = Button()
red_x = PhotoImage(file="./images/wrong.png")
wrong_btn.config(image=red_x, highlightthickness=0, command=new_card)
wrong_btn.grid(column=0, row=1)

right_btn = Button()
green_check = PhotoImage(file="./images/right.png")
right_btn.config(image=green_check, highlightthickness=0, command=known_word)
right_btn.grid(column=1, row=1)

new_card()

window.mainloop()
