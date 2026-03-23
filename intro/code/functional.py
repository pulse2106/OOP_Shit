############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   08/02/2026
#   Last Modified   :   09/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use functional programming
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

# Functional Programming Example

"""
Focus on functions and data separately.

Data is usually immutable; functions return new values.

No “owner” of the data; rules must be manually enforced.

✅ FP:

    Predictable results (no hidden side-effects)
    Easy to test small functions

❌ Limitations:

    Must pass the account every time
    Rules are not enforced automatically
    Harder to model real-world objects like accounts, loans, etc.
"""

account = {"balance": 100}  ### Account represented as a dictionary

# Deposit function (returns a new account)
def deposit(acc, amount):
    return {"balance": acc["balance"] + amount}

# Withdraw function (returns a new account)
def withdraw(acc, amount):
    if acc["balance"] >= amount:
        return {"balance": acc["balance"] - amount}
    else:
        print("Insufficient balance!")
        return acc  # no change


print("Initial Account:", account)
account = deposit(account, 50)
print("After Deposit:", account)

account = withdraw(account, 30)
print("After Withdraw:", account)

account = withdraw(account, 200)  # triggers rule
print("After Overdraw Attempt:", account)
