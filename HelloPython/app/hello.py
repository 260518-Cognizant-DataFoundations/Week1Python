# This is a comment. It won't affect the code

# This is a print statement. It "prints" things in the console below
print("Hello Python!")

""" This is a 
 multi
 line
 comment ...
 
 Just in case you need to lay out a BIG comment, for documentation, etc"""

# =============== DATATYPES ===============

# Datatypes are the TYPES of DATA we can use in Python.
# We'll see some here, and JUST talk about some niche types for now

# Strings - A sequence of characters (in other, they're text)
my_name = "John Pork"
# We can print strings easily!
print(my_name)

# Numbers - Can be integers (whole numbers) or floats (decimals)
my_age = 28
my_weight = 50.7

# Booleans - Represents True or False values
is_student = True

if(is_student):
    print("I am a student!")


# We don't JUST set booleans with True/False. They're usually the result of a comparison.
if(5 < 3):
    print("5 is less than 3")


# Lists - A collection of values. They can be any datatype.
# Lists are ordered, and mutable (them and their values can be changed)
my_favorite_animals = ["Axolotl", "Dog", "Capybara"]
my_favorite_numbers = [42, 24, 25, 3.14]

# Tuples - Similar to lists, but they're immutable (can't be changed)
ny_coordinates = (40.7128, -74.0060) # Coordinates for NYC - shouldn't change

# Dictionaries - A collection of key-value pairs. Unordered and mutable
# Property syntax is "key":value
person = {
    "name":"Bob",
    "age":30,
    "is_student":False
}

# We can access the values of a dict by using the key
print(person["name"])
print(person["age"])
if(person["is_student"]):
    print(person["name"] + " is a student.")


# Formatted Printing (using f-strings)
# Let's use the first variables we defined above
print(f"My name is {my_name}")
# Here, we used an f-string to insert the value of my_name into the string


# Here's an example of a variable defined in the "local" namespace
def my_function():
    local_var = "I'm not accessible outside of this function"

print(local_var) # NameError: "name 'local_var' is not defined"