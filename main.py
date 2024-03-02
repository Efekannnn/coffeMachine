MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO a. Check the user’s input to decide what to do next.
user_choice = input("Which coffe do you want.\n"
                    "options are \"espresso, latte and cappuccino\": ")


def resources_calculator():
    resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
    print(resources)
    return resources


resources_calculator()