############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   08/02/2026
#   Last Modified   :   09/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use OOP concept
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################


# Object-Oriented Programming Example
"""
Focus on objects that combine state + behavior.
Encapsulation protects data.
Methods enforce rules automatically.

✅ OOP:

    Data and behavior live together → easier to understand
    Rules are enforced automatically inside methods
    Easy to extend: you can create SavingsAccount, CurrentAccount, etc.

❌ Limitations:
    Slightly more code for simple tasks
    Mutating state can be tricky in concurrent programs

"""
class Account:
    def __init__(self, balance):
        self._balance = balance  # encapsulated data

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self._balance

# Usage
acc = Account(100)
print("Initial Account:", acc.get_balance())

print(acc.balance)

acc.deposit(50)
print("After Deposit:", acc.get_balance())

acc.withdraw(30)
print("After Withdraw:", acc.get_balance())

acc.withdraw(200)  # triggers rule
print("After Overdraw Attempt:", acc.get_balance())
