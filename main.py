from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
is_on = True

while is_on:
    options = menu.get_items()
    user_choice = input(f"Enter your choice ({options}) : ")
    if user_choice == "off":
        is_on = False
        print("Turning off...\nTurned off!")
    elif user_choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)