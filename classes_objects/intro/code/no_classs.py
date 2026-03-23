############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   15/02/2026
#   Last Modified   :   15/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows code complexity without OOP
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################
"""
We must:
    Create separate variables for each animal
    Pass variables manually to every function
    Manage data carefully.

If we have 20 animals, we need:
    20 name variables
    20 sound variables
    Manual function calls for each

*** This becomes messy very quickly.
"""

# Dog data
dog_name = "Buddy"
dog_sound = "Woof"

# Cat data
cat_name = "Kitty"
cat_sound = "Meow"


# Functions
def make_sound(name, sound):
    print(name, "says", sound)

def eat(name):
    print(name, "is eating.")

def sleep(name):
    print(name, "is sleeping.")


# Using functions
make_sound(dog_name, dog_sound)
eat(dog_name)

make_sound(cat_name, cat_sound)
sleep(cat_name)
