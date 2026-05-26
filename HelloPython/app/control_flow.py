# We're going to create some hypothetical scenarios where control flow is necessary

print("================(If/Elif/Else)")

# These allow us to execute different code based on CONDITIONS.

# Let's make a list of strings and pick a random one (using the "random" module)
import random # We'd normally do this at the top of the file

vibes = ["otherworldly", "chill", "spooky"]

the_vibe = random.choice(vibes) # Super simple! Thanks random module

if the_vibe == "otherworldly":
    print("The vibe is otherworldly! Let's go to another dimension!")
elif the_vibe == "chill":
    print("I'm chilling.")
else:
    print("...I gotta go")



print("================(While Loops)")

# While loops will execute their block of code until the condition is False

meatballs_eaten = 0

while meatballs_eaten < 5:
    print("I'm eating a meatball")
    meatballs_eaten += 1 # This is the same as "meatballs_eaten = meatballs_eaten + 1"

# The while loop will break once meatballs_eaten is no longer < 5.
print(f"Ok I'm full. Meatballs eaten: {meatballs_eaten}")


print("================(For Loops)")

# For loops are used to iterate over sequences like lists
# Or just execute some code a set number of times

# We can make for loops with the "range" function - this one loops 5 times
for i in range(5):
    print(f"This is loop number {i}")

"""Lists and other sequences (like ranges) are ZERO-INDEXED
 This means they start at position (aka INDEX) 0.
 -So the first loop in a for loop is loop number 0
 -The first index in a sequence is index 0
"""

# Here's an example of using zero indexing with the list we made above
print(vibes[0])
# print(vibes[3]) # IndexError: list index out of range

# Let's loop through a list (using the one we already have)
for vibe in vibes:
    print(f"The vibe is {vibe}")
