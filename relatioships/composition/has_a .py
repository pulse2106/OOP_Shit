############################################################################################
#   File            :   is_a.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   01/03/2026
#   Last Modified   :   01/03/2026
#   Version         :   1.0.0
############################################################################################
#   Description:
#       In this example, SavingsAccount inherits from BankAccount, 
#       which means it has access to the deposit and display_balance methods defined in BankAccount. 
#       Additionally, SavingsAccount can have its own unique behavior, such as the add_interest method, 
#       while still maintaining the properties of a BankAccount. 
# 
# This illustrates the IS-A relationship in object-oriented programming.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""
WITH Inheritance.....

SavingsAccount IS-A BankAccount

    - It gets deposit()
    - It gets display_balance()
    - It adds new behavior (add_interest)

"""

from bank_account import BankAccount

# HAS-A relationship
class Customer:
    def __init__(self, name, initial_balance):
        self.name = name
        self.account = BankAccount(name, initial_balance)   # Customer HAS-A BankAccount

    def deposit_money(self, amount):
        self.account.deposit(amount)

    def show_balance(self):
        print(self.name, "Balance:", self.account.balance)


# Using the classes
c1 = Customer("Ajith",1000)
c1.deposit_money(1000)
c1.show_balance()