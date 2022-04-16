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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def ingredients_enough():
    global work
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        work = False
        print("Sorry there is not enough water.")
        if MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
            work = False
            print("Sorry there is not enough coffee.")
            if choice == "latte" or choice == "cappuccino":
                if MENU[choice]["ingredients"]["milk"] > resources["milk"]:
                    work = False
                    print("Sorry there is not enough coffee.")
    return work


def money():
    global profit
    print("Please, insert coins")
    inserted_quarters = int(input("Quarters: ")) * 0.25
    inserted_dimes = int(input("Dimes: ")) * 0.10
    inserted_nickles = int(input("Nickles: ")) * 0.05
    inserted_pennies = int(input("Pennies: ")) * 0.01
    inserted_money = inserted_quarters + inserted_dimes + inserted_nickles + inserted_pennies
    if inserted_money < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif inserted_money == MENU[choice]["cost"]:
        profit += inserted_money
        print("Here is your latte. Enjoy!")
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        if choice == "latte" or choice == "cappuccino":
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    elif inserted_money > MENU[choice]["cost"]:
        change = inserted_money - MENU[choice]["cost"]
        profit += MENU[choice]["cost"]
        print(f"Your change is {round(change, 2)}")


def report():
    print(f"Report: \nWater = {resources['water']} ml \nCoffee = {resources['coffee']} ml "
          f"\nMilk = {resources['milk']} ml "
          f"\nMoney = ${profit}")


def rate_ingredients():
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    if choice == "latte" or choice == "cappuccino":
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]


work = True

while work:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        work = False
    if choice == "report":
        report()
        continue
    if choice == "espresso" or choice == "cappuccino" or choice == "latte":
        ingredients_enough()
        if not work:
            continue
        rate_ingredients()
        money()

