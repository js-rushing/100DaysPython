import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "normal"))
# my_label.pack(side="bottom")
my_label.pack()

# Two different ways to change attributes
my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    # my_label["text"] = "Button clicked"
    my_label.config(text=text_input.get())


# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
text_input = tkinter.Entry(width=20)
text_input.insert(tkinter.END, string="Placeholder text.")
text_input.pack()

# Text
multi_line_text_input = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
multi_line_text_input.focus()
# Adds placeholder text
multi_line_text_input.insert(tkinter.END, "Placeholder text.")
# Gets current textbox value at line 1, character 0
print(multi_line_text_input.get("1.0", tkinter.END))
multi_line_text_input.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
