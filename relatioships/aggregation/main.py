############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   26/02/2026
#   Last Modified   :   26/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#   This example shows a Bank class that aggregates Customer objects. The Bank class has a list of customers, 
#       but the customers can exist independently of the bank. If the bank is deleted, the customers still exist.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""
    - Customer objects are created outside Bank
    - Bank only stores references
    - If Bank object is deleted → Customers still exist

    This is called Aggregation (Has-A relationship)
    *** This is a weaker relationship than composition.

"""

class Customer:
    def __init__(self, name):
        self.name = name

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []   # Bank has customers

    def add_customer(self, customer):
        self.customers.append(customer)

    def show_customers(self):
        for customer in self.customers:
            print(customer.name)


# Creating customers independently
c1 = Customer("Ajith")
c2 = Customer("Nimal")

bank1 = Bank("ABC Bank")

bank1.add_customer(c1)  ### Bank aggregates customer
bank1.add_customer(c2)  ### Bank aggregates customer

bank1.show_customers()