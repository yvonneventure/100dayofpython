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
MENU["espresso"]["ingredients"]["milk"] = 0
# print(MENU["espresso"]["ingredients"]["milk"])
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    for key in resources:
        print(f"{key.title()}: {resources[key]}")
def sufficient(coffee):
    if resources["water"] >= MENU[coffee]["ingredients"]["water"]:
        if resources["coffee"] >=  MENU[coffee]["ingredients"]["coffee"]:
            if resources["milk"] >= MENU[coffee]["ingredients"]["milk"]:
                print("please insert coins.")
                return True
            else:
                print("There's not enough milk")
                return False
        else:
            print("There's not enough coffee.")
            return False
    else:
        print("There's not enough water.")
        return False
def coin(coffee):
    # quarters= $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickles? "))
    p = int(input("How many pennies? "))
    pay = round(q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01, 2)
    print(f"pay is {pay}")
    if pay >= MENU[coffee]["cost"]:
        change = 0
        if pay > MENU[coffee]["cost"]:
            change = pay - MENU[coffee]["cost"]
            print(f"Here is ${change} in change.")
        return True, pay-change  # make coffee
    elif pay < MENU[coffee]["cost"]:
        print("Not enough money, money refunded.")
        return False, 0
def update(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]


#TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

game = True
money = 0
while game:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    # #TODO 2:check whether user want "report", "coffee", or "off"
    if prompt == "off":
        game = False
    elif prompt == "report":
        resources["money"] = money
        report()
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        sufficient = sufficient(prompt)
        if sufficient:
            go, income = coin(prompt)
            #print(f"{go} {income}")
            if go:
                money += income
                resources["money"] = money
                update(prompt)
                report()
                print(f"Here's your {prompt} ☕️ Enjoy!")
            else:
                game = False
        else:
            game = False







