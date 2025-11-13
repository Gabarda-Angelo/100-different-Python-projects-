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
    "money":0,
}

def inventory_report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${resources['money']:.2f}")

    return 0

def resources_sufficient(resources_information, customer_order):

    if resources_information["water"] < MENU[customer_order]["ingredients"].get("water",0):
        print("Not enough water")
        return False
    elif resources_information["milk"] < MENU[customer_order]["ingredients"].get("milk",0):
        print("Not enough milk")
        return False
    elif resources_information["coffee"] < MENU[customer_order]["ingredients"].get("coffee",0):
        print("Not enough coffee")
        return False

    return True

def inserted_coins():
    try:
        print("Please insert coins.")
        quarters = input("Insert quarters: ")
        dimes = input("Insert dimes:")
        nickles = input("Insert nickles:")
        pennies = input("Insert pennies:")

        total = (float(quarters) * 0.25)+ (float(dimes) * 0.10) + (float(nickles) * 0.05)+ (float(pennies) * 0.01)

        return total
    except ValueError:
        print("Please insert coins.")
        return 0

def transaction_successful(total_money, order):
    change = total_money - MENU[order]["cost"]
    if total_money < MENU[order]["cost"]:
        print("sorry your money is not enough! Money refunded")
        return False
    elif total_money == MENU[order]["cost"]:
        print(f"Thanks I receive ${total_money}")
        return True
    elif total_money > MENU[order]["cost"]:
        print(f"Thanks I receive ${total_money:.2f}, here is your change ${change:.2f}")
        return True

    return 0

def make_coffee(customer_order):
    resources["water"] -= MENU[customer_order]["ingredients"].get("water",0)
    resources["milk"]  -= MENU[customer_order]["ingredients"].get("milk",0)
    resources["coffee"] -= MENU[customer_order]["ingredients"].get("coffee",0)

    resources["money"] += MENU[customer_order]["cost"]

    print(f"Here is your {customer_order} enjoy!")


def coffee_machine():

    machine_is_on = True

    while machine_is_on:
        #TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):
        print("MENU: Espresso: $1.5 | Latte: $2.5 | Cappuccino: $3.00")
        user_command = input("What would you like? (espresso/latte/cappuccino):").lower()

        #TODO: 2.Turn off the Coffee Machine by entering “off” to the prompt.
        if user_command == "off":
            return
        #TODO: 3.Print report.
        elif user_command == "report":
            inventory_report()
        elif user_command in MENU:

            #TODO: 4.Check resources sufficient?
            if resources_sufficient(resources, user_command):

                # TODO: 5.Process coins
                total_coins = inserted_coins()

                #TODO: 6.Check transaction successful?
                if transaction_successful(total_coins, user_command):
                    #TODO: 7.Make Coffee.
                        make_coffee(user_command)
        else:
            print("Invalid input. Please choose espresso, latte, or cappuccino.")



coffee_machine()