from tkinter import *
import os
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BREAK_SOUND = "/home/boss/web/python/Intermediate/day28/break_sound.ogg"
reps = 0
checks_list = []
timer_running = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, checks_list
    reps = 0
    checks_list = []
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title_label.config(text="Timer", fg=GREEN)
    checks_label.config(text="")
    start_btn.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    start_btn.config(state="disabled")
    global reps
    # PRODUCTION VARS
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # DEVELOPMENT VARS
    # work_seconds = 4
    # short_break_seconds = 2
    # long_break_seconds = 3

    reps += 1
    if reps % 2 != 0:
        count_down(work_seconds)
        title_label.config(text="Work", fg=GREEN)
        if reps > 1:
            add_check()
    elif reps % 8 == 0:
        os.system("ogg123 " + BREAK_SOUND)
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    else:
        os.system("ogg123 " + BREAK_SOUND)
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)


def add_check():
    global checks_list
    checks_list.append(CHECKMARK)
    check_string = ""
    for check in checks_list:
        check_string += check
    checks_label.config(text=check_string)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds >= 10:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    else:
        canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN)
title_label.config(font=(FONT_NAME, 28, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Center of canvas is width/2, height/2
tomato_img = PhotoImage(
    file="/home/boss/web/python/Intermediate/day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130,
                                text="25:00",
                                fill="white",
                                font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start")
start_btn.config(font=(FONT_NAME, 14, "normal"),
                 bg=YELLOW,
                 fg="black",
                 highlightthickness=0,
                 command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset")
reset_btn.config(font=(FONT_NAME, 14, "normal"),
                 bg=YELLOW,
                 fg="black",
                 highlightthickness=0,
                 command=reset_timer)
reset_btn.grid(column=2, row=2)

checks_label = Label()
checks_label.config(fg=GREEN, bg=YELLOW, highlightthickness=0,
                    font=(FONT_NAME, 20, "normal"))
checks_label.grid(column=1, row=3)


window.mainloop()
