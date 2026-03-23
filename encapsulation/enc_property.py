############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com,ajith.de-silva@epita.fr)
#   Created         :   23/02/2026
#   Last Modified   :   23/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows usage of encapsulation with prpoperty decorators and 
#          how it provides control over data access and modification.
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""
Encapsulation with @property:
    **** We use @property to create getter and setter methods in a more Pythonic way.
    **** This allows us to control how attributes are accessed and modified while still using simple attribute syntax.
    **** We can add validation logic in the setter to prevent invalid data from being set.
    **** This is a common practice in Python to maintain data integrity and encapsulation. 

"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   ### Private variable

    @property    ### Getter using @property
    def balance(self):
        return self.__balance

    @balance.setter ### Setter using @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative!")

    ### Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    ### Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or invalid amount.")


#### usage
account1 = BankAccount("Ajith", 1000)   ### Create account

print(account1.balance) ### Accessing balance like a variable (but it's controlled!)

account1.balance = 2000 #### Setting balance using property
print(account1.balance) #### Accessing balance again and display it

# Trying to set negative balance
account1.balance = -500   # ❌ Not allowed

# Using methods
account1.deposit(500)
account1.withdraw(300)

print("Final Balance:", account1.balance)