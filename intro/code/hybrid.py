############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   08/02/2026
#   Last Modified   :   09/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use functional programming + OOP together
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

class Account:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amt):
        self._balance = self._pure_add(self._balance, amt)

    def _pure_add(self, bal, amt):  # functional style
        return bal + amt


acc = Account(100)
acc.deposit(50)

print(acc.balance)

acc._pure_add(1000,100)