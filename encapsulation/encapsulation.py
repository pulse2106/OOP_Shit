############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com,ajith.de-silva@epita.fr)
#   Created         :   23/02/2026
#   Last Modified   :   23/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows usage of encapsulation with methods
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # Private variable

    #### Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    #### Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or invalid amount.")

    #### Getter method to check balance
    def get_balance(self):
        return self.__balance
    

#### usage
account1 = BankAccount("john", 1000)

account1.deposit(500)
account1.withdraw(200)

print("Current Balance:", account1.get_balance())

# Trying to access private variable directly
print(account1.__balance)   # ❌ This will give an error