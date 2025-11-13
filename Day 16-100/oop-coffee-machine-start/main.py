from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

angela_coffee_menu = Menu()
angela_coffee_maker = CoffeeMaker()
angela_money_machine = MoneyMachine()



coffee_machine_is_on = True
while coffee_machine_is_on:

    #TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino/):
    order_name = input(f"What would you like?{angela_coffee_menu.get_items()}:").lower()

    #TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if order_name == "off":
        coffee_machine_is_on = False
    #TODO: 3. Print report.
    elif order_name == "report":
        angela_coffee_maker.report()
        angela_money_machine.report()
    else:
        drink = angela_coffee_menu.find_drink(order_name)
        '''' in Python if the value of the variable contain something 
                     then it's considered as True'''
        if drink:
            print(f"drink: {drink}")
            #TODO: 4. Check resources sufficient?
            if angela_coffee_maker.is_resource_sufficient(drink):
            #TODO: 5. Process coins. and Check transaction successful?
                if angela_money_machine.make_payment(drink.cost):
            #TODO 6.  Make Coffee.
                    angela_coffee_maker.make_coffee(drink)
