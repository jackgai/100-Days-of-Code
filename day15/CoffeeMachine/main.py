import sys

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


# TODO: 1. prompt user by asking "What would you like? (espresso/latte/cappuccino):"


def getuserinput() -> str:
    """return the user input"""
    ans: str = input("What would you like? (espresso/latte/cappuccino):")
    return ans


# TODO: 2. turn off the coffee machine by entering "off" to the prompt


def turnoff():
    """exit program"""
    sys.exit()


# TODO: 3. print report
def print_report(resource, money):
    """print the report"""
    print(f'Water: {resource["water"]}')
    print(f'Milk: {resource["milk"]}')
    print(f'Coffee: {resource["coffee"]}')
    print(f'Money: {money}')


# TODO: 4. check resource sufficient
def check_resources(coffee_type, resource):
    """return true if resources is enough, false if not"""
    ingredients = coffee_type["ingredients"]
    for ingredient, value in ingredients.items():
        if resource[ingredient] < value:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


# TODO: 5. process coins
def coin_process():
    """return the total value of coin insertion"""
    quarters = int(input("Please insert quarter coins: "))
    dimes = int(input("Please insert dime coins: "))
    nickles = int(input("Please insert nickle coins: "))
    pennies = int(input("Please insert penny coins: "))
    payment = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return payment


# TODO: 6. check transaction successful
def check_transaction(coffee_type, payment):
    """return the money for making one coffee, return -1 is inserting coins is not enough"""
    coffee_cost = coffee_type["cost"]
    if payment < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return -1
    if payment > coffee_cost:
        print("Here is ${:0.2f} dollars in charge.".format(payment - coffee_cost))
    return coffee_cost


# TODO: 7: make coffee
def make_coffee(coffee_type, resource):
    """make coffee and reduce the resources"""
    ingredients = coffee_type["ingredients"]
    for ingredient, value in ingredients.items():
        resource[ingredient] -= value


def main():
    # we can also use "global money" inside a function to see the global money
    money = 0.0
    while True:
        user_input = getuserinput()
        if user_input == "off":
            turnoff()

        if user_input == "report":
            print_report(resources, money)
            continue

        if user_input not in MENU:
            continue

        if not check_resources(MENU[user_input], resources):
            continue

        payment = coin_process()
        earn = check_transaction(MENU[user_input], payment)
        if earn < 0:
            continue
        money += earn
        make_coffee(MENU[user_input], resources)
        print(f"Here is your {user_input} ☕️. Enjoy!")


if __name__ == '__main__':
    main()
