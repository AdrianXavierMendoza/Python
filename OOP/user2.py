class User:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.balance = 0
    
    def make_withdraw(self, amount):
        self.balance -= amount
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self

    #Break

guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
adrian = User('Adrian Xavier Mendoza','amen02me@sbcglobal.net')

guido.make_deposit(30).make_deposit(30).make_deposit(30).make_withdraw(10).display_user_balance()

monty.make_deposit(30).make_deposit(30).make_withdraw(10).make_withdraw(10).display_user_balance()

adrian.make_deposit(30).make_withdraw(10).make_withdraw(10).make_withdraw(10).display_user_balance()

guido.transfer_money(adrian,80).display_user_balance()
adrian.display_user_balance()