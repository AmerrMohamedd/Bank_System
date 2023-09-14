# task 1.1 Make Class(User) with attributes:
# name
# age
# gender
# balance
# task 1.2 Make method to show previous data
# Task 2 :
# Make Child Class(Bank) which inheritance from Class(user) with Methods:
# task 2.1 deposit : which take parameter(amount) and add it to balance and print new balance.
# task 2.2 withdraw : which take parameter(amount) and check if user have enough money.
# task 2.3 view balance : to show current balance.
# Task 3 :
# task 3.1 Make Child Class(CIB) which inheritance from Class(Bank) with Methods:
# Loan application: which take parameter(amount) and (Duration) >> max loan is one million
# task 3.2 Make Child Class(QNB) which inheritance from Class(Bank) with Methods:
# Loan application: which take parameter(amount) and (Duration) >> max loan is one 2 million

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
