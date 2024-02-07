class MoneyMachine:
    Currency="$"
    COIN_Values={
        "quarters":0.25,
        "dimes":0.10,
        "ncikles":0.05,
        "pennies":0.01
    }


    def __init__(self):

        self.money_recived=0
        self.profit = 0

    # this method will show our profit
    def report(self):
        print(f"Money:{self.Currency}{self.profit}")

    # this method: it will allow you to enter money
    def process_coins(self):
        print("please insert Coin")
        for coin in self.COIN_Values:
            self.money_recived+=int(input(f"How Many {coin}>>"))*self.COIN_Values[coin]
        return self.money_recived

        # this method will check the payment and arrange our profit
    def make_payment(self,cost):
        self.process_coins()
        if self.money_recived>=cost:
            change=round(self.money_recived-cost,2)
            print(f"Here is {self.Currency}{change} in change")
            self.profit+=cost
            self.money_recived=0
            return True
        else:
            print("Sory Thats Not Enough Money. Money Refunded")
            self.money_recived=0
            return False
