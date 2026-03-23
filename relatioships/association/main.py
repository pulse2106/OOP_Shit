
############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   01/03/2026
#   Last Modified   :   01/03/2026
#   Version         :   1.0.0
############################################################################################
#   Description:
#        
#     This example shows a BankEmployee class that uses a BankAccount class.
#       BankEmployee does not own BankAccount, but it can interact with it to perform operations like processing deposits.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""
Association means one class uses another class.

    No strong ownership
    Objects can exist independently
    Just interaction

    *** This is called Association (Uses-A relationship)
    This is a weaker relationship than composition or inheritance.
   
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


class BankEmployee:
    def __init__(self, name):
        self.name = name

    # Association: employee USES account
    def process_deposit(self, account, amount):
        account.deposit(amount)
        print(f"{self.name} deposited {amount} to {account.owner}'s account")


### usage
acc1 = BankAccount("John", 1000)
emp1 = BankEmployee("Alice")

emp1.process_deposit(acc1, 500)