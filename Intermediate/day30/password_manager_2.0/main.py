import json
from tkinter import *
from tkinter import messagebox
from collections import Counter
import random
import os.path

SAVE_LOCATION = "pass_data.json"

password_dict = {}
common_email = ""


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
    global password_dict
    if os.path.isfile(SAVE_LOCATION):
        with open(SAVE_LOCATION) as file:
            password_dict = json.load(file)

        get_common_email()


def get_common_email():
    global common_email
    array = [password_dict[item]["email"] for item in password_dict]
    common_email = Counter(array).most_common(1)[0][0]


# def search_for_website():
#     if website_input.get():
#         site = website_input.get()
#         email = password_dict[site]["email"]
#         password = password_dict[site]["password"]
#         window.clipboard_clear()
#         window.clipboard_append(password)
#         messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")


def copy_email():
    if website_input.get():
        site = website_input.get()
        try:
            email = password_dict[site]["email"]
            window.clipboard_clear()
            window.clipboard_append(email)
            messagebox.showinfo(title="Email Copied", message=f"{email} copied to clipboard.")
        except KeyError:
            messagebox.showwarning(title="Record Not Found", message=f"No record for {site} yet created.")
        except FileNotFoundError:
            messagebox.showwarning(title="Record Not Found", message=f"No record for {site} yet created.")


def copy_password():
    if website_input.get():
        site = website_input.get()
        try:
            password = password_dict[site]["password"]
            window.clipboard_clear()
            window.clipboard_append(password)
            messagebox.showinfo(title="Password Copied", message="Password copied to clipboard.")
        except KeyError:
            messagebox.showwarning(title="Record Not Found", message=f"No record for {site} yet created.")
        except FileNotFoundError:
            messagebox.showwarning(title="Record Not Found", message=f"No record for {site} yet created.")


def save_password():
    if website_input.get() and email_input.get() and password_input.get():
        website = website_input.get()
        email = email_input.get()
        password = password_input.get()

        password_dict[website] = {
                "email": f"{email}",
                "password": f"{password}"
            }
        with open(SAVE_LOCATION, mode="w") as file:
            json.dump(password_dict, file, indent=4)

        website_input.delete(0, END)
        email_input.delete(0, END)
        email_input.insert(0, common_email)
        password_input.delete(0, END)

        messagebox.showinfo(title="Success", message="Password Added.")
    else:
        messagebox.showwarning(title="Data Missing", message="All fields required.")


# ---------------------------- UI SETUP ------------------------------- #
get_saved_passwords()

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
website_input.grid(column=1, row=1, sticky="EW")

# search_btn = Button(text="Search")
# search_btn.config(command=search_for_website)
# search_btn.grid(column=2, row=1, sticky="EW")

copy_email_btn = Button(text="Copy Email")
copy_email_btn.config(command=copy_email)
copy_email_btn.grid(column=2, row=1, sticky="EW")

copy_password_btn = Button(text="Copy Password")
copy_password_btn.config(command=copy_password)
copy_password_btn.grid(column=3, row=1, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry()
email_input.insert(0, common_email)
email_input.grid(column=1, row=2, columnspan=3, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

gen_pass_btn = Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(column=2, row=3, columnspan=2, sticky="EW")

add_btn = Button(text="Add", command=save_password, width=50)
add_btn.grid(column=1, row=4, columnspan=3, sticky="EW")


window.mainloop()
