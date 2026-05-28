"""
This demo will be your reference for Classes, Objects,
and the 4 Pillars of OOP in a real code example -

We'll see Inheritance and Polymorphism in our Person and Pirate Classes
Then we'll explore Encapsulation and Abstraction with our Ship Class
"""

# Person lives in a different file/package, so we need to import it
from app.models.person import Person
from app.models.pirate import Pirate

print("======================(Using the Person Superclass)")

# Instantiating a Person object (creating a Person object)
person1 = Person("Ben", 28)

# Invoke the methods of the Person class via the person1 object
print(person1.say_hello())
print(person1.eat_food("Pizza"))

# Instantiate ANOTHER Person object with different attributes
person2 = Person("Sophie", 25)

print(person2.say_hello())
print(person2.eat_food("Salad"))

print("=======================(Using the Pirate Subclass)")

# Instantiating 2 Pirate objects
pirate1 = Pirate("Jack Sparrow", 40, 75, 1000000)
pirate2 = Pirate("Nobeard", 19, 10, 100)

# Invoke Jack Sparrow's methods first
print(pirate1.say_hello())
print(pirate1.eat_food("Rum"))
print(pirate1.plunder())

# Now invoking the other pirate
print(pirate2.say_hello())
print(pirate2.eat_food("Ship's Biscuits"))
print(pirate2.plunder())