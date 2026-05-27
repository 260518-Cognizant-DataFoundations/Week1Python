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

# This boolean will determine whether the while loop menu continues to execute
hungry = True

while hungry:
    print("[customer gets fed here]")

    # TODO: generate a 3 course meal

    # TODO: serve the user

    # Ask the user if they are still hungry
    # THIS is what determines if the while loops breaks or not
    print("Are you still hungry? (yes/no)")
    still_hungry = input(">>> ").lower()

    if still_hungry == "no":
        print("Ok thanks bye")
        hungry = False # THIS BREAKS THE LOOP!
    elif still_hungry == "yes":
        print("Great! Let's make you another meal!")
    else:
        print("Huh? I didn't understand you, so I'll just keep feeding you...")