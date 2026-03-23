############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   15/02/2026
#   Last Modified   :   15/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can define classUML Class Diagram Shapes
#classuml
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

class Animal:
    # Constructor method (runs automatically when object is created)
    def __init__(self, name, sound):
        self.name = name      # Attribute
        self.sound = sound    # Attribute

    # Method (behavior)
    def make_sound(self):
        print(self.name, "says", self.sound)

    def eat(self):
        print(self.name, "is eating.")

    def sleep(self):
        print(self.name, "is sleeping.")

# Create objects
dog = Animal("Buddy", "Woof")
cat = Animal("Kitty", "Meow")

# Use object methods
dog.make_sound()
dog.eat()

cat.make_sound()
cat.sleep()