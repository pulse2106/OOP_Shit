
############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com,ajith.de-silva@epita.fr)
#   Created         :   23/02/2026
#   Last Modified   :   23/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use inheritance to create a base class and extend it with derived classes.
#       We also show how to use abstract methods to enforce implementation in derived classes.
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

#### import bankccount and derived classes
from Inheritance.code.bank.bankaccount import BankAccount
from Inheritance.code.bank.savings_account import SavingsAccount
from Inheritance.code.bank.current_account import CurrentAccount


#### Create accounts
savings = SavingsAccount("Alice", 5000, 5)  #### 5% interest
current = CurrentAccount("Bob", 2000, 1000)  #### overdraft 1000

#### Show account type
print(savings.account_type())
print(current.account_type())

#### Deposit, withdraw, and interest
savings.deposit(1000)
savings.add_interest()
savings.withdraw(2000)

current.withdraw(2500)  #### Allowed due to overdraft
current.withdraw(1000)  #### Exceeds overdraft