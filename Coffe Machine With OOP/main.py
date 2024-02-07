from coffee_maker import CofeeMaker
from menu import MenuItem,Menu
from money_machine import MoneyMachine

money_machine=MoneyMachine()
menu=Menu()

coffe_maker=CofeeMaker()
is_on=True

while is_on:
    options=menu.get_items()
    try:
        choice=input(f"What would you like?{options}(report/off)>>")
        if choice == "off":
            is_on = False
        elif choice == "report":
            money_machine.report()
            coffe_maker.report()
        else:
            drink = menu.find_drink(choice)
            if coffe_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffe_maker.make_coffee(drink)
    except:
        print("Wrong Choice")
