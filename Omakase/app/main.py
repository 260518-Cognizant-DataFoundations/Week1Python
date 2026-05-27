""" Omakase is a Japanese dining experience
where the chef selects and prepares a series of dishes for the customer.
The word "omakase" translates to "I'll leave it up to you".


We'll be creating an Omakase Command Line Interface (CLI) app that demonstrates:
1. User input and app output
2. Data structures (lists, dictionaries)
3. Control flow (review in a more realistic setting)
4. Functions (to organize/declutter our code and make it more reusable)
"""

# TODO: Possible extra functionality

print("""

*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
                    Welcome to the Omakase CLI app!
We'll be creating a personalized 3-course meal based on your preferences
*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*

First, what is your name?
""")

# Save the user's name via input()
name = input(">>> ")

print(f"Nice to meet you, {name}!")