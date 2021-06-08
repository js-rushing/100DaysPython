import requests
import json
from config import ENVIRONMENT, SHEETY_URL
from data_manager import DataManager
from flight_search import FlightSearch

# sheety = DataManager()
#
# sheety.fill_iata_column()


def get_user_info():
    email_match = False
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    while not email_match:
        email = input("What is your email?")
        email_confirm = input("Retype your email to confirm.")
        if email == email_confirm:
            print("You're in the club!")
            email_match = True
        else:
            print("Email did not match.  Try again.")
    info = {
        "user": {
            "firstName": f"{first_name}",
            "lastName": f"{last_name}",
            "email": f"{email}"
        }
    }
    return info


def post_user_info(info):
    if ENVIRONMENT == "Production":
        res = requests.post(url=f"{SHEETY_URL}/users", json=info)
        print(res.text)
    else:
        with open(file="user_data.json", mode="r") as file:
            user_data = json.loads(file.read())
            user_data['users'].append(info)
        with open(file="user_data.json", mode="w") as file:
            file.write(json.dumps(user_data, indent=4))


# Welcome
print("Welcome to Angela's Flight Club.")
print("We find the best flight deals and email you.")

user_info = get_user_info()
print(user_info)
print("\n")
post_user_info(user_info)

# for flight in sheety.data['flights']:
#     fs = FlightSearch(flight)
#     fs.search_flights()
