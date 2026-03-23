############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   26/02/2026
#   Last Modified   :   26/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use method overriding to implement different behaviors 
#           for the same method in derived classes.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""
Same method name.
Different behavior.
That is Method Overriding.
In the example below, we have a base class BankAccount with a method withdraw.
The SavingsAccount and CurrentAccount classes override the withdraw method to implement different withdrawal rules.

"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def account_type(self):
        print("This is a generic bank account")

class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        # Savings account has withdrawal limit rule
        if amount > 1000:
            print("Withdrawal limit exceeded for Savings Account")
        else:
            super().withdraw(amount)

    def account_type(self):
        print("This is a Savings Account")

class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        # Current account allows overdraft up to 500
        if amount <= self.balance + 500:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")

    def account_type(self):
        print("This is a Current Account")


# Create accounts  
savings = SavingsAccount("Alice", 5000)
current = CurrentAccount("Bob", 2000)

# Show account types
savings.account_type()
current.account_type()

# Test withdrawals
savings.withdraw(1500)  # Should show withdrawal limit exceeded
savings.withdraw(500)   # Should succeed