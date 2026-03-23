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

# Derived class (IS-A relationship)
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print("Interest added:", interest)



sa = SavingsAccount("John", 1000)  # usage
sa.deposit(500)
sa.add_interest()
sa.display_balance()