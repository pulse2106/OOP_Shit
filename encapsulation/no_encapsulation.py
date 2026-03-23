
############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com,ajith.de-silva@epita.fr)
#   Created         :   23/02/2026
#   Last Modified   :   23/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows issue when access critial data without encapsulation
#classuml
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""
Anyone can change the balance to a negative value!
    **** This is unsafe.
    **** any application using this class can break if balance is negative.
    **** We have no control over how balance is modified.
    **** This will break/crahs the application if we try to use balance for calculations.

"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance   #### Public variable

account1 = BankAccount("Ajith", 1000)

account1.balance = -5000    #### Directly modifying balance (Danger!)

print(account1.balance)
