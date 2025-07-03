# Create a class BankAccount with:
# A private attribute __balance

# A method deposit(amount) to increase balance

# A method __deduct_fee() that subtracts 10 from balance (to be called inside deposit)

# Try accessing __balance and __deduct_fee() from outside the class
class BAnkAccount():
    def __init__(self,balance,amount):
        self.__balance = balance
        self.amount = amount 
    def depositamount(self):
        self.__deduct_fee()
        self.__balance+=self.amount
        return self.amount
    def __deduct_fee(self):
        deduction_fee = 10
        self.amount-= deduction_fee
    def display(self):
        return self.__balance
obj1 = BAnkAccount(500,50)
print(f"the amount to be deposited is {obj1.depositamount()}")
print(f"The total balance in your bank account is {obj1.display()}")