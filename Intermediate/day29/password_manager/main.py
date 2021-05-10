from tkinter import *
from tkinter import messagebox
import random
import os.path

SAVE_LOCATION = "pass_data.txt"
COMMON_EMAIL = "angela@email.com"

password_dict = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # VARIABLES
    letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbol_list = ['!', '@', '#', '$', '%', '^',
                   '&', '*', '(', ')', '~', '?', '<', '>']
    pass_arr = []
    password = ""

    num_letters = random.randint(6, 10)
    num_numbers = random.randint(6, 10)
    num_symbols = random.randint(6, 10)

    # Populate numbers array
    for n in range(0, num_numbers):
        rand_num = random.randint(0, 9)
        pass_arr.append(str(rand_num))

    # Populate letters array
    for n in range(0, num_letters):
        rand_let = random.choice(letter_list)
        lower_or_not = random.randint(0, 1)
        if lower_or_not == 0:
            pass_arr.append(rand_let)
        else:
            pass_arr.append(rand_let.lower())

    # Populate symbols array
    for n in range(0, num_symbols):
        pass_arr.append(random.choice(symbol_list))

    # Generate password
    while len(pass_arr) > 0:
        rand_num = random.randint(0, len(pass_arr) - 1)
        password += pass_arr[rand_num]
        pass_arr.pop(rand_num)

    password_input.delete(0, END)
    password_input.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_saved_passwords():
    if os.path.isfile(SAVE_LOCATION):
        stripped_arr = []
        with open(SAVE_LOCATION) as file:
            saved_passwords = file.readlines()
            for line in saved_passwords:
                stripped_arr.append(line.rstrip())
            for datum in stripped_arr:
                items = datum.split(" | ")
                # print(items)
                item_dict = {
                    "website": f"{items[0]}",
                    "email": f"{items[1]}",
                    "password": f"{items[2]}"
                }
                password_dict.append(item_dict)


def save_password(*args):
    if website_input.get() and email_input.get() and password_input.get():
        website = website_input.get()
        email = email_input.get()
        password = password_input.get()

        password_obj = {
            "website": f"{website}",
            "email": f"{email}",
            "password": f"{password}"
        }

        password_dict.append(password_obj)

        with open(SAVE_LOCATION, mode="w") as file:
            for item in password_dict:
                info_string = f"{item['website']} | {item['email']} | {item['password']}\n"
                file.writelines(info_string)

        website_input.delete(0, END)
        email_input.delete(0, END)
        email_input.insert(0 ,COMMON_EMAIL)
        password_input.delete(0, END)

        messagebox.showinfo(title="Success", message="Password Added.")
    else:
        messagebox.showwarning(title="Data Missing", message="All fields required.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_image)
logo.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry()
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry()
email_input.insert(0, COMMON_EMAIL)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

gen_pass_btn = Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", command=save_password, width=50)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

get_saved_passwords()


window.mainloop()
