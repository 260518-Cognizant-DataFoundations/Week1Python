"""
The Pirate Class is a SUBCLASS of Person -
It INHERITS all the attributes and methods of Person

We can add members specific to Pirate
And Person can have tons of subclasses that all inherit from it
This promotes POLYMORPHISM.
"""
# What's up with this import statement?
# They're in the same package so we don't need to write the full path
from .person import Person

class Pirate(Person):

    # We'll change the constructor to reflect Pirates more than the generic Person
    def __init__(self, name, age, saltiness, bounty):
        # super() calls to the constructor of the parent class (AKA superclass)
        super().__init__(name, age)
        self.saltiness = saltiness
        self.bounty = bounty

    # We can add methods specific to Pirate
    def plunder(self):
        return f"{self.name} is plundering... respectfully"

    # AND we can change the behavior of inherited methods
    def say_hello(self):

        if self.saltiness < 50:
            return f"Hello, I be {self.name}. Me bounty is {self.bounty}"

        # If the if block doesn't run, this block will run instead
        return f"Ahoy! I be {self.name}, arrrrgh me bounty be {self.bounty}"

    # NOTE: eat_food DOES exist and can be used by Pirates
    # But it's directly inherited, and we haven't changed it.