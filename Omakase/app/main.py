""" Omakase is a Japanese dining experience
where the chef selects and prepares a series of dishes for the customer.
The word "omakase" translates to "I'll leave it up to you".


We'll be creating an Omakase Command Line Interface (CLI) app that demonstrates:
1. User input and app output
2. Data structures (lists, dictionaries)
3. Control flow (review in a more realistic setting)
4. Functions (to organize/declutter our code and make it more reusable)
"""
import restaurant_util as ru

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

# Where does hungry turn False in this?
while hungry:

    # Generate a 3-course meal, save the value to use in serve_meal below
    generated_meal = ru.generate_meal()
    print(f"Ok! I can work with {generated_meal}")

    # Serve the user
    ru.serve_meal(generated_meal)

    # Ask the user if they are still hungry
    # THIS is what determines if the while loops breaks or not
    print("Are you still hungry? (yes/no)")
    still_hungry = input(">>> ").lower()

    if still_hungry == "no":
        print("Thank you! Here's your receipt:")

        # Showing off the datetime module
        from datetime import datetime

        print(datetime.now().strftime("%Y-%m-%d"))

        # Print the contents of the eaten_foods dictionary
        print(f"""
        -Apps: {ru.eaten_foods["appetizers"]}
        -Entrees: {ru.eaten_foods["entrees"]}
        -Desserts: {ru.eaten_foods["desserts"]}
        """)

        # Print the user's bill with 10% sales tax
        print(f"That will be: ${ru.bill*1.1:.2f}")
        # :.2f? That's saying "take this float and reduce it to 2 decimal places"

        hungry = False # THIS BREAKS THE LOOP!
    elif still_hungry == "yes":
        print("Great! Let's make you another meal!")
    else:
        print("Huh? I didn't understand you, so I'll just keep feeding you...")