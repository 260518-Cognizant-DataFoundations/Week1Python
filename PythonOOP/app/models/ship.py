"""
This Ship Class will be our example of ENCAPSULATION

We're going to define some attributes but we'll make them private this time
We'll only be able to access or change them through special methods called getters and setter
"""
from app.models.pirate import Pirate


class Ship:

    def __init__(self, name, num_cannonballs):
        # This one is public (which is default). Can be accessed/changed without restriction
        self.name = name
        # This one is __private - can only be accessed/changed through getters/setters
        self.__num_cannonballs = num_cannonballs

    # Getter - allows us to GET our private attribute
    def get_num_cannonballs(self):

        # Assume the user must be a "captain" to access this value
        # First, check the "role" attribute of the logged in user before allowing them to "get"

        # Also protects against "concurrency issues" -
        # Lets us set guardrails for users accessing the same data at the same time

        # Also helps protect against "accidental access" -
        # There is only one way to access this attribute

        return self.__num_cannonballs

    # Setter - allows us to SET our private attribute
    def set_num_cannonballs(self, new_num):
        # Same philosophy as getters, and we can demonstrate it here

        # Validation/Guardrails - make sure the value we're setting isn't negative
        if new_num < 0:
            print("Can't have negative cannonballs!")
            return

        self.__num_cannonballs = new_num


    # Method just for fun - takes a Pirate object and fires one cannonball
    # Note - EXPLICIT TYPING in the arg for Pirate - only pirates can fire the cannon
    def fire_cannon(self, pirate:Pirate):

        # Check if the argument is an instance of the Pirate class
        if not isinstance(pirate, Pirate):
            raise TypeError(f"Expected a Pirate object, got {type(pirate).__name__} instead.")

        # Note that we can get and set these private attributes DIRECTLY within the Class
        # Anywhere else, we need the getter/setter

        if self.__num_cannonballs <= 0:
            return "No cannonballs left captain!"

        # Decrement cannonballs by one
        self.__num_cannonballs -= 1

        print(f"{pirate.name} fired a cannonball from the {self.name}")

