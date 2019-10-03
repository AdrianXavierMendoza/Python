class User:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.accounts = {}
    
    def make_withdraw(self, amount, acct):
        self.accounts[acct].balance -= amount
        return self

    def make_deposit(self, amount, acct):
        self.accounts[acct].balance += amount
        return self

    def display_user_balance(self, acct):
        print(f"User:{self.name} Acct Name:{acct.upper()} Balance:{self.accounts[acct].balance}")
        return self

    def transfer_money(self, other_user, amount, acct):
        self.accounts[acct].balance -= amount
        other_user.account.balance += amount
        return self

    def add_acct(self, name, balance, int_rate):
        self.accounts[name] = BankAccount(int_rate, balance)
        return self

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
        if self.balance>0:
            self.balance += (self.balance * self.int_rate)
        else:
            print('insufficient funds')
        return self

guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
adrian = User('Adrian Xavier Mendoza','amen02me@sbcglobal.net')

monty.add_acct('checking', 1000, 0.01).display_user_balance('checking').make_deposit(100,"checking").display_user_balance('checking')