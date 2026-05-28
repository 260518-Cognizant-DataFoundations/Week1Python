# First, let's revise the REUSABILITY of functions

# We can call functions multiple times, instead of rewriting them every time
# It's easy to take this for granted - but look how versatile this method is
def start_game(players):

    # len() is a useful function that returns the LENgth of a list or other sequence

    if len(players) < 1:
        print("Invalid number of players. Please enter 1 or more.")
        return # We can return early if given invalid input, terminating the function

    if len(players) == 1:
        print("Starting a single player game...")
    elif len(players) == 2:
        print("Starting a two player game...")
    else:
        print("Starting a free-for-all game")

lonely_gamer = ["Bob"]
buddy_gamers = ["Joe", "Billy"]
squad = ["Bob", "Joe", "Billy", "Sally"]

# We can call the SAME function with different arguments to get different results
start_game(lonely_gamer)
start_game(buddy_gamers)
start_game(squad)


print("===============(Lambdas)")

"""
Lambdas, on the other hand, are NOT reusable. 
They are meant to be used once, and then discarded.
Ok... why would we do that?

- Lambdas are often used as args in higher-order functions 
(which are functions that take other functions as an argument)

- Or as a quick way to create a function without taking up space

- I pretty much ONLY use lambdas when a function arg calls for it,
or when I know for a fact that I just need a quick function I'll never want to reuse
"""

# Here's a function that takes a function (I hate this function btw - too general)
def versatile_calculation(func, value):
    return func(value)

# We can use a lambda as the func argument! Or create a standalone function, taking up space...
result = versatile_calculation(lambda x : x ** 2, 5)
print(result) # This will print 25, since the lambda is squaring the input value

# So the return looks like this: return 5**2, which is 25


# Now a more realistic example, using the built-in sorted() function,
# it helps us SORT sequences
# which takes a "key" argument that expects a function

names = ["Jimm", "Jom", "Jummmy", "Jammmyyy"]

# We can sort the names by their length using a lambda as the key function
# BTW - if we DIDN'T supply a key function, sorted() go by natural order (numerical, alphabetical)
sorted_names = sorted(names, key=lambda name: len(name))

print(sorted_names) # This will print the names sorted by length

# So as you can see, lambdas are a bit more niche. Regular functions are way more common
# But lambdas can be super useful when you just need a quick, specific, one-time function
