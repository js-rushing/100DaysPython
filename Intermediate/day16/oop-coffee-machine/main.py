from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_on = True
drink_exists = False

while is_on:
    order = input(f"What would you like? ({menu.get_items()})")
    if order == "report":
        coffee_machine.report()
        money_machine.report()
    elif order == "off":
        print("Powering Off")
        is_on = False
    else:
        while not drink_exists:
            recipe = menu.find_drink(order)
            if recipe:
                drink_exists = True
            else:
                order = input("What would you like?")
        if coffee_machine.is_resource_sufficient(recipe) and money_machine.make_payment(recipe.cost):
            coffee_machine.make_coffee(recipe)
