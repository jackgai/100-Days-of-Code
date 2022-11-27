import sys

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_Maker = CoffeeMaker()
money_Machine = MoneyMachine()
while True:
    choice = input(f"What would you like? ({menu.get_items()})")
    if choice == "off":
        sys.exit()
    if choice == "report":
        coffee_Maker.report()
        money_Machine.report()
        continue

    # check resources sufficient
    menuItem: MenuItem = menu.find_drink(choice)
    if menuItem is None:
        continue
    if not coffee_Maker.is_resource_sufficient(menuItem):
        continue
    # process coins and check transaction successful
    if not money_Machine.make_payment(menuItem.cost):
        continue
    # make coffee
    coffee_Maker.make_coffee(menuItem)

