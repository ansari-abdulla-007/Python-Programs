class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for", self.name)

    def show_balance(self):
        print("Current Balance:", self.balance)

# Creating object
acc1 = BankAccount("Ali", 5000)

# Calling method
acc1.show_balance()
