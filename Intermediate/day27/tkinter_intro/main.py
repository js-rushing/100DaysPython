from tkinter import *


def button_clicked():
    my_label.config(text=text_input.get())


window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "normal"))
my_label.config(text="New Text", padx=5, pady=5)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
text_input = Entry(width=10)
text_input.grid(column=3, row=2)


window.mainloop()
