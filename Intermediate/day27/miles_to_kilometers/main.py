from tkinter import *


def calculate():
    miles = miles_input.get()
    if miles != "":
        miles = float(miles)
        kilometers = miles * 1.609
        kilometers_lbl.config(text=f"{kilometers}")


window = Tk()
window.minsize(width=300, height=200)
window.title("Miles to Km Converter")
window.config(padx=70, pady=50)

miles_input = Entry()
miles_input.config(width=15)
miles_input.grid(column=0, row=0)

miles_lbl = Label(text="Miles")
miles_lbl.grid(column=1, row=0)

equal_to_lbl = Label(text="is equal to")
equal_to_lbl.config(pady=10)
equal_to_lbl.grid(column=0, row=1)

kilometers_lbl = Label(text="0")
kilometers_lbl.grid(column=0, row=2)

km_lbl = Label(text="Km")
km_lbl.grid(column=1, row=2)

calc_btn = Button(text="Calculate", command=calculate)
calc_btn.place(x=25, y=110)


window.mainloop()
