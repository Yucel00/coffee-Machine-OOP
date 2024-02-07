class CofeeMaker:
    def __init__(self):
        self.resources={
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    # this method will show the remaining resources
    def report(self):
        for item in self.resources:
            print(f"{item}:{self.resources[item]}")


    # This Method the resources be enough to check it
    def is_resource_sufficient(self,drink):
        can_make=True
        for item in drink.ingredients:
            if drink.ingredients[item]>self.resources[item]:
                print(f"Sorry there is not enough {item}")
                can_make=False
        return can_make

    # this method will make the entered coffee
    def make_coffee(self,order):
        for item in order.ingredients:
            self.resources[item]-=order.ingredients[item]
        print(f"Here Is your {order.name}")
