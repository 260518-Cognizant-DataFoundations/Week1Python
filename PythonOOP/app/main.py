"""
This demo will be your reference for Classes, Objects,
and the 4 Pillars of OOP in a real code example -

We'll see Inheritance and Polymorphism in our Person and Pirate Classes
Then we'll explore Encapsulation and Abstraction with our Ship Class
"""

# Person lives in a different file/package, so we need to import it
from app.models.person import Person

print("======================(Using the Person Class)")

# Instantiating a Person object (creating a Person object)
person1 = Person("Ben", 28)

# Invoke the methods of the Person class via the person1 object
print(person1.say_hello())
print(person1.eat_food("Pizza"))

# Instantiate ANOTHER Person object with different attributes
person2 = Person("Sophie", 25)

print(person2.say_hello())
print(person2.eat_food("Salad"))