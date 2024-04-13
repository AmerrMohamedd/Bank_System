class User:
    def __init__(self, name, age, gender, balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance

    def show_data(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Balance: ", self.balance)


class Bank(User):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ", amount)
        print("New Balance: ", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn: ", amount)
            print("New Balance: ", self.balance)
        else:
            print("Insufficient balance.")

    def view_balance(self):
        print("Current Balance: ", self.balance)


class CIB(Bank):
    def loan_application(self, amount, duration):
        if amount <= 1000000:
            print("Loan application for amount: ", amount, "and duration", duration, "months is accepted.")
        else:
            print("Maximum loan amount is 1 million")


class QNB(Bank):
    def loan_application(self, amount, duration):
        if amount <= 1000000:
            print("Loan application for amount: ", amount, "and duration", duration, "months is accepted.")
        else:
            print("Maximum loan amount is 2 million")
