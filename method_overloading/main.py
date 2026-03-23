############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   26/02/2026
#   Last Modified   :   26/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#     This module shows how we can use method overriding to implement different behaviors
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""

Python does NOT support traditional method overloading like Java/C++.
But we can simulate it using:
    Default arguments
    *args

Same method name.
Different parameters.
That is Method Overloading.
In the example below, we have a class Calculator with an add method that can handle different numbers of arguments.
This is Overloading in derived class (Python style)

"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. Balance: {self.balance}")


class SavingsAccount(BankAccount):

    # Overloaded version (Python style)
    def deposit(self, amount, bonus=0):
        total = amount + bonus
        self.balance += total
        print(f"{self.owner} deposited {total} (including bonus). Balance: {self.balance}")

    def account_type(self):
        print("This is a Savings Account")

class CurrentAccount(BankAccount):

    ## Overloaded version (Python style) with *args to accept variable number of arguments
    def deposit(self, *amounts):
        total = sum(amounts)
        self.balance += total
        print(f"{self.owner} deposited {total}. Balance: {self.balance}")

    def account_type(self):
        print("This is a Current Account")


# Create account  
acc2 = CurrentAccount("Bob", 2000)

# Test deposits with different parameters

acc2.deposit(500)   ### This will call the deposit method with one argument (500)

### This will call the deposit method with two arguments (200 and 300) and sum them up to 500 before adding to balance
acc2.deposit(200, 300) 

# This will call the deposit method with three arguments (100, 200, and 300) and sum them up to 600 before adding to balance
acc2.deposit(100, 200, 300)