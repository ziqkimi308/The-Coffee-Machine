"""
********************************************************************************
* Project Name:  The Coffee Machine
* Description:   The Coffee Machine project is a simulation of a coffee vending machine that can serve multiple types of coffee
* Author:        ziqkimi308
* Created:       2024-12-03
* Updated:       2024-12-03
* Version:       1.0
********************************************************************************
"""

# Import
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Main Code
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_Off = False
while not turn_Off:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        turn_Off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
               coffee_maker.make_coffee(coffee)