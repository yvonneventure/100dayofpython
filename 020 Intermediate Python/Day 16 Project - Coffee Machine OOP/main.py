from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make = CoffeeMaker()
coin = MoneyMachine()

game = True
while game:
    prompt = input(f"What would you like? ({menu.get_items()}):")
    if prompt == "off":
        game = False
    elif prompt == "report":
        make.report()
        coin.report()
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        drink = menu.find_drink(prompt)

        if make.is_resource_sufficient(drink):


            if coin.make_payment(drink.cost):
                make.make_coffee(drink)
                # make.report()
                # coin.report()
            else:
                game = False
        else:
            game = False








