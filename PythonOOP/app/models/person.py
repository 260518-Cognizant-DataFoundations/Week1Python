"""
This Person Class is used to MODEL a generic person (Hence "models" folder)

It has an attribute for name and age (every Person object will have unique values for these)
It has 2 methods for eat and say hello (every Person will be able to do these things)
"""

class Person:

    # This is the "constructor method". It defines the attributes of the class (name and age)
    # We call this method to create a new instance of Person (a person OBJECT)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instantiating a Person object may look like this: person = Person("John", 30)

    # Defining some methods for Person (actions a Person can take)

    def eat_food(self, food):
        return f" {self.name} is eating {food}"

    def say_hello(self):
        return f"Hello, my name is {self.name} and I'm {self.age}"