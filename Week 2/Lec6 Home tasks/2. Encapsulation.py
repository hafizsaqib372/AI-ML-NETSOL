class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.__balance -= amount
        print("Withdrawn:", amount)

    def get_balance(self):
        return self.__balance


acc = BankAccount("Hamza", 5000)
acc.deposit(2000)
acc.withdraw(1500)
print("Balance:", acc.get_balance())
