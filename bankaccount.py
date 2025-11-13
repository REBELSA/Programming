class bankaccount:
    def __init__(self, balance):
        self.balance  = balance
    def deposit(self, amount):
        self.balance += amount
        print("New balance: ",self.balance)

acc = bankaccount(25000)
acc.deposit(15000)