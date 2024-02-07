class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=200, milk=0, coffee=24, cost=2.5),
            MenuItem(name="cappuchino", water=200, milk=150, coffee=24, cost=2.5)
        ]

   # this method return content of the menu
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    # if this method finds the entered drink in our menu, we will return the ingredients of that drink
    def find_drink(self,order_name):
        for item in self.menu:
            if item.name==order_name:
                return item
