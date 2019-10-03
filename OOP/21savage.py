class BankAccount:

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Interest Rate:{self.int_rate}, Balance:{self.balance}")
	
    def yield_interest(self):
        if(self.balance>0):
            self.balance += (self.balance * self.int_rate)
        else:
            print('insufficient funds')
        return self

checkings = BankAccount(0.5,1000)
savings = BankAccount(0.2,-1000)

checkings.deposit(30).deposit(30).deposit(30).withdrawal(10).yield_interest().display_account_info()

savings.deposit(30).deposit(30).withdrawal(10).withdrawal(10).withdrawal(10).withdrawal(10).yield_interest().display_account_info()