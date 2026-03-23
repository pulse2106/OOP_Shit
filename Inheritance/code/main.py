############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   19/02/2026
#   Last Modified   :   19/02/2026
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can define base class & extend it with inheritance
#classuml
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

## Base class
class Animal:
    def __init__(self, name):
        self.name = name
        self.Name=name
    def make_sound(self):
        print(f"{self.name} makes a sound")

    def eat(self):
        print(f"{self.name} is eating")


# Derived/extended class Dog
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says Woof")

# Derived/extended class Cat
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow")

# Derived/extended class Cow
class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says Moo")
    
    def eat(self):
        print(f"{self.name} i seating grass..")

### Usage
dog1 = Dog("Buddy")
cat1 = Cat("Kitty")
cow1 = Cow("Bessie")

animals = [dog1, cat1, cow1]    ### makes the animal list

### loop through animal list and call methods
for animal in animals:
    animal.make_sound()
    animal.eat()
    print("---")



""" NOTES 
*** Inheritance allows one class to reuse the properties and methods of another class.
A Dog is an Animal
A Cat is an Animal
A Cow is an Animal

So we create:

    A base (parent) class → Animal
    Several derived (child) classes → Dog, Cat, Cow

It helps avoid code duplication.
It models real-world relationships.
"""