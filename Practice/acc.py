class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Current balance: {self.balance}")

account = Bank("John Doe", 1000)
account.display_balance()
account.credit(500)
account.debit(200)  