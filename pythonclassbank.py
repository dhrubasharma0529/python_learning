class BankDetails():
    def __init__(self,account,amount):
        self.account = account
        self.amount = amount
    def deposit(self,balance):
        self.amount +=balance
        return self.amount
    def withdraw (self,balance):
        if self.amount > 0 and balance<= self.amount:
            self.amount -=balance
        return self.amount
    def get_balance(self):
        return f"the balance in your account is {self.amount}"
obj1 = BankDetails("ram",0)
obj1.deposit(500)
print(obj1.get_balance())
obj1.withdraw(250)
print(obj1.get_balance())
