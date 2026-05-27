# This is a UTILITY file - it contains data and functions that we use throughout the app
# I don't want to clutter main.py, and I want these things to be reusable

# TODO: Store the eaten foods in a dictionary

# TODO: Store the bill

# A function to find out the user's fav foods and come up with a meal for them
def generate_meal():

    # prompt the user to input their fav foods, which fills out the list (using append())
    print("What are your 3 favorite foods?")
    fav_foods = []

    # Get the user's food preference 3 times (3 different favorite foods)
    for i in range(3):
        food = input(f"Food #{i+1}: ")
        fav_foods.append(food)

    # Return statement - the function will "output" this (the list of foods in this case)
    return fav_foods

# Based on the generated meal, serve the user the chef's creation
# This one takes an argument called "meal"
# Based on the return of generated_meal(), we'll serve the user something
def serve_meal(meal):
    print(f"""
        **================W==============**
        Your appetizer: {meal[0]} Bisque
        Your entree: {meal[1]} Wellington
        Your dessert: Frozen {meal[2]}
        **================W==============**
    """)