import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

OPTIONS = ["refill", "off", "report", "1", "2", "3"]

out_of_service = False

off = False

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0


def clear_console():
    os.system('clear')


def print_report():
    global money
    money_string = "${:.2f}".format(money)
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {money_string}")


def prompt_user():
    request = input("\nWhat would you like?\n"
                    "Press:"
                    "\t1 for Espresso\n"
                    "\t2 for Latte\n"
                    "\t3 for Cappuccino\n")
    while request not in OPTIONS:
        print("Invalid option entered.")
        request = input("What would you like?\n"
                        "Press:"
                        "\t1 for Espresso\n"
                        "\t2 for Latte\n"
                        "\t3 for Cappuccino\n")
    if request == "1":
        request = "espresso"
    elif request == "2":
        request = "latte"
    elif request == "3":
        request = "cappuccino"

    return request


def check_resources(drink):
    if drink == "espresso":
        if resources['water'] < MENU[drink]['ingredients']['water'] \
                or \
                resources['coffee'] < MENU[drink]['ingredients']['coffee']:
            return False
        else:
            return True
    else:
        if resources['water'] < MENU[drink]['ingredients']['water'] \
                or \
                resources['coffee'] < MENU[drink]['ingredients']['coffee'] \
                or \
                resources['milk'] < MENU[drink]['ingredients']['milk']:
            return False
        else:
            return True


def get_money(beverage):
    cost = MENU[beverage]['cost']
    cost_string = "${:.2f}".format(cost)
    payment = 0.00
    coin_list = ['q', 'd', 'n', 'p', 'c']
    cancelled = False
    coin = ""
    while payment < cost and not cancelled:
        clear_console()
        payment_string = "${:.2f}".format(payment)
        if beverage == "espresso":
            print(f"An {beverage} costs {cost_string}.")
        else:
            print(f"A {beverage} costs {cost_string}.")
        print(f"You have paid {payment_string} so far.")
        coin = input("Please insert coins.\n"
                     "'q' for quarter\n"
                     "'d' for dime\n"
                     "'n' for nickel\n"
                     "'p' for penny\n"
                     "'c' to cancel sale\n").lower()
        while coin not in coin_list:
            print("Coin Rejected")
            coin = input("Please insert coins.\n"
                         "'q' for quarter\n"
                         "'d' for dime\n"
                         "'n' for nickel\n"
                         "'p' for penny\n"
                         "'c' to cancel sale\n").lower()
        if coin == 'q':
            payment += .25
        elif coin == 'd':
            payment += .10
        elif coin == 'n':
            payment += .05
        elif coin == 'p':
            payment += .01
        else:
            cancelled = True
            payment -= payment*2
    return payment


def make_change(beverage, payment):
    cost = MENU[beverage]['cost']
    remainder = payment - cost
    return remainder


def update_resources(beverage, payment):
    global money
    resources['water'] -= MENU[beverage]['ingredients']['water']
    resources['coffee'] -= MENU[beverage]['ingredients']['coffee']
    if beverage != "espresso":
        resources['milk'] -= MENU[beverage]['ingredients']['milk']
    money += payment


def take_order():
    global off
    global resources
    choice = prompt_user()
    if choice == "report":
        print_report()
    elif choice == "refill":
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    elif choice == "off":
        print("Powering Off")
        off = True
    else:
        if check_resources(choice):
            clear_console()
            customer_payment = get_money(choice)
            if customer_payment < 0:
                clear_console()
                change = 0 - customer_payment
                change_string = "${:.2f}".format(change)
                print("Sale cancelled.")
                print(f"Here is your {change_string} back")
            else:
                clear_console()
                update_resources(choice, customer_payment)
                change = make_change(choice, customer_payment)
                change_string = "${:.2f}".format(change)
                if change > 0:
                    print(f"Here is your change: {change_string}")
                    print(f"And here is your {choice}!")
                else:
                    print(f"Here is your {choice}!\n")
        else:
            print("Insufficient Resources")


def check_service():
    global out_of_service
    if not check_resources("espresso") \
            and not check_resources("latte") \
            and not check_resources("cappuccino"):
        print("\nMachine Out of Service\nPlease notify employee\n")
        print_report()
        out_of_service = True


def operate_machine():
    take_order()
    if not off:
        check_service()


while not off:
    operate_machine()
