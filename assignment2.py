# Create a base class Account with account_number and balance.
# Create a derived class SavingsAccount that has an interest rate.
# Add a method to calculate the interest earned.
class Account():
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self,account,balance,rate):
        self.rate  = rate
        super().__init__(account,balance)
    def interestrate(self):
        interest = self.balance * self.rate
        return interest
acc = SavingsAccount("5000",10000,0.05)
print(acc.interestrate())
